Overview
This is a simple Streamlit application that allows users to upload a SQLite database file (.db) and view its tables and contents interactively. The app displays all available tables in the database and lets users select any table to view its data in a clean, scrollable DataFrame format.

Features
Upload any SQLite database file (.db extension)

Automatic detection of all tables in the database

Interactive table selection dropdown

Clean display of table contents using Pandas DataFrame

Responsive interface that works on desktop and mobile

Installation & Usage
Prerequisites:

Python 3.7+

pip package manager

Install dependencies:

bash
pip install streamlit sqlite3 pandas
Run the application:

bash
streamlit run sqlite_viewer.py
Using the app:

Click "Browse files" to upload your SQLite database file (.db)

Select a table from the dropdown menu

View the table contents in the interactive DataFrame display

File Structure
sqlite-viewer/
├── sqlite_viewer.py      # Main application code
├── README.md             # This documentation file
└── requirements.txt      # Python dependencies (optional)
Requirements
List of Python packages required (already included in installation instructions):

streamlit

sqlite3 (built into Python)

pandas

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

