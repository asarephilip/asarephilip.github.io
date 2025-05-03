import psycopg2
import numpy as np

# Connect to your database
conn = psycopg2.connect(
    dbname="vector_db",
    user="postgres",
    password="postgres",
    host="127.0.0.1"
)
# Create a table with a vector column
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE items (
            id serial PRIMARY KEY,
            embedding vector(3)
        );
    """)
    conn.commit()