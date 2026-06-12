from utils import datatype

make_project_dir: datatype.Task = {
            "Message": "프로젝트 폴더 생성",
            "Exec": ["mkdir", "!Edkpath"],
            "Path": "!Home",
        }

git_clone: datatype.Task = {
            "Message": "edk2 소스 다운받기",
            "Exec": ["git", "clone", "https://github.com/tianocore/edk2"],
            "Path": "!Edkpath",
        }

git_init: datatype.Task = {
            "Message": "서브모듈 초기화 하기",
            "Exec": ["git", "submodule", "update", "--init"],
            "Path": "!Edkpath/edk2",
        }

make: datatype.Task = {
            "Message": "BaseTools make 하기",
            "Exec": ["make", "-C", "BaseTools"],
            "Path": "!Edkpath/edk2",
        }
"""
        {
            "Exec" : ["bash", "-c", "source edksetup.sh"],
            "Path": "!Edkpath/edk2",
            "explan": "edksetup.sh를 실행"
        },
"""
make2: datatype.Task = {
            "Message": "BaseTools make 하기 x2",
            "Exec": ["make", "-C", "BaseTools"],
            "Path": "!Edkpath/edk2",
        }

c_install_tasks = [
    make_project_dir,
    git_clone,
    git_init,
    make,
    make2
]
