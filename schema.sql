DROP TABLE IF EXISTS chemicals;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'employee'
);

CREATE TABLE chemicals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    unit TEXT NOT NULL,
    opening_balance INTEGER NOT NULL,
    received_quantity INTEGER NOT NULL,
    consumption_quantity INTEGER NOT NULL,
    closing_balance INTEGER NOT NULL,
    measurement_unit TEXT NOT NULL,
    expiry DATE NOT NULL,
    timestamp TEXT NOT NULL
);
