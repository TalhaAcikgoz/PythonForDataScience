from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ Your docstring for King class """
    def __init__(self, first_name: str, is_alive=True, eyes="brown",
                 hairs="dark"):
        super().__init__(first_name, is_alive, eyes, hairs)

    def set_eyes(self, eyes="brown"):
        self.eyes = eyes

    def set_hairs(self, hairs="dark"):
        self.hairs = hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs

    def __str__():
        return "King"
