import os


def test_ppa_package(host):
    assert host.package("nodejs").is_installed
    assert host.package("nginx").is_installed

def test_node_package_version(host):
   check_version = host.run("node --version")
   assert "18" in check_version.stdout
