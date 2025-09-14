from rich.console import Console
from abc import ABC, abstractmethod


class Game(ABC):
    
    @abstractmethod
    def play(self, console: Console):
        pass