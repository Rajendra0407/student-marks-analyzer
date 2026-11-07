# Student Marks Analyzer

A beginner Python project that reads marks for multiple students,
validates the input, and prints a report with grades, the class
topper and the class average. The report is also saved to a file.

## Features
- Takes marks for 5 subjects per student
- Rejects text and marks outside 0 to 100, then asks again
- Handles empty and duplicate student names
- Calculates each student's average and grade
- Finds the class topper and the class average
- Saves the report to `report.txt`

## How to run
1. Install Python 3.
2. Clone this repository.
3. Run: `python src/marks_analyzer.py`
4. Type a student name, enter 5 marks, and type `done` to finish.

## Example
```
Student name (or type done): raj
...
Student name (or type done): done
raj: Percentage: 46.0 Grade: (C)
sam: Percentage: 47.2 Grade: (C)
Topper: sam with 47.2
Class average: 46.6
Report saved to report.txt
```

## Grading scheme
90+ A+, 75-89 A, 60-74 B, 40-59 C, 30-39 D, below 30 F

## What I learned
- Virtual environments and project structure
- Git and GitHub workflow
- Functions, dictionaries and loops
- Input validation with try/except, if and raise
- Reading user input and writing a report to a file

## Next steps
- Add automated tests
- Read students from a CSV file
