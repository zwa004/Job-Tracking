import streamlit as st
import pandas as pd
from database import create_job, get_all_jobs, delete_job, delete_all_jobs, get_uniuqe_companies, get_unique_titles

def main():
    st.title("Job Hunt Tracker")

    companies = get_uniuqe_companies()
    titles = get_unique_titles()

    with st.form("Job Input Form", clear_on_submit=True):
        company = st.selectbox("Company", [''] + companies)
        title = st.selectbox("Title", [''] + titles)
        pay_range = st.text_input("Pay Range", value="")
        link = st.text_input("Job Link", value="")
        notes = st.text_area("Notes", value="")

        submitted = st.form_submit_button("Add Job")

        if submitted:
            create_job(company, title, pay_range, notes, link)
            st.success("Job added successfully!")

    # Expander for showing/hiding jobs
    with st.expander("Show/Hide Jobs"):
        jobs = get_all_jobs()
        if not jobs.empty:
            job_to_delete = st.selectbox("Select a job to delete", jobs['id'].tolist())

            if st.button(f"Delete Job #{job_to_delete}"):
                delete_job(job_to_delete)
                st.success(f"Job #{job_to_delete} deleted successfully!")
                jobs = get_all_jobs()  # Refresh the list of jobs

            if st.button("Delete All Jobs"):
                delete_all_jobs()
                st.success("All jobs deleted successfully!")
                jobs = get_all_jobs()  # Refresh the list of jobs

            # In your main function, replace the for loop with this function call
            if not jobs.empty:
                display_jobs_with_links(jobs)
        else:
            st.write("No jobs to display.")
        
def display_jobs_with_links(jobs):
    jobs['link'] = jobs['link'].apply(lambda x: f'<a href="{x}" target="_blank">Link</a>' if x else '')
    st.write(jobs.to_html(escape=False, index=False), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
