from modules import datatype

package_install: datatype.ShellTask = {
    "Message": "Qemu용 패키지 설치",
    "Path": "!Home",
    "Exec": [
        "sudo",
        "apt",
        "install",
        "-y",
        "qemu-system-x86"
        ]
}

install_tasks: list[datatype.ShellTask] = [
    package_install
]
