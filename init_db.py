import sqlite3
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

def init_db():
    # First remove existing database if it exists
    import os
    if os.path.exists('inventory.db'):
        os.remove('inventory.db')
    
    # Connect to database
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    
    # Read schema
    with open('schema.sql', 'r') as f:
        schema = f.read()
    
    # Execute schema
    conn.executescript(schema)
    
    # Create admin user
    admin_password = generate_password_hash('admin123')  # Change this password in production
    try:
        c.execute('''
            INSERT INTO users (employee_id, password, name, role)
            VALUES (?, ?, ?, ?)
        ''', ('ADMIN001', admin_password, 'System Administrator', 'admin'))
        print("Admin user created successfully!")
    except sqlite3.IntegrityError:
        print("Admin user already exists")

    # Add some test data
    test_data = [
        ('TSP', 'AVU - Atmospheric & Vacuum Unit', 1500, 800, 300, 2000, 'Kilogram (kg)', 
         (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d'), 
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ('ARI-100 EXL', 'FCC - Fluid Catalytic Cracking', 500, 500, 200, 800, 'Litre (L)', 
         (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d'), 
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ('IMX-05 A Catalyst', 'DCU - Delayed Coker Unit', 1000, 800, 300, 1500, 'Kilogram (kg)', 
         (datetime.now() + timedelta(days=120)).strftime('%Y-%m-%d'), 
         datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        ('E-Catalyst', 'PRU - Propylene Recovery Unit', 500, 400, 150, 750, 'Kilogram (kg)', 
         (datetime.now() + timedelta(days=150)).strftime('%Y-%m-%d'), 
         datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    ]
    
    conn.executemany("""
        INSERT INTO chemicals (name, unit, opening_balance, received_quantity, consumption_quantity, closing_balance, measurement_unit, expiry, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, test_data)
    
    conn.commit()
    
    # Verify the tables exist and have data
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM chemicals")
    chem_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    print(f"Database initialized successfully with {chem_count} test records and {user_count} users!")
    
    conn.close()

if __name__ == '__main__':
    init_db() 