# Student Grade Tracker

This is a Python program that reads student grades from a CSV file, calculates their average score, determines pass/fail status and letter grade (HD, D, C, P, F), and writes the results to a new CSV file.

## Features

- Reads student data from a CSV file
- Calculates the average of all subject scores (e.g. Programming, Databases, Systems Analysis)
- Determines:
  - **Pass or Fail** (pass mark: 60)
  - **Grade** based on UOW scale:
    - HD: 85–100
    - D: 75–84
    - C: 65–74
    - P: 50–64
    - F: 0–49
- Saves results to a new CSV file with name, average, grade, and pass/fail status

## How to Use

1. **Prepare your input file**  
   Create a CSV file (e.g. `grades.csv`) with the following format:

   ```csv
   Name,CSIT110,CSIT114,CSIT115
   Alice,92,85,88
   Bob,60,58,55
   Charlie,78,82,80
   ```

   These are example subjects:
   - **CSIT110**: Fundamental Programming
   - **CSIT114**: System Analysis
   - **CSIT115**: Database Management Systems

2. **Run the program**  
   Make sure your input file is in the same folder as your Python script.

   Run the program using the terminal:

   ```bash
   python main.py grades.csv results.csv
   ```
(You can choose the names of the output file as you wish).

3. **Check the results**  
   A new file (e.g. `results.csv`) will be created with the following format:

   ```csv
   Name,Average,Grade,Status
   Alice,88.33,HD,Pass
   Bob,57.67,P,Pass
   Charlie,80.0,D,Pass
   ```

## Requirements

- Python 3.x  
- No external libraries needed (uses only built-in `csv` and `argparse`)

## License

This project is open-source and free to use for learning purposes.
