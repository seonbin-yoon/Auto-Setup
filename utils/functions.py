import datetime
import os
import sys
from typing import Any, NoReturn

from utils import color_print
from utils.color_print import Color


def program_exit(exit_code: int = 0, message: Any = "", color: str = Color.RESET)\
    -> NoReturn:

    if message:
        color_print.write(message, color)
    sys.exit(exit_code)

def get_spend_time(start_time: datetime.datetime, end_time: datetime.datetime) -> str:
    spend_second = int((end_time - start_time).total_seconds())

    if spend_second < 60:
        return f"{spend_second}초"

    if spend_second < 3600:
        return f"{spend_second // 60}분"

    return f"{spend_second // 3600}시간"

def check_need_sudo() -> bool:
    if os.getuid() == 0:
        return False

    return True
