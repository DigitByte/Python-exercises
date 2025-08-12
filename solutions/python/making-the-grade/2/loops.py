"""Functions for organizing and calculating student exam scores."""
from typing import List


def round_scores(student_scores: List[float]) -> List[int]:
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores: List[int]) -> int:
    """Count the number of failing students out of the group provided."""
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> List[int]:
    """Create a list of grade thresholds based on the provided highest grade."""
    interval = (highest - 40) // 4
    return [41 + interval * step for step in range(4)]


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:
    """Organize the student's rank, name, and grade information in descending order."""
    return [f"{rank}. {name}: {score}" for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1)]


def perfect_score(student_info: List[List]) -> List:
    """Create a list with the name and grade of the first student to make a perfect score on the exam."""
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
