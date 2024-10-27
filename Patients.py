import streamlit as st
from utils.helpers import (
    load_css,
    display_header,
    get_current_timestamp,
    get_mongo_client,
)
import json
import os
from datetime import datetime
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings
import av
import numpy as np


def main():
    load_css("styles.css")
    display_header()

    st.markdown("---")
    st.header("Patients Page")

    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        if st.session_state["role"] == "patient":
            st.write("""
                Welcome to the **Patients Dashboard**. You can input your symptoms below to help healthcare providers understand your condition.
            """)

            with st.form("symptom_form"):
                symptoms = st.text_area("Describe your symptoms here:", height=200)
                submit = st.form_submit_button("Submit Symptoms")

            if submit:
                if symptoms.strip() == "":
                    st.error("Please enter your symptoms before submitting.")
                else:
                    symptom_data = {
                        "username": st.session_state["username"],
                        "symptoms_text": symptoms.strip(),
                        "submitted_at": get_current_timestamp(),
                    }

                    client = get_mongo_client()
                    if client:
                        db = client["myDatabase"]
                        symptoms_collection = db["symptoms"]

                        try:
                            symptoms_collection.insert_one(symptom_data)
                            st.success(
                                "Your symptoms have been successfully submitted!"
                            )
                        except Exception as e:
                            st.error(
                                f"An error occurred while submitting your symptoms: {e}"
                            )
                    else:
                        st.error(
                            "Failed to connect to the database. Please try again later."
                        )
        else:
            st.error("Access Denied: You do not have permission to view this page.")
    else:
        st.warning("Please log in to access the Patients page.")


if __name__ == "__main__":
    main()
