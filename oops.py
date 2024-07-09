# Initialising dictionary to store student grades
student_grades = {}

# Function to add a new student
def add_student(name, grade):
    student_grades[name] = grade  # Add student name and grade to the dictionary
    print(f"Added {name} with a {grade}")  # Print confirmation message

# Function to update a student's grade
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade  # Update student's grade if student exists
        print(f"{name}'s marks are updated to {grade}")  # Print confirmation message
    else:
        print(f'{name} is not found!')  # Print message if student is not found

# Function to delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]  # Delete student from dictionary if student exists
        print(f'{name} has been successfully deleted')  # Print deletion confirmation message
    else:
        print(f'{name} not found')  # Print message if student is not found

# Function to display all students and their grades
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f'{name}: {grade}')  # Print each student and their grade
    else:
        print("No student found/added")  # Print message if no students are found

# Main function to run the program
def main():
    while True:
        print('\nStudent Grades Management System')
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View all students")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))  # Get user choice as integer
        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)  # Call add_student function
        elif choice == 2:  
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            update_student(name, grade)  # Call update_student function
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)  # Call delete_student function
        elif choice == 4:
            display_all_students()  # Call display_all_students function
        elif choice == 5:
            print("Closing the program")
            break  # Exit loop and end program
        else:
            print("Invalid choice")  # Print message for invalid choice

# Call the main function to start the program
main()
