# AUTOMATED-REPORT-GENERATION

COMPANY: CODETECH IT SOLUTIONS

NAME: TANVI BEJADI

INTERN ID: CT04DH2184

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

Project Description: Automated Report Generation
This project focuses on the development of an automated system for reading, analyzing, and reporting data using Python programming. The task was designed to showcase how routine data handling and report preparation can be automated through scripting, reducing manual work and improving efficiency. The final deliverables include a Python script, a sample input dataset in CSV format, and a professionally formatted PDF report generated from the analyzed data.

Platform and Tools Used:
The script was written and tested using Python, which is known for its readability and broad range of libraries suited for data manipulation, file handling, and automation. The development work was carried out using Visual Studio Code (VS Code), a versatile and widely adopted code editor that offers powerful features such as syntax highlighting, debugging support, and terminal integration. Alternatively, other editors such as Sublime Text, Notepad++, or Python’s built-in IDLE could also be used effectively for this type of task.

To run the script, the Windows Command Prompt was used as the terminal interface. Users can navigate to the project directory using the cd command and execute the script using Python’s interpreter. The pip package manager was utilized to install external libraries. Specifically, the fpdf library was installed to enable PDF generation with the command pip install fpdf.

The following Python modules were used in the project:

csv: A built-in module used for reading and parsing CSV files.

statistics: Used to compute statistical measures such as average, minimum, and maximum scores.

fpdf: A third-party module that allows the creation of PDF files with custom headers, footers, fonts, and tables.

Functionality and Workflow:
The script begins by reading data from a CSV file named data.csv, which contains a list of names and their corresponding numerical scores. The data is parsed using the csv.DictReader function, which converts each row into a dictionary for easier access. After reading the data, the script calculates basic summary statistics including the total number of entries, average score, highest score, and lowest score using Python’s built-in statistics module.

Next, the script creates a custom class that inherits from FPDF. This class includes a formatted header titled "AUTOMATED REPORT GENERATION," a footer with dynamic page numbers, and two core methods: one for writing the statistical summary and another for presenting the data in tabular form. The PDF report is generated and saved as report.pdf in the same folder as the script and input file.

Applications and Relevance:
This automated reporting system has multiple practical applications across various sectors. In educational settings, it can be used to generate student performance reports, attendance summaries, or examination results. In business environments, it is applicable for sales reporting, employee evaluations, and financial summaries. Healthcare institutions can adapt it for patient summaries or lab reports. Government agencies and non-governmental organizations may use it to compile survey results or demographic data.

By automating the generation of structured PDF reports from raw data, this solution increases productivity, reduces manual errors, and ensures consistency in formatting. It can easily be scaled or modified to integrate with databases, web APIs, or scheduling systems for more complex requirements.

Conclusion:
In summary, this project demonstrates the practical use of Python scripting for automating everyday reporting tasks. The tools and techniques used are widely available and beginner-friendly, making this a valuable skill for students, analysts, and professionals across disciplines. With slight customization, the script can serve as a foundational component in larger reporting systems or dashboards.
