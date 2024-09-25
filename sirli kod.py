import random
import string


class Codgenerator:
    def __init__(self):
        self.__code = ""

    def code_condition(self, length):
        characters = string.ascii_letters + string.digits
        self.__code = ''.join(random.choice(characters) for _ in range(length))

    def take_code(self, length):
        if len(self.__code) == length:
            return self.__code
        else:
            return "Access Denied"


generator = Codgenerator()

generator.code_condition(8)
print(generator.take_code(8))
print(generator.take_code(6))
