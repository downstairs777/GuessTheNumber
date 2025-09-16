from typing import List
from art import text2art # type: ignore
from rich.text import Text
from libs.guess import Guess
from libs.game import Game
from libs.console import Terminal
from InquirerPy import inquirer


# OPTIONS = ["I guess", "I'm thinking", "exit"]
OPTIONS = ["I guess", "exit"]


class Menu:
    _stdout: List[Text | str] = []
    terminal: Terminal
    
    def __init__(self) -> None:
        self.terminal = Terminal()
        
    def _select_mode(self) -> Game:
        while True:
            mode = inquirer.select( # type: ignore
                "Select your mode of play",
                choices=OPTIONS,
            ).execute()
            if mode == "exit": self.terminal.exit()
            elif mode.lower() == "i guess": return Guess()
            else: self.terminal.temporal(Text.from_markup("Invalid mode. Please try again.", style="bright_red"))

    def main(self):
        title = text2art("Guess The Number") # type: ignore
        self.terminal.output(title) # type: ignore
        self.terminal.output(Text.from_markup("Enter 'exit' to exit.", style="grey27"))
        self.terminal.output(Text.from_markup("Welcome to the Guess The Number game!", style="orange1"))
        
        game = self._select_mode()
        game.play()


if __name__ == "__main__":
    menu = Menu()
    menu.main()
