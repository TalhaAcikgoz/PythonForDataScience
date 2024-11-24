from typing import Any
from S1E9 import Character


class Baratheon(Character):
    """Representing a Baratheon character."""
    def __init__(self, first_name: str, is_alive=True, eyes="brown",
                 hairs="dark"):
        """Initializes a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        self.is_alive = False

    def __getattribute__(self, name: str) -> Any:
        if name == "__str__":
            return f"({self.family_name}, {self.eyes}, {self.hairs})"
        return super().__getattribute__(name)

    def __str__(self):
        return f"<bound method Baratheon.__str__ of Vector: (\
            {self.family_name}, {self.eyes}, {self.hairs})>"

    @property
    def __repr__(self):
        return f"<bound method Baratheon.__repr__ of Vector: (\
            {self.family_name}, {self.eyes}, {self.hairs})>"


class Lannister(Character):
    """A class representing a Lannister character."""
    def __init__(self, first_name: str, is_alive=True,
                 eyes="blue", hairs="light"):
        """Initializes a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    def create_lannister(first_name: str, is_alive=True, eyes="blue",
                         hairs="light"):
        """Creates a Lannister character."""
        return Lannister(first_name, is_alive, eyes, hairs)

    def __getattribute__(self, name: str) -> Any:
        if name == "__str__":
            return f"<bound method Baratheon.__str__ of Vector: (\
                {self.family_name}, {self.eyes}, {self.hairs})>"
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return f"<bound method Baratheon.__str__ of Vector: (\
            {self.family_name}, {self.eyes}, {self.hairs})>"
