from semester import Semester

class undergrad:

    def __init__(
        self,
        current_semester: Semester,
        past_semesters: list[Semester] = None,
    ):

        self.current_semester = current_semester
        self.past_semesters = past_semesters

    def undergraduate_quality_points(self) -> float:
        if self.past_semesters == None:
            return 0

        quality_points = 0
        for semester in self.past_semesters:
            quality_points += semester.quality_points()
        return quality_points

    def undergraduate_credits(self) -> int:
        if self.past_semesters == None:
            return 0

        credits = 0
        for semester in self.past_semesters:
            credits += semester.credits()
        return credits

    def projected_quality_points(self) -> float:
        return self.undergraduate_quality_points() + self.current_semester.quality_points()

    def projected_credits(self) -> int:
        return self.undergraduate_credits() + self.current_semester.credits()

    def undergraduate_gpa(self) -> float:
        if self.past_semesters == None:
            return None

        return self.undergraduate_quality_points() / self.undergraduate_credits()

    def projected_gpa(self) -> float:
        return (self.undergraduate_quality_points() + self.projected_quality_points()) / (self.undergraduate_credits() + self.projected_credits())
