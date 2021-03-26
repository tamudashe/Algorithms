class Employee:
    """
    __init__ method is the constructor
    - it is raa automatically whe the class is instantiated
    - the [self] argument is by convention, it can be any word
    - the self.[name] can also be changed to anything
    """
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@theofficeusa.com".format(first, last)

    def display_full_name(self):
        return "{} {}".format(self.first, self.last)

def main():
    emp_1 = Employee("Dwight", "Schrute", 99999)
    emp_2 = Employee("Jim", "Halpert", 100000)

    print(emp_1.email)
    print(emp_2.display_full_name())


if __name__ == '__main__':
    main()
