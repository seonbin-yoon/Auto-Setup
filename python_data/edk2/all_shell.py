from utils import datatype

make_project_dir: datatype.ShellTask = {
            "Message": "프로젝트 폴더 생성",
            "Exec": ["mkdir", "!Edkpath"],
            "Path": "!Home",
        }

git_clone: datatype.ShellTask = {
            "Message": "edk2 소스 다운받기",
            "Exec": [
                "git",
                "clone",
                "--depth",
                "1",
                "https://github.com/tianocore/edk2"
                ],
            "Path": "!Edkpath",
        }

git_init: datatype.ShellTask = {
            "Message": "서브모듈 초기화 하기",
            "Exec": ["git", "submodule", "update", "--init"],
            "Path": "!Edkpath/edk2",
        }

make: datatype.ShellTask = {
            "Message": "BaseTools make 하기",
            "Exec": ["make", "-C", "BaseTools"],
            "Path": "!Edkpath/edk2",
        }


edksetup_sh: datatype.ShellTask = {
            "Message": "부가 파일 생성",
            "Path": "!Edkpath/edk2",
            "Exec" : ["bash", "-c", "source edksetup.sh"],
        }

make2: datatype.ShellTask = {
            "Message": "BaseTools make 하기 x2",
            "Exec": ["make", "-C", "BaseTools"],
            "Path": "!Edkpath/edk2",
        }

install_tasks = [
    make_project_dir,
    git_clone,
    git_init,
    make,
    edksetup_sh,
    make2
]
