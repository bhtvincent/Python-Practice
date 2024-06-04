def most_e(*args):
    """
    Returns the string with the most occurrences of the letter 'e'.

    :param args: any number of strings
    :return: the string with the most occurrences of the letter 'e'
    """
    if len(args) == 0:
        return None
    return max(args, key=lambda count_e: count_e.count('E') + count_e.count(
        'e'))


def top_midterm(grades, n=4):
    """
    Returns a list that contains the names of the top n students with the
    highest midterm grade.

    :param grades: a dictionary representing the student grades
    :param n: (default=4) amount of top students to return for the list
    :return: list containing the names of the top n students with the
    highest midterm grades
    """
    return sorted(grades, key=lambda midterm: grades[midterm][2],
                  reverse=True)[:n]


def shout(function):
    """
    Decorator used with functions that return strings that converts the
    return value to uppercase and adds '!!!' to the end.

    :param function: the function to uppercase and add '!!!' to
    :return: the converted return value of the function
    """
    def wrapper(*args):
        message = function(*args).upper() + '!!!'
        return message
    return wrapper


def repeat_character(seq, n):
    """
    Generates strings of length n

    :param seq: the string of characters
    :param n: the length to generate for each character
    :return: the character repeated num times
    """
    start = 0
    while start < len(seq):
        repeated_string = seq[start]*n
        yield repeated_string
        start += 1


def alpha_labels(seq='A'):
    """
    Generates labels alphabetically, starting with the starting label and
    increases length after reaching 'Z'.

    :param seq: (default = 'A') The starting label to use
    :return: the sequence incremented after each yield
    """
    import string
    alphabet = string.ascii_uppercase
    position = alphabet.index(seq[0])
    length = len(seq)
    while True:
        if position == 26:
            position = 0
            length += 1
        yield from(repeat_character(alphabet[position], length))
        position += 1

# Functions for Question 3
@shout
def greet(name):
    """
    Return a personalized hello message.
    :param name: (string)
    :return: (string)
    """
    return f'Hello {name}'

@shout
def repeat(phrase, n):
    """
    Repeat the specified string n times
    with a space character in between.
    :param phrase: (string)
    :param n: number of times the phrase will be repeated
    :return:
    """
    words = phrase.split()
    return ' '.join(n * words)


def main():
    # Question 1
    print("Question 1\n")
    print(most_e())  # None
    print(most_e('Go', 'Spartans', 'Take', 'Selfies', 'eat',
                 'APPLES'))  # Selfies
    print(most_e('Go', 'Spartans', 'APPLES'))  # APPLES
    print(most_e('Go', 'Spartans', 'Eat'))  # Eat
    print(most_e('Go', 'Spartans', 'Take', 'Selfies', 'degree'))  # degree
    print(most_e('Spartans'))  # Spartans

    # Question 2
    print("\nQuestion 2\n")
    empty_class = {}
    cs122 = {'Zoe': [90, 100, 75], 'Alex': [86, 90, 96],
             'Dan': [90, 60, 70], 'Anna': [60, 80, 100],
             'Ryan': [100, 95, 80], 'Bella': [79, 70, 99]}

    print(top_midterm(cs122, 2))  # ['Anna', 'Bella']
    print(top_midterm(cs122))  # ['Anna', 'Bella', 'Alex', 'Ryan']
    print(top_midterm(cs122,
                      10))  # ['Anna', 'Bella', 'Alex', 'Ryan', 'Zoe', # 'Dan']

    print(top_midterm(empty_class, 6))  # []
    print(cs122)  # {'Zoe': [90, 100, 75], 'Alex': [86, 90, 96],
    # 'Dan': [90, 60, 70], 'Anna': [60, 80, 100], 'Ryan': [100, 95, 80],
    # 'Bella': [79, 70, 99]}

    # Question 3
    print("\nQuestion 3\n")
    print(greet('Rula'))  # HELLO RULA!!!
    print(repeat('Python is fun!',
                 3))  # PYTHON IS FUN! PYTHON IS FUN! PYTHON IS FUN!!!!
    print(repeat('Go Spartans!',
                 5))  # GO SPARTANS! GO SPARTANS! GO SPARTANS!
    # GO SPARTANS! GO SPARTANS!!!!

    # Question 4
    print("\nQuestion 4\n")
    '''vocabulary = repeat_character('ACGT', 3)
    print(next(vocabulary))  # AAA
    print(next(vocabulary))  # CCC
    print(next(vocabulary))  # GGG
    print(next(vocabulary))  # TTT
    print(next(vocabulary))  # StopIteration'''

    import string
    labels = repeat_character(string.ascii_uppercase, 2)
    for each_label in labels:
        print(each_label)  # AA through ZZ is printed.

    # Question 5
    print("\nQuestion 5")
    # labels = alpha_labels('YY')
    labels = alpha_labels()
    for each_label in labels:
        print(each_label)


if __name__ == "__main__":
    main()
