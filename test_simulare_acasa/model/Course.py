class Course:

    def __init__(self, courseId, courseName, courseStudents):
        self.__id = courseId
        self.__name = courseName
        self.__students = courseStudents

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_students(self):
        return list(self.__students)

    def set_id(self, courseId):
        self.__id = courseId

    def set_name(self, courseName):
        self.__name = courseName

    def set_students(self, courseStudents):
        self.__students = list(courseStudents)
