import mysql.connector

def get_connection():
    """Create and return a MySQL connection."""
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database="db"
    )

