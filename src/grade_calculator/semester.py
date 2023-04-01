from course import Course

class Semester:
    """
    semester
    """

    def __init__(self, name: str):

        self.name = name
        self.courses = []

        print(f"first time setup for {self.name}")
        while 'y' == input(f"would you like to add a course to {self.name}? (input y for yes)"):

            course_code_input = input("what's the course code?")
            assert course_code_input not in self.courses
            description_input = input("what's the course description?")
            credit_input = int(input("how many credits is this course worth?"))
            new_course = Course(
                course_code=course_code_input,
                description=description_input,
                credit=credit_input
            )
            self.courses.append(new_course)

        print(f"semester setup complete, {self.name} course breakdown as follows:")
        for course in self.courses:
            print(f'    {course}: {course.credit} cr')

    def quality_points(self) -> float:
        quality_points = 0
        for course in self.courses:
            quality_points += course.quality_points()
        return quality_points

    def credits(self) -> int:
        credit_hours = 0
        for course in self.courses:
            credit_hours += course.credit
        return credit_hours

    def gpa(self) -> float:
        return self.quality_points() / self.credits()
