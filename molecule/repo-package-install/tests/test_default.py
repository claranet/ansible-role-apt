import os


def test_version(host):
    p = host.package("nginx")
    assert p.is_installed

    os_characteristics = [
        {"distribution": "debian", "codename": "stretch", "version": "1.10"},
        {"distribution": "debian", "codename": "buster", "version": "1.14"},
        {"distribution": "debian", "codename": "bullseye", "version": "1.18"},
        {"distribution": "debian", "codename": "bookworm", "version": "1.22"},
        {"distribution": "ubuntu", "codename": "noble", "version": "1.24"},
    ]

    current_os = list(
        filter(
            lambda os_c: os_c["distribution"] == host.system_info.distribution
            and os_c["codename"] == host.system_info.codename,
            os_characteristics,
        )
    )
    version = current_os[0]["version"] if len(current_os) > 0 else "1.18"

    assert p.version.startswith(version)


def test_htop_package_version(host):
    check_version = host.run("htop --version")
    assert "3.3.0" in check_version.stdout
