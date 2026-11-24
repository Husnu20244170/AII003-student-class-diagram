from student import Course, Student


def main():
    # Fictional student details are used in this demonstration.
    student = Student("S001", "Example Student", "Information Systems Engineering")
    student.enroll(Course("AII003", "Software Engineering", 3))
    student.enroll(Course("AII302", "Operating Systems", 3))
    student.display_info()
    print("\nAfter dropping AII302:")
    student.drop("AII302")
    student.display_info()


if __name__ == "__main__":
    main()
