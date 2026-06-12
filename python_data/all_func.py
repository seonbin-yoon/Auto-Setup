import os

from utils import datatype


# INSTALL
def _add_bashrc_func(context: datatype.Contexts):
    function = __processing_bash_func(context)
    bashrc_path = os.path.join(context.home, ".bashrc")

    with open(bashrc_path, "a", encoding='utf-8') as bashrc:
        bashrc.writelines(function)

def __processing_bash_func(context: datatype.Contexts) -> list[str]:
    source_file_path = os.path.join(context.program, "data", "bash.txt")
    function: list[str] = []

    with open(source_file_path, encoding='utf-8') as source_file:
        for line in source_file:
            if "!Edk2path" in line:
                line = line.replace("!Edk2path", context.config["edk2_path"])

            function.append(line)

    return function

install_tasks: list[datatype.Function] = [
    {
        "Message": "bashrc 환경 활성화 함수 추가",
        "Func": _add_bashrc_func
    },
]
