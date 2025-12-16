
class Sorts:

    @staticmethod
    def quick_sort(lista, key=lambda x: x, rev=False):

        def helper(lst):
            if len(lst) <= 1:
                return lst

            pivot = lst[0]
            left = []
            right = []

            for x in lst[1:]:
                if key(x) <= key(pivot):
                    left.append(x)
                else:
                    right.append(x)

            return helper(left) + [pivot] + helper(right)

        rezultat = helper(lista)
        if rev:
            return rezultat[::-1]
        return rezultat

    @staticmethod
    def gnome_sort(lista, key = lambda x: x, rev = False):
        temp_list = [x for x in lista]

        index = 0
        n = len(temp_list)
        while index < n:
            if index == 0:
                index += 1
            if key(temp_list[index]) >= key(temp_list[index - 1]):
                index += 1
            else:
                temp_list[index], temp_list[index-1] = temp_list[index-1], temp_list[index]
                index -= 1
        if rev:
            return temp_list[::-1]
        return temp_list
