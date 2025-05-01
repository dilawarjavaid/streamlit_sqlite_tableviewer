import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("SQLite Table Viewer")
uploaded_file = st.file_uploader("Choose a .db file", type="db")

if uploaded_file is not None:
    db_file_path = uploaded_file.name
    with open(db_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]


    if table_names:
        selected_table = st.selectbox("Select a table", table_names)