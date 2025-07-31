# Student Grade Tracker

This is a Python program that reads student grades from a CSV file, calculates their average score, determines pass/fail status and letter grade (HD, D, C, P, F), saves the results to a new CSV file, and stores them in a SQLite database.

## Features

- Reads student data from a CSV file
- Dynamically detects subject columns (no hardcoding needed)
- Calculates the average of all subject scores
- Determines:
  - **Pass or Fail** (pass mark: 60)
  - **Grade** based on UOW scale:
    - HD: 85–100
    - D: 75–84
    - C: 65–74
    - P: 50–64
    - F: 0–49
- Saves results to:
  - A new CSV file with name, average, grade, and pass/fail status
  - A SQLite database for structured storage and future querying
- Command-line interface (CLI) using `argparse`

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

   You can change `grades.csv` or `results.csv` to your own file names.

3. **Check the results**  
   A new file (e.g. `results.csv`) will be created with:

   ```csv
   Name,Average,Grade,Status
   Alice,88.33,HD,Pass
   Bob,57.67,P,Pass
   Charlie,80.0,D,Pass
   ```

4. **Database Storage**  
   A database file named `grades.db` will also be created in the same folder.

   It contains a table `grades` with all student results stored.
   <img width="2442" height="1566" alt="image" src="https://github.com/user-attachments/assets/519b14f1-b10e-4d92-904c-4a9865e32286" />


## Requirements

- Python 3.x  
- Uses only built-in libraries:
  - `csv`
  - `argparse`
  - `sqlite3`

## License

This project is open-source and free to use for learning purposes.
