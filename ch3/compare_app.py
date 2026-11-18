"""Chained Comparisons"""

MIN_GRADE = 50
MAX_GRADE = 100


def is_passing(grade: int) -> bool:
    """Returns True if the grade lies between 50 and 100, otherwise is false"""
    return MIN_GRADE <= grade <= MAX_GRADE  # grade >= MIN_GRADE and grade <= MAX_GRADE


def main() -> None:
    """Reads the grading of a user and checks if he is passing"""
    for grade in (80, 90, 40, 30):
        is_grade_passing = is_passing(grade)
        print(f"The grading {grade} is successful: {is_grade_passing}")

    print()


if __name__ == "__main__":
    main()