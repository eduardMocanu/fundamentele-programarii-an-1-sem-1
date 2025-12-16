from operator import truediv


class Client:

    def __init__(self, id, nume, CNP):
        self.__id = id
        self.__nume = nume
        self.__CNP = CNP

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_CNP(self):
        return self.__CNP

    def set_id(self, id):
        self.__id = id

    def set_nume(self, nume):
        self.__nume = nume

    def set_CNP(self, CNP):
        self.__CNP = CNP

    def __repr__(self):
        return f"Nume: {self.__nume}, Id: {self.__id}, CNP: {self.__CNP}"

    def __eq__(self, other):
        if other.get_nume() == self.get_nume() and other.get_id() == self.get_id() and self.get_CNP() == other.get_CNP():
            return True
        return False