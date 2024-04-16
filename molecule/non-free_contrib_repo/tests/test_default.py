import os


def test_package(host):
    p = host.package("apache2")
    assert p.is_installed
