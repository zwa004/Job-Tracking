import sqlite3
import pandas as pd

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = sqlite3.connect('jobs.db')
    return conn

def create_job(title, company, pay_range, link, industry, level, application_date, notes):
    """Create a new job entry in the jobs table."""
    conn = create_connection()
    sql = '''INSERT INTO jobs(title, company, pay_range, link, industry, level, application_date, notes)
             VALUES(?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, (title, company, pay_range, link, industry, level, application_date, notes))
    conn.commit()

def get_all_jobs():
    """Query all jobs from the jobs table."""
    conn = create_connection()
    sql = 'SELECT * FROM jobs'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return pd.DataFrame(rows, columns=['id', 'title', 'company', 'pay_range', 'link', 'industry', 'level', 'application_date', 'notes'])

# Initialize the database and the jobs table
def init_db():
    conn = create_connection()
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

if __name__ == "__main__":
    init_db()
