import os


def test_package_zabbix_srv(host):
    p = host.package("zabbix-server-mysql")
    assert p.is_installed


def test_package_zabbix_frnt_php(host):
    p = host.package("zabbix-frontend-php")
    assert p.is_installed
