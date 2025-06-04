# IOCL_ChemicalDashboard

Overview:

The Chemical Inventory Management Dashboard is a comprehensive, web-based application developed to address the challenges of chemical inventory management in large-scale industrial environments such as oil refineries. Traditionally, chemical stock tracking in such settings is performed manually, which can lead to errors, inefficiencies, and compliance risks. This project, created during a summer internship at Indian Oil Corporation Limited (Paradip Refinery), leverages modern web technologies to provide a centralized, secure, and user-friendly solution for managing chemical inventories.The dashboard facilitates the entire lifecycle of chemical inventory data. From the initial entry of stock to tracking daily consumption, received quantities, and monitoring expiry dates, every aspect is handled digitally. The system not only improves accuracy and operational efficiency but also enhances traceability and accountability, which are critical in environments dealing with hazardous materials.

Objectives :

The primary objectives of this project are:

1. Centralized Platform for Chemical Stock Data
To unify all chemical inventory information from different refinery units into a single platform, making data easily accessible and manageable for authorized users.

2. Elimination of Manual Errors
Manual record-keeping is prone to human error, leading to discrepancies in stock levels and potential safety hazards. This system automates data entry and calculations, greatly reducing the risk of mistakes.

3. Real-Time Data Tracking and Updates
All inventory data is updated in real time, ensuring that users always have access to the latest information regarding stock levels, consumption, and received quantities.

4. Visual Insights for Quick Decision-Making
The dashboard provides visual indicators and charts that allow users to instantly assess the health of chemical stocks, identify critical shortages, or spot expired chemicals.

5. Flexible Data Export for Reporting and Auditing
Users can export inventory data in PDF or Excel formats, facilitating easy reporting, compliance checks, and audits.

6. Secure Access Control
A robust login system ensures that only authenticated users can access or modify sensitive chemical data, with different permissions for admins and employees.

7. Enhanced Compliance and Accountability
By maintaining detailed logs of all inventory transactions and updates, the system supports regulatory compliance and helps track responsibility for stock management.


Technologies Used :

This project is built using a modern stack of technologies, each chosen for its suitability to the task:

 1.Python (Flask Framework): Acts as the backend server, handling business logic, routing, user authentication, and API endpoints.

 2.SQLite: A lightweight, file-based relational database used to store user credentials and all chemical inventory data securely.

 3.HTML, CSS & Bootstrap: Used to create responsive, visually appealing, and easy-to-navigate front-end interfaces.

 4.JavaScript (with Chart.js): Powers dynamic charts and interactive dashboard elements, providing real-time data visualization.

 5.Jinja2: Template engine for rendering dynamic HTML pages with server-side data.

 6.Pandas & xlsxwriter: Used for exporting inventory data to Excel spreadsheets, supporting advanced data analysis and reporting.

 7.xhtml2pdf: Converts HTML tables and views into downloadable, print-ready PDF documents for offline use and compliance.

Key Features :

1.🔐 Secure Login System
Employee Authentication: Every user must log in using their unique Employee ID and password. This prevents unauthorized access to sensitive chemical data.

Role-Based Access: There are two user roles—Admin and Employee. Admins have full control, including the ability to add or update chemicals, while Employees have restricted access, typically limited to viewing and searching inventory data.

Session Management: The system ensures that only active, authenticated sessions can interact with the application, further enhancing security.

2.📊 Interactive Dashboard

Central Hub: After logging in, users are taken to the dashboard, which serves as the main control center for all inventory activities.

Summarized Data: The dashboard displays a comprehensive table of all chemicals, including key details such as opening balance, quantities received and consumed, closing stock, expiry dates, and measurement units.

Visual Indicators: Color-coded tags and icons highlight low stock levels, expired chemicals, or other critical conditions, enabling users to take prompt action.

Live Updates: All data on the dashboard is updated in real time, ensuring users always see the most current information.

3.🏭 Unit-wise Inventory Tracking

