from typing import List, Any
from rich.panel import Panel
from rich.console import Console, Group
from rich.text import Text


class Terminal:
    _instance: "Terminal | None" = None
    _stdout: List[Text | str] = []
    _console: Console
    _attempts: int = 0
    
    def __new__(cls, *args: Any, **kwargs: Any) -> "Terminal":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self._console = Console()
            self._initialized = True
            
    def output(self, text: str | Text) -> None:
        self._stdout.append(text)
        group = Group(*self._stdout)
        self._console.clear()
        self._console.print(Panel(group))
        
    def exit(self) -> None:
        self._console.print(Text.from_markup("Bye!", style="bright_green"))
        exit(0)
        
    def temporal(self, text: str | Text) -> None:
        group = Group(*self._stdout)
        self._console.clear()
        self._console.print(Panel(group))
        self._console.print(text)