from utils import datatype

package_upgrade: datatype.ShellTask = {
    "Message": "로컬 패키지 업데이트",
    "Path": "!Home",
    "Exec": [
        "sudo",
        "dnf",
        "upgrade",
        "-y"
        ]
}

package_install: datatype.ShellTask = {
    "Message": "빌드용 필수 패키지 설치",
    "Path": "!Home",
    "Exec": [
        "sudo",
        "dnf",
        "install",
        "-y",
        "@development-tools",
        "gcc-c++",
        "libuuid-devel",
        "acpica-tools",
        "git",
        "nasm"
        ]
}

install_tasks: list[datatype.ShellTask] = [
    package_upgrade,
    package_install
]
