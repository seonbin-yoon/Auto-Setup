import sys
from typing import Any, NoReturn

from utils import color_print
from utils.color_print import Color


def program_exit(exit_code: int = 0, message: Any = "", color: str = Color.RESET)\
    -> NoReturn:

    if message:
        color_print.write(message, color)
    sys.exit(exit_code)
