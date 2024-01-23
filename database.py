import sqlite3
import pandas as pd

def create_connection():
    """Create a database connection to the SQLite database."""
    return sqlite3.connect('jobs.db')

def create_job(title, company, pay_range, link, industry, level, application_date, notes):
    try:
        with create_connection() as conn:
            sql = '''INSERT INTO jobs(title, company, pay_range, link, industry, level, application_date, notes)
                     VALUES(?,?,?,?,?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, (title, company, pay_range, link, industry, level, application_date, notes))
            conn.commit()
    except Exception as e:
        print(f"Error in create_job: {e}")
        raise e

def get_all_jobs():
    try:
        with create_connection() as conn:
            sql = 'SELECT * FROM jobs'
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return pd.DataFrame(rows, columns=['id', 'title', 'company', 'pay_range', 'link', 'industry', 'level', 'application_date', 'notes'])
    except Exception as e:
        print(f"Error in get_all_jobs: {e}")
        return pd.DataFrame()

def init_db():
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS jobs (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        company TEXT,
                        pay_range TEXT,
                        link TEXT,
                        industry TEXT,
                        level TEXT,
                        application_date DATE,
                        notes TEXT
                    );''')
        conn.commit()

def test_db_connection():
    try:
        with create_connection() as conn:
            cur = conn.cursor()
            cur.execute('SELECT 1')
            result = cur.fetchone()
            print("Database connection successful." if result else "Database connection failed.")
    except Exception as e:
        print(f"Database connection test failed: {e}")

if __name__ == "__main__":
    init_db()
    test_db_connection()
    # Uncomment these lines to test direct data insertion and retrieval
    create_job("Test Job", "Test Company", "<$30000", "http://example.com", "Technology", "Entry Level", "2023-01-01", "Test notes")
    print(get_all_jobs())
