import numpy as np

def calculate_marks(marks):
    return marks.sum(axis=1)

def calculate_percentage(total,no_of_subs):
    return total / no_of_subs

def calculate_grade(percentages):
    def get_grade(p):
        if p >=  90:
            return 'A'

        elif p >= 75:
            return 'B'

        elif p >= 60:
            return 'C'

        elif p >= 35:
            return 'D'

        else:
            return 'fail'

    vectorized = np.vectorize(get_grade)
    return vectorized(percentages)