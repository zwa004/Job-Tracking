import sqlite3
import pandas as pd

def create_connection():
    conn = sqlite3.connect('jobs.db')
    return conn

def create_job(company, title, pay_range, notes, link):
    conn = create_connection()
    sql = ''' INSERT INTO jobs(company,title,pay_range,notes,link)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (company, title, pay_range, notes, link))
    conn.commit()
    return cur.lastrowid

def get_all_jobs():
    conn = create_connection()
    jobs = pd.read_sql_query("SELECT * FROM jobs", conn)
    return jobs

def delete_job(job_id):
    try:
        conn = create_connection()
        sql = 'DELETE FROM jobs WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (job_id,))
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_all_jobs():
    try:
        conn = create_connection()
        sql = 'DELETE FROM jobs'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")


# Initialize DB and table
conn = create_connection()
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS jobs (
                    id integer PRIMARY KEY,
                    company text NOT NULL,
                    title text,
                    pay_range text,
                    notes text,
                    link text
                ); ''')
conn.commit()
