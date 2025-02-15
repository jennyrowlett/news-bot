import streamlit as st
from datetime import date
import backend as backend  # Import the backend script


# Streamlit UI
st.title("NewsBot")
st.subheader("I am an AI bot that will search the web for the top ten news articles from a date of your choice.")
# Date input widget
date_selected = st.date_input("Date", date.today())

# Button to submit date
if st.button("Submit"):
    st.session_state["selected_date"] = date_selected
    response = backend.query_llm(date_selected)
    st.session_state["llm_response"] = response

# Display LLM response if available
if "llm_response" in st.session_state:
    st.write(f"Answer: {st.session_state['llm_response']}")