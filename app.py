import streamlit as st
import pandas as pd

def extract_pacient_from_excel(excel_file):
    """Extracts pacient information from the provided Excel file."""
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []

    df['DOCUMENT'] = df['DOCUMENT'].astype(str)
    df['FULL_NAME'] = df['NAMES'] + ' ' + df['LAST_NAMES']
    
    
    df = df[['DOCUMENT', 'FULL_NAME', 'PHONE', 'EPS']]

    st.write(df)

st.title("UPLOAD THE PATIENT LIST EXCEL FILE")

uploaded_file = st.file_uploader("Patient list Excel file", type=["xls", "xlsx"])
if uploaded_file is not None:
    extract_pacient_from_excel(uploaded_file)
    st.write("File has been uploaded successfully")