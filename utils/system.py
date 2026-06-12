import platform

import distro
import psutil

__DISTRO: dict[tuple[str, ...], str] = {
    ("fedora", "rhel"): "RHEL",
    ("ubuntu", "debian"): "DEBIAN"
}

def get_distro() -> str:
    os = platform.system()

    if os != "Linux":
        raise NotImplementedError(os)

    os_distro_id = distro.id()

    for keys, value in __DISTRO.items():
        if os_distro_id.lower() in keys:
            return value
    raise NotImplementedError(os_distro_id)

def get_threads():
    return psutil.cpu_count(logical=True)
