# Student Grade Tracker

This is a simple Python program that reads student grades from a CSV file, calculates their average score, determines pass or fail status, and writes the results to a new CSV file.

## Features

- Reads student data from a CSV file
- Calculates average of Math, Science, and English scores
- Marks students as Pass or Fail (pass mark is 60)
- Saves results to a new CSV file

## How to Use

1. **Prepare your input file**  
   Create a file named `grades.csv` with the following format:

```

Name,Math,Science,English
Alice,85,90,80
Bob,50,60,55
Charlie,78,82,88

````

2. **Run the program**  
Make sure your `grades.csv` file is in the same folder as your Python script.

Then run the program:

```bash
python main.py
````

3. **Check the results**
   A new file called `results.csv` will be created with the following format:

   ```
   Name,Average,Status
   Alice,85.0,Pass
   Bob,55.0,Fail
   Charlie,82.67,Pass
   ```

## Requirements

* Python 3.x

No external packages needed (only built-in `csv` module is used).

## License

This project is open-source and free to use for learning purposes.
