import streamlit as st
from crud import get_connection
import pandas as pd

st.title("Welcome to Salary and Compensation Insights Page!")


def get_avg_salary_by_title():
    """Return job titles and their average salaries."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT job_title as 'JOB-TITLE',AVG(salary_in_usd) AS 'Avg-Salary' 
        FROM db.salaries
        GROUP BY job_title 
        ORDER BY 'Avg-Salary' DESC
    """)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

data = get_avg_salary_by_title()

# Convert to DataFrame
df = pd.DataFrame(data, columns=["JOB-TITLE", "Avg-Salary(US Dollars)"])

# Show as table
st.subheader("Average Salary by Job Title")
st.dataframe(df)

# Optional: Show as bar chart
# st.subheader("Average Salary by Job Title (Chart)")
# st.bar_chart(df.set_index("JOB-TITLE"))