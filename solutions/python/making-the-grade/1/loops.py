"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list) -> list:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    rounded_list = []
    for score in student_scores:
        rounded_list.append(round(score))

    return rounded_list


def count_failed_students(student_scores: list) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    counter = 0

    for score in student_scores:
        if score <= 40:
            counter += 1

    return counter

    


def above_threshold(student_scores: list, threshold: int) -> list:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_list = []
    for score in student_scores:
        if score >= threshold:
            best_list.append(score)

    return best_list

def letter_grades(highest: int) -> list:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    starting_score = 41
    final_list = []
    for score in range(4):
        final_list.append(starting_score)
        starting_score += (highest-40)//4

    return final_list      



def student_ranking(student_scores: list, student_names: list) -> list:
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    rank_list = []
    for index, score in enumerate(student_scores):
        rank_list.append(f"{index+1}. {student_names[index]}: {score}")

    return rank_list


def perfect_score(student_info: list) -> list:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for value in student_info:
        if value[-1] == 100:
            return value    
    return []
