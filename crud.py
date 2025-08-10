import mysql.connector

def get_connection():
    """Create and return a MySQL connection."""
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database="db"
    )

# Execute query
# mycursor.execute("SELECT COUNT(*) FROM salaries")
#
# # Fetch result
# result = mycursor.fetchone()  # returns a tuple
# print(f"Total rows in salaries table: {result[0]}")
#
# # Clean up
# mycursor.close()
# conn.close()
