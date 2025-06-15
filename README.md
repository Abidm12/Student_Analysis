## Student Analysis
This Python-based tool helps analyze student marks from a CSV file. It computes total marks, percentages, grades,
identifies toppers, and ranks students. The project is modularized into three components: data loading (loader.py),
calculations (calculate.py), and analysis/reporting (analysis.py).

------------------------

## Project Structure
Student_Analysis/
- loader.py # Loads student data from CSV
- calculate.py # Calculates totals, percentages, grades
- analysis.py # Analyzes and generates reports
- README.md # Project documentation

------------------------

## How It Works

1. Data Loading (loader.py)

- Function: load_data(filename)
- Parameters:
 filename (str): Path to the CSV file.
- Returns:
 names (np.ndarray), marks (np.ndarray), no_of_subs (int), subjects (list)
- Description:
 Reads the file, extracts student names, subject titles, and marks.


2. Calculations (calculate.py)

- Function: calculate_marks(marks)
 - Parameters: marks (np.ndarray): 2D array of marks.
 - Returns: Total marks (1D array) per student.
- Function: calculate_percentage(total, no_of_subs)
 - Parameters: total (np.ndarray), no_of_subs (int)
 - Returns: Percentage (1D array) per student.
- Function: calculate_grade(percentages)
 - Parameters: percentages (np.ndarray)
 - Returns: Grade (1D array) per student.
- Grading Criteria:
 - A: 90% and above
 - B: 75%-89%
 - C: 60%74%
 - D: 35%-59%
 - Fail: Below 35%


3. Analysis and Reporting (analysis.py)

- Function: overall_topper(percentage)
 - Returns: Index of student with highest percentage.
- Function: subject_topper(marks)
 - Returns: List of indices representing top scorers in each subject.
- Function: report(names, total, percentage, grade, index=None)
 - Description:
 - If index is None, prints a report for all students.
 - If index is valid, prints report of that student only.
 - Otherwise, prints "Invalid index".
- Function: rank_students(names, percentage, n)
 - Parameters: n (int): Number of top students to display.
 - Returns: List of top n students with rank, name, and percentage.

 ------------------------

## Sample Input Format (data.csv)

Name,Math,Science,English
Alice,85,78,92
Bob,88,90,76
Charlie,90,95,93

------------------------

## Limitations

- The CSV file must include a header row with subject names.
- Each student record must have complete marks; no missing or blank values are allowed.
- Marks must be valid integers; non-numeric values will cause errors.
- No error handling for invalid CSV formats, duplicate names, or extra columns.
- Currently built for small/medium datasets. Optimization may be needed for large-scale data.

------------------------

## Usage Instructions

1. Place your data.csv file in the same directory as the scripts.
2. Run the scripts interactively or through a main script:
 from loader import load_data
 from calculate import calculate_marks, calculate_percentage, calculate_grade
 from analysis import overall_topper, subject_topper, report, rank_students
 names, marks, no_of_subs, subjects = load_data('data.csv')
 total = calculate_marks(marks)
 percentage = calculate_percentage(total, no_of_subs)
 grade = calculate_grade(percentage)
 report(names, total, percentage, grade)

 ------------------------

 ##  MIT License

Copyright (c) 2025 Abid Maner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is          
furnished to do so, subject to the following conditions:                        

The above copyright notice and this permission notice shall be included in     
all copies or substantial portions of the Software.                             

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.

