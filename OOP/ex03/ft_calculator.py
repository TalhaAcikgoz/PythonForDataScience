class calculator:
    """ Ft_calculator """
    def __init__(self, list):
        self.list = list

    def __add__(self, object) -> None:
        li = []
        for i in self.list:
            li.append(i+object)
        self.list = li
        print(self.list)

    def __mul__(self, object) -> None:
        li = []
        for i in self.list:
            li.append(i*object)
        self.list = li
        print(self.list)

    def __sub__(self, object) -> None:
        li = []
        for i in self.list:
            li.append(i-object)
        self.list = li
        print(self.list)

    def __truediv__(self, object):
        if (object == 0):
            return 0
        li = []
        for i in self.list:
            li.append(i/object)
        self.list = li
        print(self.list)
