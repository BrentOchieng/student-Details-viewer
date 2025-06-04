#This code simplifies and automates data accesibility from a csv or excel file based on the first column.
#the code outputs the specific details of the first row in the first column upon input.
import pandas as pd

# Load the data
data_url = 'https://docs.google.com/spreadsheets/d/1AA0QkqOgeDjBK6R_IFTV_Hvw1xNwBiq2/export?format=xlsx'
df = pd.read_excel(data_url)


# Dataset columns
print("Columns in the dataset:", df.columns.tolist()) #get a list of the column names from the pd data frame provided

# Input based on the students ID
action_1 = input('Enter ID: ')

# Convert to int if needed (depends on data)
try:
    action_1 = int(action_1)
except ValueError:
    pass  # Keep as string if needed

Details = ['ID', 'Name','Marks in Math (Out of 100)', 'Marks in Physics (Out of 100)', 'Marks in Chemistry (Out of 100)', 'Percentage']# the details from the pd data frame columns

# Match the ID
if 'ID' not in df.columns:
    print("Error: 'ID' column not found.")
else:
    matching_rows = df[df['ID'] == action_1]
    if not matching_rows.empty:
        student_details = matching_rows.iloc[0][Details].tolist()
        print("Student Details:")
        for detail_name, detail_value in zip(Details, student_details):
            print(f"{detail_name}: {detail_value}")
    else:
        print('Error input: ID not found.')
