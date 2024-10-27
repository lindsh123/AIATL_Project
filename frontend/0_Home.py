# app.py

import streamlit as st
from utils.helpers import load_css, display_header


def main():
    load_css("styles.css")
    display_header()

    st.markdown("---")
    st.write("""
        To get started, register for an account using the Register tab on the left side. 
    """)

    # Add an overview or features
    st.subheader("Features")
    features = [
        "User-friendly interface for patients and doctors.",
        "Symptom input for patients via text or speech.",
        "Potential diagnoses and the doctor that should be notified.",
        "Alerts sent to the doctors. ",
    ]

    for feature in features:
        st.markdown(f"- {feature}")


if __name__ == "__main__":
    main()
