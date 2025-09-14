from rich.console import Console
# from rich.prompt import Prompt
# from rich.text import Text
from libs.game import Game


class Thinking(Game):
    def play(self, console: Console):
        print("Playing I'm thinking...")