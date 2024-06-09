from S1E9 import Character


class Baratheon(Character):
    """ A class representing a Baratheon character."""
    def __init__(self, first_name: str, is_alive=True, eyes="brown", hairs="dark"):
        """Initializes a Lannister character."""
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs
        self.family_name = "Baratheon"
    
    def __str__(self) -> str:
        return f"<bound method Baratheon.__str__ of Vector: ({self.family_name}, {self.eyes}, {self.hairs})>"


class Lannister(Character):
    """A class representing a Lannister character."""
    def __init__(self, first_name: str, is_alive=True, eyes="blue", hairs="light"):
        """Initializes a Lannister character."""
        super().__init__(first_name, is_alive)
        self.eyes = eyes
        self.hairs = hairs
        self.family_name = "Lannister"
    
    def create_lannister(first_name: str, is_alive=True, eyes="blue", hairs="light"):
        """Creates a Lannister character."""
        return Lannister(first_name, is_alive, eyes, hairs)
