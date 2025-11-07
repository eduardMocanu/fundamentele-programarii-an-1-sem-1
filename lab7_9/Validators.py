class Validators:

    def check_int(self, value):
        try:
            transformed = int(value)
            return True
        except ValueError:
            return False