from utils import datatype

add_kvm_group: datatype.ShellTask = {
    "Message": "kvm 그룹 등록",
    "Path": "!Home",
    "Exec": [
        "sudo",
        "usermod",
        "-aG",
        "kvm",
        "$USER"
    ]
}

install_task: list[datatype.ShellTask] = [
    add_kvm_group
]
