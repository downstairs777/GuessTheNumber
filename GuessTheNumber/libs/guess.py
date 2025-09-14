import random
from rich.prompt import Prompt
from rich.text import Text
from libs.game import Game
from libs.console import Terminal


class Guess(Game):
    terminal: Terminal
    
    def __init__(self) -> None:
        self.terminal = Terminal()
    
    def play(self):
        number = random.randint(1, 10)
        attempts = 0
        
        self.terminal.output(
            Text.from_markup(
                f"Ok, I'm thinking of a number between 1 and 10. Try to guess the number!", 
                style="bright_magenta"
            )
        )
        
        guessed = False        
        while not guessed:
            if attempts > 0: self.terminal.output(Text.from_markup(f"You have {attempts} attempts left.", style="bright_yellow"))
            input = Prompt.ask(Text.from_markup("Which number am I thinking of?", style="bright_yellow"))
            try:
                if input == "exit": self.terminal.exit()
                elif int(input) == number:
                    self.terminal.output(Text.from_markup("You guessed the number!", style="bright_green"))
                    guessed = True
                elif int(input) < number:
                    self.terminal.output(Text.from_markup(f"The number {input} is too low!", style="bright_magenta"))
                    attempts += 1
                else:
                    self.terminal.output(Text.from_markup(f"The number {input} is too high!", style="bright_magenta"))
                    attempts += 1
            except ValueError:
                self.terminal.temporal(Text.from_markup("Invalid number. Please try again.", style="bright_red"))
                continue