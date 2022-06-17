import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    p = host.package('apache2')
    assert p.is_installed


def test_pythonpip(host):
    if host.system_info.distribution == 'debian' and host.system_info.codename == 'bullseye':
        p = host.package('python3-pip')
        assert p.is_installed
    else:
        p = host.package('python-pip')
        assert p.is_installed
