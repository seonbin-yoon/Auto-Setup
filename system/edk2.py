import os

from python_data import all_func, all_shell
from system import execute
from utils import check, color_print, datatype
from utils.color_print import Color
from utils.functions import program_exit


def install(program_context: datatype.Contexts) -> bool:
    _wake(program_context.config, install=True)
    color_print.write("이 작업은 시간이 조금 걸릴 수 있습니다..", Color.MAGENTA)

    func_tasks = _get_func_task_lists(install=True)
    shell_tasks = _get_shell_task_lists(program_context.distro)

    _processing_tasks(shell_tasks, program_context)

    task_contexts = datatype.TaskContexts(
        func_task_num=len(func_tasks),
        shell_task_num=len(shell_tasks),
        total_num=len(shell_tasks) + len(func_tasks)
    )

    execute.shell_run(shell_tasks, task_contexts)
    execute.func_run(func_tasks, task_contexts, program_context)

    color_print.write("")
    return True

def delete(program_context: datatype.Contexts) -> bool:
    _wake(program_context.config, install=False)

    return True

def _wake(config: datatype.Config, install: bool):
    """중복 호출이 되는 부분이므로, edk2 설정을 확인하는 부분을
    한 함수로 묶었습니다.\n"""

    color_print.clear_screen()
    color_print.write("edk2 셋팅을 시작합니다..", Color.YELLOW)

    color_print.write("\r설치 여부 검사 -> ...", Color.YELLOW, end="")
    try:
        __check(config, install)
    except FileExistsError as Error:
        program_exit(1, f"\r설치 여부 검사 -> 실패\n{Error}", Color.RED)
    color_print.write("\r설치 여부 검사 -> 통과", Color.GREEN, end="")

    color_print.write("\r설정 파일 내용 검사 -> ...", Color.YELLOW, end="")
    try:
        check.edk2_config(config)
    except NotImplementedError as error_message:
        program_exit(
            1, f"\r설정 파일 내용 검사 -> 실패\n{error_message}", Color.RED
            )
    color_print.write("\r설정 파일 내용 검사 -> 통과", Color.GREEN)

def __check(config: datatype.Config, install: bool):
    result = os.path.exists(config["edk2_path"])
    if install and result or not install and not result:
        raise FileExistsError("이미 edk2 폴더가 존재하므로 더 이상 진행할 수 없습니다.")


def _get_shell_task_lists(distro: str) -> list[datatype.Task]:
    if distro == "RHEL":
        from python_data.RHEL import rhel_command
        task = rhel_command.install_tasks
        task.extend(all_shell.c_install_tasks)
    elif distro == "DEBIAN":
        raise NotImplementedError
    else:
        raise NotImplementedError

    return task

def _get_func_task_lists(install: bool) -> list[datatype.Function]:
    if install:
        return all_func.install_tasks
    else:
        raise NotImplementedError

def _processing_tasks(raw_tasks: list[datatype.Task], program_context: datatype.Contexts):
    for task in raw_tasks:
        if "!Home" in task["Path"]:
            task["Path"] = task["Path"].replace("!Home", program_context.home)
        if "!Edkpath" in task["Path"]:
            task["Path"] = task["Path"].replace("!Edkpath", program_context.config["edk2_path"])

        for num, _exec in enumerate(task["Exec"]):
            if "!Edkpath" in _exec:
                _exec = _exec.replace("!Edkpath", program_context.config["edk2_path"])
                task["Exec"][num] = _exec