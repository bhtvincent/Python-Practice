class Employee(object):
    """
    Represent an SJSU employee

    Arguments:
    name (string): employee's name.
    ssn (string):  employee's social security number


    Attributes:
    name (string): employee's name.
    ssn (string):  employee's social security number
    """

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __getattribute__(self, attr_name):
        value = super().__getattribute__(attr_name)
        if attr_name == "ssn":
            return "XXX-XX-" + value[-4:]
        else:
            return value