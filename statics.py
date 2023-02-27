'''
statics
'''


def compute_letter_grade(percentage: float) -> str:
    '''
    compute the letter grade

    Args:
        percentage (float): percentage grade

    Returns:
        str: letter grade
    '''
    if percentage >= 97:
        letter_grade = "A+"
    elif percentage >= 93:
        letter_grade = "A"
    elif percentage >= 90:
        letter_grade = "A-"
    elif percentage >= 87:
        letter_grade = "B+"
    elif percentage >= 83:
        letter_grade = "B"
    elif percentage >= 80:
        letter_grade = "B-"
    elif percentage >= 77:
        letter_grade = "C+"
    elif percentage >= 73:
        letter_grade = "C"
    elif percentage >= 70:
        letter_grade = "C-"
    elif percentage >= 67:
        letter_grade = "D+"
    elif percentage >= 63:
        letter_grade = "D"
    elif percentage >= 60:
        letter_grade = "D-"
    else:
        letter_grade = "F"
    return letter_grade

def compute_quality_points(letter_grade: str, credit: int) -> float:
    '''
    compute quality points

    Args:
        letter_grade (str): course letter grade
        credit (int): course credit hours

    Returns:
        float: quality points for course
    '''

    quality_points = {
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0
    }

    assert letter_grade in quality_points

    return quality_points[letter_grade] * credit