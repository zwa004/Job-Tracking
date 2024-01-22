import streamlit as st
import pandas as pd
from database import create_job, get_all_jobs, delete_job, delete_all_jobs

def main():
    st.title("Job Hunt Tracker")

    with st.form("Job Input Form", clear_on_submit=True):
        company = st.text_input("Company", value="")
        title = st.text_input("Job Title", value="")
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

            # Display each job
            for job in jobs.itertuples():
                st.markdown(f"**Company:** {job.company}")
                st.markdown(f"**Title:** {job.title}")
                st.markdown(f"**Pay Range:** {job.pay_range}")
                st.markdown(f"**Notes:** {job.notes}")
                st.markdown(f"**Link:** [Here]({job.link})")
        else:
            st.write("No jobs to display.")

if __name__ == "__main__":
    main()
