import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_zabbix_srv(host):
    p = host.package('zabbix-server-mysql')
    assert p.is_installed


def test_package_zabbix_frnt_php(host):
    p = host.package('zabbix-frontend-php')
    assert p.is_installed
