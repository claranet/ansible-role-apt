import os


def test_ppa_package(host):
    assert host.package("nodejs").is_installed
    assert host.package("nginx").is_installed
