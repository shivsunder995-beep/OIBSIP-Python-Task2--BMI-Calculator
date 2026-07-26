Advanced BMI Calculator

Project Title

Advanced BMI Calculator using Python, Tkinter, SQLite, and Matplotlib

Objective

The objective of this project is to develop a graphical Body Mass Index (BMI) Calculator that allows multiple users to calculate their BMI, save their records, and visualize BMI trends over time. The application provides a user-friendly interface, stores historical data in an SQLite database, and displays BMI trends using line charts.

Technologies Used

- Programming Language: Python
- GUI Framework: Tkinter
- Database: SQLite (sqlite3)
- Graph Library: Matplotlib
- IDE: VS Code / PyCharm / IDLE

Features

- User-friendly GUI built with Tkinter.
- Input fields for user name, weight (kg), and height (m).
- BMI calculation using the standard formula:
  BMI = Weight (kg) / Height² (m²)
- BMI classification:
  - Underweight (BMI < 18.5)
  - Normal (18.5–24.9)
  - Overweight (25–29.9)
  - Obese (BMI ≥ 30)
- Colour-coded BMI results for better visualization.
- Multi-user support by storing records with user names.
- Automatic storage of BMI records in an SQLite database.
- Historical BMI trend visualization using Matplotlib.
- Input validation for invalid or negative values.
- Database error handling with appropriate error messages.

Software Requirements

- Python 3.x
- Tkinter (included with Python)
- SQLite3 (included with Python)
- Matplotlib

Install Matplotlib using:

pip install matplotlib

Project Structure

BMI_Calculator/

├── main.py

├── database.py

├── bmi.db (created automatically)

└── README.md

Working of the Project

1. The user enters their name, weight, and height.
2. The application validates the input values.
3. BMI is calculated using the BMI formula.
4. The BMI category is determined.
5. The result is displayed with a colour indicating the health category.
6. The record is saved in the SQLite database.
7. Users can view their previous BMI records as a line graph.

Database Structure

Table Name: bmi_records

Column| Data Type
id| INTEGER (Primary Key)
name| TEXT
weight| REAL
height| REAL
bmi| REAL
category| TEXT
date| TIMESTAMP

Advantages

- Easy to use graphical interface.
- Stores BMI history for multiple users.
- Helps users monitor health progress over time.
- Secure local database storage.
- Fast and lightweight application.

Future Enhancements

- Add user login and authentication.
- Export BMI reports as PDF or Excel.
- Calculate daily calorie requirements.
- Add height selection in feet/inches and centimeters.
- Display health recommendations based on BMI.
- Integrate cloud database support.

Conclusion

The Advanced BMI Calculator is an efficient desktop application that combines BMI calculation, data storage, and graphical trend analysis in a single system. It demonstrates the use of Python GUI development, SQLite database management, and data visualization, making it an excellent beginner-to-intermediate Python project.