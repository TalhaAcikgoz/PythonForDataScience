from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for character class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """ Your docstring for Character constructor method"""
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """Your docstring for Stark class"""
    def __init__(self, first_name: str, is_alive=True):
        """Your docstring for Stark constructor method"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Stark die method"""
        self.is_alive = False
