import streamlit as st
from utils.helpers import load_css, display_header, get_mongo_client


def main():
    load_css("styles.css")
    display_header()

    st.markdown("---")
    st.header("Doctor's Dashboard")

    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        if st.session_state["role"] == "doctor":
            st.write(
                "Welcome, Doctor! Use the search bar below to view a patient's symptoms."
            )

            with st.form("search_form"):
                username = st.text_input("Enter the patient's username:")
                submit = st.form_submit_button("Search")

            if submit:
                if username.strip() == "":
                    st.error("Please enter a username to search.")
                else:
                    client = get_mongo_client()
                    if client:
                        db = client["myDatabase"]
                        symptoms_collection = db["symptoms"]

                        symptoms = list(
                            symptoms_collection.find({"username": username})
                        )

                        if symptoms:
                            st.success(
                                f"Found {len(symptoms)} symptoms for user: {username}"
                            )
                            for i, symptom in enumerate(symptoms, start=1):
                                st.markdown(f"### Symptom #{i}")
                                st.write(f"**Submitted At:** {symptom['submitted_at']}")
                                st.write(f"**Symptoms:** {symptom['symptoms_text']}")
                                st.markdown("---")
                        else:
                            st.warning(
                                f"No symptoms found for the username: {username}"
                            )
                    else:
                        st.error(
                            "Failed to connect to the database. Please try again later."
                        )
        else:
            st.error("Access Denied: You do not have permission to view this page.")
    else:
        st.warning("Please log in to access the Doctor's Dashboard.")


if __name__ == "__main__":
    main()
