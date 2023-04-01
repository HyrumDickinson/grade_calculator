"""
course
"""

from src.src.category import Category
from src.src.statics import compute_letter_grade, compute_quality_points


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
        self.categories = []

        # get grading categories
        print(f"first time setup for {self.longname}")
        category_sum = 0
        while category_sum != 100:
            print(f"current categories are {self.categories}")
            name_input = input("create a new grading category for this "
                               "course, input name")
            assert name_input not in self.categories
            weight_input = int(input("what percentage of the total grade does "
                                     "this category make?"))
            assert category_sum + weight_input <= 100
            assignment_input = int(input("how many assignments?"))
            drops_input = int(input("how many drops?"))
            name_input = Category(
                weight=weight_input,
                assignments=assignment_input,
                drops=drops_input
            )
            self.categories.append(name_input)
            category_sum += weight_input
            print(f'new category {name_input} created, {name_input.weight}% of the grade for {self.name}')
        print(f"category setup complete, {self.name} course grade breakdown as follows:")
        for category in self.categories:
            print(f'    {category}: {category.weight}%')

        # get initial grades
        for category in self.categories:
            while 'y' == input(f"would you like to add a grade for {category}? (input y for yes)"):
                category.add(float(input("input grade percentage")))

    @staticmethod
    def add_grade(grade: float, category: Category) -> None:
        assert None in category.assignments
        category.add(grade)

    def course_grade(self, return_type: str = "percentage") -> float | str:
        """
        get the course grade

        Args:
            return_type (str, optional): type of grade to return. Defaults to "percentage".

        Returns:
            float | str: grade in percentage or letter form
        """

        assert return_type in ("letter", "percentage")
        self.check_category_sum()
        percentage = 0
        for category in self.categories:
            percentage += category.weight * category.grade
        if return_type == "percentage":
            return percentage
        return compute_letter_grade(percentage)

    def quality_points(self) -> float:
        return compute_quality_points(self.course_grade("letter"), self.credit)

    def check_category_sum(self) -> None:
        """
        assert that category weights sum to 100
        """
        category_sum = 0
        for category in self.categories:
            category_sum += category.weight
        assert category_sum == 100
