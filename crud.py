import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database="db"
    )
    mycursor = conn.cursor()
    print("Connection Established")
except mysql.connector.Error as e:
    print(f"Connection Error: {e}")

# Execute query
mycursor.execute("SELECT COUNT(*) FROM salaries")

# Fetch result
result = mycursor.fetchone()  # returns a tuple
print(f"Total rows in salaries table: {result[0]}")

# Clean up
mycursor.close()
conn.close()
