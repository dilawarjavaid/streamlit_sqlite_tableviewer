import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("SQLite Table Viewer")
uploaded_file = st.file_uploader("Choose a .db file", type="db")