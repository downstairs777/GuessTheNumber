import random
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from libs.game import Game


class Guess(Game):
    
    def play(self, console: Console):
        number = random.randint(1, 10)
        
        console.print(Text.from_markup("Ok, I'm thinking...", style="bright_magenta"))
        console.print(Text.from_markup(f"I'm thinking of a number between 1 and 10", style="bright_magenta"))
        console.print(Text.from_markup(f"Try to guess the number", style="bright_magenta"))
        console.print(Text.from_markup(f"Enter 'exit' to exit the game.", style="grey27"))
        
        guessed = False
        
        while not guessed:
            input = Prompt.ask(Text.from_markup("Which number am I thinking of?", style="bright_yellow"))
            try:
                if input == "exit":
                    console.print(Text.from_markup("Bye!", style="bright_green"))
                    exit(0)
                elif int(input) == number:
                    console.print(Text.from_markup("You guessed the number!", style="bright_green"))
                    guessed = True
                elif int(input) < number:
                    console.print(Text.from_markup("Too low!", style="bright_magenta"))
                elif int(input) > number:
                    console.print(Text.from_markup("Too high!", style="bright_magenta"))
                else:
                    console.print(Text.from_markup("Wrong number!", style="bright_red"))
            except ValueError:
                console.print(Text.from_markup("Invalid number. Please try again.", style="bright_red"))
                continue
        
        
        