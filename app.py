import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if connection.is_connected():
            st.write("Connected to database")
        return connection
    except Error as e:
        st.write(f"Error connecting to database: {e}")
        return None

def extract_from_excel_1(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return pd.DataFrame()

    df['DOCUMENT'] = df['DOCUMENT'].astype(str)
    df['FULL_NAME'] = df['NAME'] + ' ' + df['LAST_NAME']
    df['PHONE'] = df['PHONE'].astype(str)
    
    df = df[['DOCUMENT', 'FULL_NAME', 'PHONE', 'EPS', 'MEDICAL_SPECIALTY']]

    st.write(df)
    return df

def extract_from_excel_2(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return pd.DataFrame()

    df['SPECIALTY_NAME'] = df['NAME'] + ' ' + df['LAST_NAME']
    df['SPECIALTY_PHONE'] = df['PHONE_1'].astype(str) + ', ' + df['PHONE_2'].astype(str)
    df['MEDICAL_SPECIALTY'] = df['MEDICAL_SPECIALTY']

    df = df[['SPECIALTY_NAME', 'SPECIALTY_PHONE', 'MEDICAL_SPECIALTY']]

    st.write(df)
    return df

def insert_data_to_db(df):
    
    df = df.fillna('')  

    connection = create_db_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    for index, row in df.iterrows():
        try:
            cursor.execute(
                """
                INSERT INTO combined_table (DOCUMENT, FULL_NAME, PHONE, 
                EPS, MEDICAL_SPECIALTY, SPECIALTY_NAME, SPECIALTY_PHONE)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row['DOCUMENT'], row['FULL_NAME'], row['PHONE'], 
                    row['EPS'], row['MEDICAL_SPECIALTY'], row['SPECIALTY_NAME'], 
                    row['SPECIALTY_PHONE']
                )
            )
        except Error as e:
            st.write(f"Error inserting data: {e}")
            connection.rollback()

    connection.commit()
    st.write("Data inserted successfully into the database.")
    cursor.close()
    connection.close()

st.title("UPLOAD THE EXCEL FILES")

uploaded_file_1 = st.file_uploader("Patient list Excel file", type=["xls", "xlsx"])
uploaded_file_2 = st.file_uploader("Specialties list Excel file", type=["xls", "xlsx"])

if uploaded_file_1 is not None and uploaded_file_2 is not None:
    df1 = extract_from_excel_1(uploaded_file_1)
    df2 = extract_from_excel_2(uploaded_file_2)

    st.write("Files have been uploaded successfully")

    if not df1.empty and not df2.empty:
        combined_df = pd.merge(df1, df2, on='MEDICAL_SPECIALTY', how='left')
        st.write("Combined Data:")
        st.write(combined_df)

        if st.button('Insert Data into Database'):
            insert_data_to_db(combined_df)

    else:
        st.write("One of the files could not be processed.")