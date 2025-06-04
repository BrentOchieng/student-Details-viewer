# student-Details-viewer
This is a  simple Python tool that allows one to retrieve student academic details based on their ID from an Excel spreadsheet.
## Features
- Loads student records from an online Excel file (Google Sheets export).
- Prompts the user to input a student ID.
- Displays student details like:
  - Name
  - Marks in Math, Physics, and Chemistry
  - Overall Percentage
- Handles missing or invalid ID input gracefully.

## Requirements
- Python 3.x
- pandas
- openpyxl (used implicitly by `pandas.read_excel` for `.xlsx` files)
