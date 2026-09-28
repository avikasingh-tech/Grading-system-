# Smart Student Performance Analyser

## 1. Overview

Smart Student Performance Analyser is a Python-based project made to analyse a student's academic performance.

The user enters the student's details, subjects, and marks. The program then calculates the total marks, average, percentage, grade, failed subjects, highest and lowest marks, and the overall result.

The main purpose of this project is to use basic Python concepts to solve a practical problem related to student performance.

## 2. Objectives

The main objectives of this project are:

- To take and store student details.
- To take marks for different subjects.
- To calculate the total marks and average.
- To calculate the student's percentage.
- To find subjects in which the student has failed.
- To find the highest and lowest marks.
- To assign a grade based on the percentage.
- To display the final Pass/Fail result.
- To apply Python concepts in a practical application.

## 3. Features

- Student details input
- Subject-wise marks input
- Total marks calculation
- Average calculation
- Percentage calculation
- Failed subject identification
- Highest and lowest marks
- Grade calculation
- Overall Pass/Fail result
- Input validation

## 4. Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub

## 5. Python Concepts Used

The project uses the following Python concepts:

- Variables and data types
- Input and output
- Dictionaries
- Lists
- Functions
- For and while loops
- Conditional statements
- Dictionary methods
- `len()`, `max()` and `min()`
- Input validation
- Modular programming

## 6. Project Structure

```text
SMART-STUDENT-PERFORMANCE-ANALYSER/
│
├── main.py
├── student.py
├── analysis.py
├── validation.py
├── README.md
└── requirements.txt
### File Description

- `main.py` – Runs the main program and displays the final results.
- `student.py` – Takes the student's details, subjects, and marks.
- `analysis.py` – Contains functions used to analyse the student's marks.
- `validation.py` – Checks whether the entered marks are valid.
- `README.md` – Contains information about the project.
- `requirements.txt` – Contains the project dependencies.
## 7. Grade Criteria

| Percentage | Grade |
|---|---|
| 90% and above | S |
| 80%–89.99% | A |
| 70%–79.99% | B |
| 60%–69.99% | C |
| 50%–59.99% | D |
| 40%–49.99% | E |
| Below 40% | F |
## 9. Validation

The project includes validation for the marks entered by the user.

The entered marks should:

- Not be less than 0.
- Not be greater than the maximum marks.

This helps prevent invalid marks from being entered into the program.
## 10. Requirements

- Python 3.x
- Visual Studio Code (recommended)
- No external Python libraries are currently required.