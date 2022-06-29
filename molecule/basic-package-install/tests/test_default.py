import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    p = host.package('apache2')
    assert p.is_installed


def test_pythonpip(host):
    if host.system_info.distribution == 'debian' and host.system_info.codename == 'bullseye':
        package_name = 'python3-pip'
    else:
        package_name = 'python-pip'

    p = host.package(package_name)
    assert p.is_installed
