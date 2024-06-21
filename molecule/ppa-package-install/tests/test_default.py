import os


def test_ppa_package(host):
    assert host.package("code").is_installed
    assert host.package("nginx").is_installed

def test_vscode_package_version(host):
   check_version = host.run("code --no-sandbox --user-data-dir /tmp --version")
   assert "1.90.2" in check_version.stdout
