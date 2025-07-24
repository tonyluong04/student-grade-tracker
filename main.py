# Import required module
import csv
import argparse


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
    if avg >= 60:
        return True
    else:
        return False
    
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

# Main function to control program flow
def main():
    parser = argparse.ArgumentParser(description='Process student grades.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('output_file', help='Path to the output CSV file')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file


    # Step 1: Read student data from file
    student_data = read_grades(input_file)


    # Get subject names dynamically from first row
    if student_data:
        headers = student_data[0].keys()
        subjects = [h for h in headers if h not in ['Name']]
    else:
        print("No data found.")
        return


    # Step 2: Process each student and store results
    results = []
    for student in student_data:
        avg = calculate_average(student, subjects)
        status = 'Pass' if is_passing(avg) else 'Fail'
        grade = get_grade(avg)
        
        results.append({
            'Name': student.get('Name'),
            'Average': round(avg, 2),
            'Grade': grade,
            'Status': status
        })
    

    # Step 3: Write results to output file
    write_results(results, output_file)
    print("Done. Results saved to", output_file)

# Run main if this file is executed directly
if __name__ == '__main__':
    main()
