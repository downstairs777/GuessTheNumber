from art import tprint # type: ignore
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from libs.thinking import Thinking
from libs.guess import Guess
from libs.game import Game


class Menu:
    _console: Console
    
    def __init__(self):
        self._console = Console()
    
    def main(self):
        tprint("Guess The Number")
        self._console.print(Text.from_markup("Welcome to the game!", style="bright_green"))
        self._console.print(Text.from_markup("Enter 'exit' to exit the game.", style="grey27"))
        
        game = self._select_mode()
        game.play(console=self._console)
        
    def _select_mode(self) -> Game:
        while True:
            mode = Prompt.ask(
                Text.from_markup("Enter your mode", style="bright_yellow"), 
                choices=["I guess", "I'm thinking", "exit"], 
                case_sensitive=False
            )
            if mode == "exit": 
                self._console.print(Text.from_markup("Bye!", style="bright_green"))
                exit(0)
            elif mode == "I guess": return Guess()
            elif mode == "I'm thinking": return Thinking()
            else: self._console.print(Text.from_markup("Invalid mode. Please try again.", style="bright_red"))


if __name__ == "__main__":
    menu = Menu()
    menu.main()
