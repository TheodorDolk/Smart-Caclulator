import re


class Calculator:
    def __init__(self):
        self.variables = {}
        self.input = ""

    def add_variable(self):
        self.input = self.input.replace(" ", "").split("=")

        # Many "=" signs
        if len(self.input) != 2:
            print("Invalid assignment")
            return

        # Invalid identifier (left side)
        if not is_latin(self.input[0]):
            print("Invalid identifier")
            return

        # Invalid assignment (right side)
        if not is_latin(self.input[1]) and not self.input[1].isdigit():
            print("Invalid assignment")
            return

        # Assignment variable is not a number (right side)
        if is_latin(self.input[1]):
            if self.input[1] in self.variables:
                self.variables[self.input[0]] = self.variables[self.input[1]]
            else:
                print("Unknown variable")
        else:
            # Assignment variable is a number (right side)
            self.variables[self.input[0]] = int(self.input[1])

    def print_variable(self):
        self.input = self.input.replace(" ", "")
        if is_latin(self.input):
            try:
                print(self.variables[self.input])
            except KeyError:
                print("Unknown variable")
        else:
            print("Invalid identifier")

    def evaluate(self):
        self.input = self.input.replace("/", "//")
        pattern = re.compile(r'\++')
        self.input = re.sub(pattern, "+", self.input)

        pattern_even = re.compile(r'\-(?=(\-{2})*[^-])')
        self.input = pattern_even.sub('-', self.input)

        for item in self.input:
            if item in self.variables.keys():
                self.input = self.input.replace(item, str(self.variables.get(item)))
        try:
            print(eval(self.input))
        except SyntaxError:
            print("Invalid expression")

    def run_command(self):
        if self.input == "/exit":
            print("Bye!")
            exit()
        elif self.input == "/help":
            print("The program calculates the sum of numbers")
        else:
            print("Unknown command")


def is_latin(s):
    pattern = re.compile('^[a-zA-Z]+$')
    return pattern.match(s) is not None


def main():
    calc = Calculator()
    while True:

        calc.input = input("")
        if calc.input.replace(" ", "") == "":
            continue

        elif calc.input[0] == "/":
            calc.run_command()

        elif "=" in calc.input and ("+" in calc.input
                                    or "-" in calc.input
                                    or "*" in calc.input
                                    or "/" in calc.input):
            print("Invalid assignment")

        elif "=" not in calc.input \
                and "+" not in calc.input \
                and "-" not in calc.input \
                and "*" not in calc.input \
                and "/" not in calc.input:

            calc.print_variable()

        elif "=" in calc.input and "+" not in calc.input and "-" not in calc.input:
            calc.add_variable()

        elif "=" not in calc.input and ("+" in calc.input
                                        or "-" in calc.input
                                        or "*" in calc.input
                                        or "/" in calc.input):
            calc.evaluate()


if __name__ == "__main__":
    main()
