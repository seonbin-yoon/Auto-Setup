from utils import datatype

package_update: datatype.ShellTask = {
    "Message": "최신 패키지 정보 업데이트",
    "Path": "!Home",
    "Exec": [
        "sudo",
        "apt",
        "update"
        ]
}

package_upgrade: datatype.ShellTask = {
    "Message": "로컬 패키지 업데이트",
    "Path": "!Home",
    "Exec": [
        "sudo",
        "apt",
        "upgrade"
    ]
}

package_install: datatype.ShellTask = {
    "Message": "빌드용 필수 패키지 설치",
    "Path": "!Home",
    "Exec": [
        "sudo",
        "apt",
        "install",
        "-y",
        "build-essential",
        "uuid-dev",
        "iasl",
        "git",
        "nasm",
        "python3"
        ]
}

install_tasks: list[datatype.ShellTask] = [
    package_update,
    package_upgrade,
    package_install
]
