import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),  # Replace with your MySQL username
        password=os.getenv("MYSQL_PASSWORD"),  # Replace with your MySQL password
        database=os.getenv("MYSQL_DB")
    )
    return connection

def log_transaction(transaction_id, status):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO transaction_log (transaction_id, status) VALUES (%s, %s)"
    cursor.execute(query, (transaction_id, status))
    connection.commit()
    connection.close()
