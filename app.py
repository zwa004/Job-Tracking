import streamlit as st
import pandas as pd
import datetime
from database import create_job, get_all_jobs

# Define the pay range, experience level options, and sample industries
pay_ranges = [f"${x}-{x+4999}" for x in range(30000, 150000, 5000)] + ["$150,000+"]
experience_levels = ["Internship", "Entry Level", "Associate", "Mid-Level", "Senior", "Director", "Executive"]
industries = ["Technology", "Healthcare", "Finance", "Education", "Retail", "Manufacturing", "Other"]

def input_application():
    st.title("Input New Job Application")
    with st.form("Job Input Form", clear_on_submit=True):
        title = st.text_input("Job Title")
        company = st.text_input("Company")
        pay_range = st.selectbox("Pay Range", pay_ranges)
        link = st.text_input("Job Link")
        industry = st.selectbox("Industry", industries)
        level = st.selectbox("Experience Level", experience_levels)
        application_date = st.date_input("Application Date", datetime.date.today())
        notes = st.text_area("Notes")

        submitted = st.form_submit_button("Add Job")
        if submitted:
            create_job(title, company, pay_range, link, industry, level, application_date, notes)
            st.success("Job added successfully!")

def view_applications():
    st.title("Job Applications")
    jobs = get_all_jobs()
    if not jobs.empty:
        st.dataframe(jobs)
    else:
        st.write("No job applications to display.")

def main():
    st.sidebar.title("Navigation")
    if st.sidebar.button("Input Application"):
        input_application()
    if st.sidebar.button("View Applications"):
        view_applications()

if __name__ == "__main__":
    main()
