class Validators:
    def __init__(self):
        pass

    def check_ID(self, ID):
        try:
            a = int(ID)
            return True
        except:
            return False