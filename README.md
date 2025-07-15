# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: TANVI BEJADI

INTERN ID: CT04DH2184

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

Description of the Task:
This project is about making a simple Python program that reads data from a file, understands it, and creates a neat PDF report from it. The idea is to save time and effort when we have a list of information—like students' marks, sales numbers, or employee records—and we want to make it look good in a printed or digital report.

Instead of doing this by hand, the Python program does all the steps automatically. This kind of task is useful in schools, offices, hospitals, and businesses where reports are created often.

Tools and Platform Used:
This project was done using:

Python programming language – It is easy to understand and very good for working with data.

Visual Studio Code (VS Code) – A text editor used to write the Python code. You can also use Notepad, Notepad++, or IDLE.

Command Prompt – To run the Python file on a Windows computer.

Libraries Used:

csv – A built-in module that helps in reading .csv files (comma-separated values).

statistics – A built-in module to calculate things like average, highest, and lowest values.

fpdf – A Python library used to create PDF files.

Before running the program, the fpdf library must be installed using this command in Command Prompt:

nginx
Copy
Edit
pip install fpdf
Working Procedure:

Create a CSV File:
First, a data file called data.csv is created. It contains names and scores.

Write the Python Script:
A Python file named generate_report.py is written. This file does all the work:

Reads the CSV file using the csv module.

Stores the names and scores in a list.

Calculates the total number of students, the average score, and finds the highest and lowest scores using the statistics module.

Creates a formatted PDF report using the fpdf module. The report includes a title, summary section, and a table of all names and scores.

Run the Script:
Open the Command Prompt, go to the folder where the script is saved using the cd command, and then run:

nginx
Copy
Edit
python generate_report.py
After running the script, a file called report.pdf is created in the same folder.

View the Output:
The PDF file can be opened to see the clean, readable report with all the data and summary.

Applications of This Project:
This project can be used in many real-world situations, such as:

Schools and colleges: Automatically generate report cards, attendance sheets, or performance summaries.

Offices: Create monthly sales reports, employee performance summaries, or meeting summaries.

Hospitals: Generate patient history summaries, test result reports, or medicine usage reports.

Shops or businesses: Create inventory summaries or sales statistics.

Government or NGOs: Make survey reports, population statistics, or public service records.

It is very helpful in places where reports are prepared regularly and there is a need to make them look clean and professional without spending too much time.

Conclusion:
This project shows how a simple Python program can make everyday tasks easier. With just a few lines of code, we can turn plain data into a proper report. It helps reduce errors, saves time, and makes the work more professional. This skill is useful for students, teachers, office workers, and anyone who works with data regularly.

#OUTPUT

<img width="985" height="813" alt="Image" src="https://github.com/user-attachments/assets/41b8cc5c-e399-4202-80f6-da4696855048" />