Departmental Organization: Each chemical is associated with a specific unit within the refinery (e.g., AVU, FCC, DCU, PRU). This allows for clear separation and management of chemicals by department.

Responsibility Breakdown: Supervisors and staff can focus on the chemicals relevant to their unit, reducing confusion and improving accountability.

Easy Filtering: Users can filter inventory data by unit, making it simple to locate and manage chemicals for a particular section of the refinery.

4.📤 Export to PDF and Excel

PDF Export: Users can generate a print-friendly, time-stamped PDF report of the current inventory view. This is useful for compliance, audits, or sharing with management.

Excel Export: Inventory data can be exported to Excel spreadsheets, enabling advanced analysis, long-term storage, or integration with other business systems.

Traceability: All exported files include the current date and time, ensuring traceability and supporting regulatory requirements.

5.🛠 Add & Manage Chemicals

Admin Controls: Admin users can add new chemicals to the system or update the details of existing stocks.

Tracked Fields: Each chemical entry includes the chemical name, associated unit, opening balance, quantities received and consumed, closing balance (calculated automatically), measurement unit (e.g., kg, L), expiry date, and a timestamp of the last update.

Audit Trail: Every transaction or update is logged with a timestamp, ensuring full traceability and accountability for all inventory changes.

6.🔎 Search & Filter

Keyword Search: Users can quickly find chemicals by typing part of the chemical name, unit, or measurement type.

Drop-Down Filters: The interface includes drop-down menus for filtering by unit or chemical name, making it easy to narrow down results.

Instant Results: The inventory table updates in real time as users apply search terms or filters, ensuring a smooth and efficient user experience.

7.🔄 Auto Session Check

Session Validation: The system regularly checks the validity of user sessions. If a session becomes inactive or unauthorized, the user is logged out automatically.

Enhanced Security: This feature helps prevent unauthorized access and ensures that only legitimate users can interact with the application.

Use Case in IOCL (Paradip Refinery) :

In a complex facility like IOCL Paradip, hundreds of chemicals are consumed daily for processes such as distillation, catalytic cracking, coking, and recovery. Managing these chemicals manually can lead to several problems:

Stock Mismatches: Manual errors can cause discrepancies between recorded and actual stock, leading to shortages or overstocking.

Improper Usage: Without real-time tracking, chemicals may be overused or underused, affecting process efficiency and safety.

Expired Chemicals: Lack of expiry tracking can result in the use of expired chemicals, posing safety and compliance risks.

Regulatory Compliance: Manual records are difficult to audit and may not meet stringent safety and environmental regulations.

The Chemical Inventory Management Dashboard addresses these challenges by automating inventory tracking, providing real-time visibility, and ensuring that every transaction is logged and auditable. This empowers plant managers, engineers, and supervisors to make informed decisions, maintain compliance, and improve overall operational efficiency.


Future Enhancements :

To further improve the system, the following features are planned:

Automated Notifications: Email or SMS alerts for critical stock levels or chemicals nearing expiry.

Procurement Integration: Direct integration with purchasing systems to automate reordering of chemicals.

Role-Specific Dashboards: Customized interfaces for supervisors, operators, and managers, each showing relevant data and controls.

Mobile Support: Responsive design or a dedicated mobile app for on-the-go inventory management.

Multi-User Collaboration: Real-time collaboration features and detailed update logs to track changes by user.

Conclusion :

The Chemical Inventory Management Dashboard demonstrates how modern web technologies can transform the management of critical industrial resources. By providing a secure, real-time, and user-friendly platform, this project enhances operational clarity, safety, and efficiency in chemical inventory management. The system not only reduces errors and improves compliance but also empowers refinery staff with the tools they need to make better, faster decisions.



Developed by Shiv Swagat Subudhi during a summer internship at Indian Oil Corporation Limited (Paradip Refinery). For any questions or queries, please contact at shivswagatsubudhi@gmail.com.




