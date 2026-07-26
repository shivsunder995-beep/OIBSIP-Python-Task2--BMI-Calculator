import sqlite3

DB_NAME = "bmi.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_record(name, weight, height, bmi, category):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO bmi_records(name,weight,height,bmi,category)
        VALUES(?,?,?,?,?)
        """, (name, weight, height, bmi, category))

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        raise Exception(f"Database Error: {e}")


def get_records(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT bmi,date
    FROM bmi_records
    WHERE name=?
    ORDER BY date
    """, (name,))

    data = cursor.fetchall()

    conn.close()

    return data