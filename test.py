class Test:
    __number_of_calls = 0
    def __init__(self, num):
        self.__test_number = num
        Test.__number_of_calls += 1

    def get_test_number(self):
        return self.__test_number

    def set_test_number(self, num):
        self.__test_number = num

    @classmethod
    def get_number_of_calls(cls):
        return cls.__number_of_calls

    def __str__(self):
        return f"Number: {self.__test_number} and {Test.__number_of_calls} 2 instances"


test = Test(200)
print(test.get_test_number())
test.set_test_number(2000)
print(test.get_test_number())

test1 = Test(1000)

print(Test.get_number_of_calls())

print(test)