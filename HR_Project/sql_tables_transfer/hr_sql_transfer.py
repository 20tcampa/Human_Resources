#Importing the libraries I need.
from dotenv import load_dotenv
import os
import pyodbc
import pandas as pd

#Getting the Driver and Server info from a seperate file. 
load_dotenv()

driver = os.getenv('DRIVER')
server = os.getenv('SERVER')

#Getting the dataframes that I need to put into tables and removing the Unnamed: 0 column.
department_df = pd.read_csv(r'C:\Users\Thomas Campana\VisualStudioTests\DATA_SCIENCE\HR_Project\sql_tables_transfer\department.csv')
employee_df = pd.read_csv(r'C:\Users\Thomas Campana\VisualStudioTests\DATA_SCIENCE\HR_Project\sql_tables_transfer\employee.csv')
manager_df = pd.read_csv(r'C:\Users\Thomas Campana\VisualStudioTests\DATA_SCIENCE\HR_Project\sql_tables_transfer\manager_df.csv')
marital_df = pd.read_csv(r'C:\Users\Thomas Campana\VisualStudioTests\DATA_SCIENCE\HR_Project\sql_tables_transfer\marital.csv')
position_df = pd.read_csv(r'C:\Users\Thomas Campana\VisualStudioTests\DATA_SCIENCE\HR_Project\sql_tables_transfer\position.csv')

department_df.drop('Unnamed: 0', axis=1, inplace=True)
employee_df.drop('Unnamed: 0', axis=1, inplace=True)
manager_df.drop('Unnamed: 0', axis=1, inplace=True)
marital_df.drop('Unnamed: 0', axis=1, inplace=True)
position_df.drop('Unnamed: 0', axis=1, inplace=True)

#Establishing the connection to the SQL server.
conn = pyodbc.connect(
    Trusted_Connection = 'Yes',
    Driver = driver,
    Server = server,
    Database = 'HR_Project'
)

#Creating the Tables that I need for this data.
cursor = conn.cursor()

cursor.execute("""CREATE TABLE department (
               DeptID int PRIMARY KEY, 
               Department varchar(250)
               )""")

cursor.execute("""CREATE TABLE managers (
               ManagerID int PRIMARY KEY, 
               ManagerName varchar(250)
               )""")

cursor.execute("""CREATE TABLE marital_status (
               MaritalStatusID int PRIMARY KEY, 
               MaritalDesc varchar(250)
               )""")

cursor.execute("""CREATE TABLE positions (
               PositionID int PRIMARY KEY, 
               Position varchar(250)
               )""")

cursor.execute("""CREATE TABLE employees (
               EmpID int PRIMARY KEY, 
               Employee_Name varchar(250), 
               MaritalStatusID int FOREIGN KEY REFERENCES marital_status(MaritalStatusID), 
               Sex varchar(10),
               EmploymentStatus varchar(250),
               DeptID int FOREIGN KEY REFERENCES department(DeptID),
               FromDiversityJobFairID int,
               Salary int,
               PositionID int FOREIGN KEY REFERENCES positions(PositionID),
               State varchar(5),
               Zip int,
               DOB date,
               CitizenDesc varchar(250),
               HispanicLatino varchar(100),
               RaceDesc varchar(250),
               DateofHire date,
               DateofTermination date,
               TermReason varchar(250),
               ManagerID int FOREIGN KEY REFERENCES managers(ManagerID),
               RecruitmentSource varchar(250),
               PerformanceScore varchar(250),
               EngagementSurvey float,
               EmpSatisfaction int,
               SpecialProjectsCount int,
               LastPerformanceReview_Date date,
               DaysLateLast30 int,
               Absences int
               )""")

#Created loops to input all the data from the pandas dataframe to their respective SQL server tables.
for i in department_df.itertuples():
    cursor.execute("""
                INSERT INTO HR_Project.dbo.department (DeptID, Department)
                VALUES (?, ?)
                """, i.DeptID, i.Department)
    
for i in manager_df.itertuples():
    cursor.execute("""
                INSERT INTO HR_Project.dbo.managers (ManagerID, ManagerName)
                VALUES (?, ?)
                """, i.ManagerID, i.ManagerName)
    
for i in marital_df.itertuples():
    cursor.execute("""
                INSERT INTO HR_Project.dbo.marital_status (MaritalStatusID, MaritalDesc)
                VALUES (?, ?)
                """, i.MaritalStatusID, i.MaritalDesc)
    
for i in position_df.itertuples():
    cursor.execute("""
                INSERT INTO HR_Project.dbo.positions (PositionID, Position)
                VALUES (?, ?)
                """, i.PositionID, i.Position)

for i in employee_df.itertuples():
    cursor.execute("""
                INSERT INTO HR_Project.dbo.employees (EmpID, Employee_Name, MaritalStatusID, Sex, EmploymentStatus, DeptID, FromDiversityJobFairID, Salary, PositionID, State, Zip, DOB, CitizenDesc, HispanicLatino, RaceDesc, DateofHire, ManagerID, RecruitmentSource, PerformanceScore, EngagementSurvey, EmpSatisfaction, SpecialProjectsCount, LastPerformanceReview_Date, DaysLateLast30, Absences)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, i.EmpID, i.Employee_Name, i.MaritalStatusID, i.Sex, i.EmploymentStatus, i.DeptID, i.FromDiversityJobFairID, i.Salary, i.PositionID, i.State, i.Zip, i.DOB, i.CitizenDesc, i.HispanicLatino, i.RaceDesc, i.DateofHire, i.ManagerID, i.RecruitmentSource, i.PerformanceScore, i.EngagementSurvey, i.EmpSatisfaction, i.SpecialProjectsCount, i.LastPerformanceReview_Date, i.DaysLateLast30, i.Absences)

conn.commit()