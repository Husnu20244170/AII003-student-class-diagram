class Course:
    def __init__(self, code, title, credits):
        if not isinstance(credits, int) or credits <= 0:
            raise ValueError("Credits must be a positive integer.")
        self.code = code
        self.title = title
        self.credits = credits

    def description(self):
        return f"{self.code} - {self.title} ({self.credits} credits)"


class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.courses = []

    def enroll(self, course):
        if any(item.code == course.code for item in self.courses):
            raise ValueError("Already enrolled in this course.")
        self.courses.append(course)

    def drop(self, course_code):
        for course in self.courses:
            if course.code == course_code:
                self.courses.remove(course)
                return
        raise ValueError("Not enrolled in this course.")

    def total_credits(self):
        return sum(course.credits for course in self.courses)

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")
        print("Courses:")
        for course in self.courses:
            print(f"  {course.description()}")
        print(f"Total credits: {self.total_credits()}")
