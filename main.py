# Import required modules
import csv
import argparse
import sqlite3

# Read student data from a CSV file and return a list of dictionaries
def read_grades(filename):
    student_data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_data.append(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return student_data

# Calculate the average score for one student
def calculate_average(student, subjects):
    try:
        total = 0
        for subject in subjects:
            total += float(student.get(subject, 0))
        return total / len(subjects)
    except (ValueError, ZeroDivisionError) as e:
        print("Error calculating average:", e)
        return 0

# Determine if a student passed based on average score
def is_passing(avg):
    return avg >= 60

# Determine grade based on average
def get_grade(avg):
    if avg >= 85:
        return 'HD'
    elif avg >= 75:
        return 'D'
    elif avg >= 65:
        return 'C'
    elif avg >= 50:
        return 'P'
    else:
        return 'F'

# Write final results (name, average, pass/fail) to a new CSV file
def write_results(results, filename):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'Average', 'Grade', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in results:
            writer.writerow(student)

# Save results to SQLite database
def save_to_database(results, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            average REAL,
            grade TEXT,
            status TEXT
        )
    ''')

    # Insert each result
    for student in results:
        cursor.execute('''
            INSERT INTO student_results (name, average, grade, status)
            VALUES (?, ?, ?, ?)
        ''', (student['Name'], student['Average'], student['Grade'], student['Status']))

    conn.commit()
    conn.close()

# Main function to control program flow
def main():
    parser = argparse.ArgumentParser(description='Process student grades.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('output_file', help='Path to the output CSV file')
    parser.add_argument('--db', default='grades.db', help='Path to the SQLite database')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    db_file = args.db

    # Step 1: Read student data from file
    student_data = read_grades(input_file)

    if student_data:
        headers = student_data[0].keys()
        subjects = [h for h in headers if h != 'Name']
    else:
        print("No data found.")
        return

    # Step 2: Process data
    results = []
    for student in student_data:
        avg = calculate_average(student, subjects)
        grade = get_grade(avg)
        status = 'Pass' if is_passing(avg) else 'Fail'

        results.append({
            'Name': student.get('Name'),
            'Average': round(avg, 2),
            'Grade': grade,
            'Status': status
        })

    # Step 3: Write to CSV
    write_results(results, output_file)
    print("Results saved to", output_file)

    # Step 4: Save to database
    save_to_database(results, db_file)
    print("Results saved to database:", db_file)

# Run main
if __name__ == '__main__':
    main()
