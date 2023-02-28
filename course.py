'''
course
'''

from src.category import Catagory
from src.statics import compute_letter_grade, compute_quality_points


class Course:

    def __init__(
        self,
        course_code: str,
        description: str,
        credit: int
    ):
        self.name = course_code
        self.longname = f'{course_code}: {description}'
        self.credit = credit
        self.catagories = []

        # get grading catagories
        print(f"first time setup for {self.longname}")
        catagory_sum = 0
        while catagory_sum != 100:
            print(f"current catagories are {self.catagories}")
            name_input = input("create a new grading catagory for this course, input name")
            assert name_input not in self.catagories
            weight_input = input("what percentage of the total grade does this catagory make?")
            assert catagory_sum + weight_input <= 100
            assignment_input = input("how many assignments?")
            drops_input = input("how many drops?")
            name_input = Catagory(
                weight=weight_input,
                assignments=assignment_input,
                drops=drops_input
            )
            self.catagories.append(name_input)
            catagory_sum += weight_input
            print(f'new catagory {name_input} created, {name_input.weight}% of the grade for {self.name}')
        print(f"catagory setup complete, {self.name} course grade breakdown as follows:")
        for catagory in self.catagories:
            print(f'    {catagory}: {catagory.weight}%')

        # get initial grades
        for catagory in self.catagories:
            while 'y' == input(f"would you like to add a grade for {catagory}? (input y for yes)"):
                catagory.add(input("input grade percentage"))

    def add_grade(self, grade: float, catagory: Catagory) -> None:
        assert None in catagory.assignments
        catagory.add(grade)

    def course_grade(self, return_type: str = "percentage") -> float | str:
        '''
        get the course grade

        Args:
            return_type (str, optional): type of grade to return. Defaults to "percentage".

        Returns:
            float | str: grade in percentage or letter form
        '''

        assert return_type in ("letter", "percentage")
        self.check_catagory_sum()
        percentage = 0
        for catagory in self.catagories:
            percentage += catagory.weight * catagory.grade
        if return_type == "percentage":
            return catagory
        return compute_letter_grade(percentage)

    def quality_points(self) -> float:
        return compute_quality_points(self.course_grade("letter"), self.credit)

    def check_catagory_sum(self) -> None:
        '''
        assert that catagory weights sum to 100
        '''
        catagory_sum = 0
        for catagory in self.catagories:
            sum += catagory.weight
        assert catagory_sum == 100
