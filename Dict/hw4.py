
def top_students(students, num=3):
    """
    Returns a list of the top scoring students

    :param students: (dictionary) student names: grades
    :param num: (int) number of students, default = 3
    :return: (list) of top num students
    """
    top_array = sorted(students, key=students.get, reverse=True)[0:num]
    return top_array


def extra_credit(grades, points=1):
    """
    Returns a dictionary of updated student scores with extra credit
    :param grades: (dictionary) student names: grades
    :param points: (int) number of extra credit points
    :return: (dictionary) of updated student scores
    """
    updated_grades = {}
    for key in grades:
        updated_grades[key] = grades[key] + points
    return updated_grades


def adjusted_grade(iclicker, exams):
    """
    Returns updated dictionary of student scores based off of iclicker
    and exam scores
    :param iclicker: (dictonary) of iclicker scores
    :param exams: (dictionary) of exam scores
    :return: (dictionary) of updated score
    """
    updated_grades = {}
    avg = 0
    for key in iclicker:
        avg += iclicker[key]
    if len(iclicker) != 0:
        avg = avg/len(iclicker)
    for key in exams:
        if key in iclicker:
            if iclicker[key] > avg:
                updated_grades[key] = exams[key] + 1
            else:
                updated_grades[key] = exams[key]
        else:
            updated_grades[key] = exams[key]
    for key in iclicker:
        if key not in exams:
            if iclicker[key] > avg:
                updated_grades[key] = 1
            else:
                updated_grades[key] = 0
    return updated_grades


def sum_of_inverse_odd(n):
    """
    Returns the sum of inverse (1/n) of odd numbers between 1 and n
    :param n: (int) positive integer
    :return: (int) sum from equation
    """
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            sum += 1 / i
    return sum


def same_length(*argv):
    """
    Checks if all the strings have same length
    :param argv: argument containing strings
    :return: (bool) if all string have same length
    """
    length = 0
    if len(argv) == 0:
        return True
    else:
        length = len(argv[0])
    for arg in argv:
        if len(arg) != length:
            return False
    return True


def main():
    # Question 1
    print("Question 1")
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    print(top_students(cs122, 2))  # ['Anna', 'Alex']
    print(top_students(cs122))  # ['Anna', 'Alex', 'Zoe']
    print(top_students(cs122, 10))  # ['Anna', 'Alex', 'Zoe', 'Dan']

    print(top_students(empty_class, 6))  # []
    print(cs122)  # {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}f

    # Question 2
    print("\nQuestion 2")
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(extra_credit(cs122))
    # {'Zoe':92, 'Alex': 95, 'Dan':81, 'Anna':102}
    print(
        extra_credit(cs122, 2))
    # {'Zoe':90, 'Alex': 93, 'Dan':79, 'Anna':100}
    print(cs122)
    # {}
    print(extra_credit(empty_class, 5))

    # Question 3
    print("\nQuestion 3")
    iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                'Bryan': 2, 'Andrea': 110}
    exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
            'Bryan': 95, 'Andrea': 86}
    # {'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96, 'Ryan': 90,
    # 'Andrea': 87, 'Dan': 89}
    print(adjusted_grade(iclicker, exam))
    # {'Ryan': 89, 'Andrea': 86, 'Bryan': 95, 'Anna': 64, 'Dan': 89, ''
    # 'Alex': 95}
    print(adjusted_grade({}, exam))
    # {'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0, 'Anna': 1,
    # 'Alex': 1}
    print(adjusted_grade(iclicker, {}))
    # {}
    print(adjusted_grade({}, {}))

    #Question 4
    print("\nQuestion 4")
    print(sum_of_inverse_odd(0))  # 0
    print(sum_of_inverse_odd(1))  # 1.0
    print(sum_of_inverse_odd(2))  # 1.0
    print(sum_of_inverse_odd(3))  # 1.3333333333333333
    print(sum_of_inverse_odd(2000))  # 4.435632673335106

    # Question 5
    print("\nQuestion 5")
    print(same_length())  # True
    print(same_length('hi', 'ha', 'it', 'quiet'))  # False
    print(same_length('hi', 'ha', 'it'))  # True
    print(same_length('hello', 'ha', 'it', 'ok'))  # False
    print(same_length('Spartan'))  # True


if __name__ == "__main__":
    main()
