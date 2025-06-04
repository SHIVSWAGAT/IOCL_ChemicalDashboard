from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file, jsonify
import sqlite3
from datetime import datetime, timedelta
import pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import io

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Session timeout after 30 minutes
app.config['SESSION_COOKIE_SECURE'] = False  # Allow cookies over HTTP in development
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent JavaScript access to session cookie
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Protect against CSRF
DATABASE = 'inventory.db'

CHEMICALS = [
    "TSP", "ARI-100 EXL", "IMX-05 A Catalyst", "APS", 
    "PTBC", "Ammonium Polysulphide", "E-Catalyst", 
    "High TAN CI 6687"
]

UNITS = [
    "AVU - Atmospheric & Vacuum Unit",
    "SR LPG Treater - Straight Run LPG Treater",
    "DCU - Delayed Coker Unit",
    "FCC - Fluid Catalytic Cracking",
    "FCC LN Treater - FCC Light Naphtha Treater",
    "PRU - Propylene Recovery Unit"
]

MEASUREMENT_UNITS = [
    "Kilogram (kg)", "Litre (L)", "Milligram (mg)", "Millilitre (mL)",
    "Gram (g)", "Ton (t)", "Cubic Metre (m³)"
]

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE employee_id = ?', (employee_id,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['employee_id'] = user['employee_id']
            session['name'] = user['name']
            session['role'] = user['role']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid employee ID or password.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    response = redirect(url_for('login'))
    # Clear all cookies and set cache control headers
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    flash('You have been logged out successfully.', 'success')
    return response

@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db_connection()
    total_chemicals = conn.execute('SELECT COUNT(*) FROM chemicals').fetchone()[0]
    active_units = conn.execute('SELECT COUNT(DISTINCT unit) FROM chemicals').fetchone()[0]
    low_stock = conn.execute('SELECT COUNT(*) FROM chemicals WHERE closing_balance < 1000').fetchone()[0]
    expired = conn.execute('SELECT COUNT(*) FROM chemicals WHERE expiry < date("now")').fetchone()[0]
    distribution = conn.execute('SELECT unit, COUNT(*) as count FROM chemicals GROUP BY unit').fetchall()
    recent = conn.execute('SELECT * FROM chemicals ORDER BY id DESC LIMIT 5').fetchall()
    conn.close()
    return render_template('dashboard.html',
                           total=total_chemicals,
                           active=active_units,
                           low=low_stock,
                           expired=expired,
                           distribution=distribution,
                           recent=recent)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_chemical():
    if request.method == 'POST':
        name = request.form['chemical']
        unit = request.form['unit']
        opening_balance = int(request.form['opening_balance'])
        received_quantity = int(request.form['received_quantity'])
        consumption_quantity = int(request.form['consumption_quantity'])
        closing_balance = opening_balance + received_quantity - consumption_quantity
        measurement_unit = request.form['measurement_unit']
        expiry = request.form['expiry']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO chemicals (name, unit, opening_balance, received_quantity, consumption_quantity, closing_balance, measurement_unit, expiry, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, unit, opening_balance, received_quantity, consumption_quantity, closing_balance, measurement_unit, expiry, timestamp))
        conn.commit()
        conn.close()
        flash('Chemical added successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('add_chemical.html', 
                         chemicals=CHEMICALS, 
                         units=UNITS, 
                         measurement_units=MEASUREMENT_UNITS)

@app.route('/inventory')
@login_required
def view_inventory():
    conn = get_db_connection()
    chemicals = conn.execute('SELECT * FROM chemicals').fetchall()
    conn.close()
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('view_inventory.html', chemicals=chemicals, current_date=current_date)

@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_chemical(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM chemicals WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Chemical deleted successfully!', 'success')
    return redirect(url_for('view_inventory'))

@app.route('/unit', methods=['GET', 'POST'])
@login_required
def add_unit():
    if request.method == 'POST':
        new_unit = request.form['unit']
        if new_unit and new_unit not in UNITS:
            UNITS.append(new_unit)
        return redirect(url_for('dashboard'))
    return render_template('add_unit.html', units=UNITS)

@app.route('/export/excel')
@login_required
def export_excel():
    conn = get_db_connection()
    chemicals = conn.execute('SELECT * FROM chemicals').fetchall()
    conn.close()
    
    # Convert to DataFrame
    df = pd.DataFrame(chemicals)
    
    # Create Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Inventory', index=False)
    
    output.seek(0)
    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=f'inventory_{datetime.now().strftime("%Y%m%d")}.xlsx'
    )

@app.route('/export/pdf')
@login_required
def export_pdf():
    conn = get_db_connection()
    chemicals = conn.execute('SELECT * FROM chemicals').fetchall()
    conn.close()
    
    return render_template('export_pdf.html', 
                         chemicals=chemicals,
                         current_date=datetime.now().strftime('%Y-%m-%d'))

@app.route('/check_session')
def check_session():
    return jsonify({'authenticated': 'user_id' in session})

@app.route('/download_report')
def download_report():
    return send_file('Chemical_Dashboard_Project_Report.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
