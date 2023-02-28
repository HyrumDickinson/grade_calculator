from semester import Semester

class undergrad:

    def __init__(
        self,
        current_semester: Semester,
        past_semesters: list[Semester] = None,
    ):

        assert isinstance(current_semester, Semester)
        assert past_semesters is None or all(isinstance(s, Semester) for s in past_semesters)
        
        self.current_semester = current_semester
        self.past_semesters = past_semesters

    def undergraduate_quality_points(self) -> float:
        if self.past_semesters is None:
            return 0

        return sum(semester.quality_points() for semester in self.past_semesters)

    def undergraduate_credits(self) -> int:
        if self.past_semesters is None:
            return 0

        return sum(semester.credits() for semester in self.past_semesters)

    def projected_quality_points(self) -> float:
        return self.undergraduate_quality_points() + self.current_semester.quality_points()

    def projected_credits(self) -> int:
        return self.undergraduate_credits() + self.current_semester.credits()

    def undergraduate_gpa(self) -> float:
        if self.past_semesters == None:
            return None

        return self.undergraduate_quality_points() / self.undergraduate_credits()

    def projected_gpa(self) -> float:
        total_quality_points = sum(
            [self.undergraduate_quality_points(), self.current_semester.quality_points()]
        )
        total_credits = sum(
            [self.undergraduate_credits(), self.current_semester.credits()]
        )
        return total_quality_points / total_credits
