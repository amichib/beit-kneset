import streamlit as st
import pandas as pd

# Load data from CSV
CSV_PATH = "data.csv"  
try:
    df = pd.read_csv(CSV_PATH, dtype={"ID": str})  # Ensure ID is treated as string
except Exception as e:
    st.error(f"Failed to load data.csv: {e}")
    st.stop()

st.title("User ID Lookup")
user_input = st.text_input("Enter your 9-digit ID:")

# Check input
if user_input:
    if len(user_input) != 9 or not user_input.isdigit():
        st.warning("Please enter a valid 9-digit number.")
    else:
        # Look for rows where ID is a substring of user input
        matches = df[df["ID"].astype(str).apply(lambda x: x in user_input)]
        if not matches.empty:
            st.success("ID Found!")
            st.write(matches)
        else:
            st.warning("ID NOT FOUND")
