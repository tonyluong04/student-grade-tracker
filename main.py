# Import required module
import csv

# Read student data from a CSV file and return a list of dictionaries
def read_grades(filename):
    student_data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data.append(row)
    return student_data

# Calculate the average score for one student
def calculate_average(student):
    math = int(student.get('Math'))
    science = int(student.get('Science'))
    english = int(student.get('English'))
    avg = (math + science + english) / 3
    return avg

# Determine if a student passed based on average score
def is_passing(avg):
    return avg >= 60  # returns True or False directly

# Write final results (name, average, pass/fail) to a new CSV file
def write_results(results, filename):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['Name', 'Average', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in results:
            writer.writerow(student)

# Main function to control program flow
def main():
    input_file = 'grades.csv'      # Input CSV file with raw scores
    output_file = 'results.csv'    # Output CSV file for processed results

    # Step 1: Read student data from file
    student_data = read_grades(input_file)

    # Step 2: Process each student and store results
    results = []
    for student in student_data:
        avg = calculate_average(student)
        status = 'Pass' if is_passing(avg) else 'Fail'
        results.append({
            'Name': student.get('Name'),
            'Average': round(avg, 2),
            'Status': status
        })

    # Step 3: Write results to output file
    write_results(results, output_file)
    print("Done. Results saved to", output_file)

# Run main if this file is executed directly
if __name__ == '__main__':
    main()
