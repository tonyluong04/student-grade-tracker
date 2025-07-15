# Student Grade Tracker

This is a simple Python program that reads student grades from a CSV file, calculates average scores, determines pass/fail status, and saves the results to a new CSV file.

## Features

- Reads data from `grades.csv`
- Calculates average of Math, Science, and English scores
- Determines if the student passed (average >= 60)
- Outputs result to `results.csv` with Name, Average, and Status

## How to Use

1. **Prepare your input file**  
   Create a file named `grades.csv` with the following format:

Name,Math,Science,English
Alice,85,90,80
Bob,50,60,55
Charlie,78,82,88

2. **Run the program**

Make sure you have Python installed. Then run:

python main.py


3. **Check the output**

A file named `results.csv` will be created with the following format:

Name,Average,Status
Alice,85.0,Pass
Bob,55.0,Fail
Charlie,82.67,Pass


## Requirements

- Python 3.x
- No external libraries needed (uses built-in `csv` module)

## Notes

- You can modify the input and run again to test different results.
- This is a basic project ideal for Python beginners or as a small portfolio piece.

