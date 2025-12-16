class Student:

    def __init__(self, studentId, studentName):
        self.__id = studentId
        self.__name = studentName

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_id(self, studentId):
        self.__id = studentId

    def set_name(self, studentName):
        self.__name = studentName

    def __str__(self):
        return f"{self.__id},{self.__name}"

    def __repr__(self):
        return f"Id: {self.__id}, Name: {self.__name}"

    def __eq__(self, other):
        if other.get_id() == self.get_id() and other.get_name() == self.get_name():
            return True
        return False