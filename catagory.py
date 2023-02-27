import warnings


# grading catagory
class Catagory:

    def __init__(
        self,
        weight: int,
        assignments: int,
        drops: int,
    ):

        # weight of this catagory in the total grade
        self.weight = weight

        # ordered list of assignments (graded and not) for this course
        self.assignments = [None] * assignments

        # list of indices in self.assignments that are dropped
        self.drops = [None] * drops

        # computed grade for this catagory
        self.grade = None

    def add(self, grade: float) -> None:
        self.update_assignments(grade)
        self.update_drops()
        self.update_grade()

    def update_assignments(self, grade: float) -> None:
        for i in self.assignments:
            if i is not None:
                i = grade
                return
        warnings.warn("added grade when all grades full")
        self.assignments.append(grade)

    def update_drops(self) -> None:
        graded_assignments = {}
        for i, val in enumerate(self.assigments):
            if val is not None:
                graded_assignments[i] = val
        if len(self.drops) >= len(graded_assignments):
            for i, grade_idx in enumerate(graded_assignments):
                self.drops[i] = grade_idx
        elif len(self.drops) < len(graded_assignments):
            for _, i in enumerate(self.drops):
                min_grade = min(graded_assignments.values())
                pop_me = None
                for j in graded_assignments:
                    if graded_assignments[j] == min_grade:
                        self.drops[i] = min_grade[j]
                        pop_me = j
                        break
                graded_assignments.pop[pop_me]
            assert None not in self.drops

    def update_grade(self) -> None:
        graded_assignments = []
        for i in self.assignments:
            if i is not None:
                graded_assignments.append(i)
        self.grade = sum(graded_assignments) / len(graded_assignments)
