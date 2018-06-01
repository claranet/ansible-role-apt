import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    p = host.package('apache2')
    assert p.is_installed


def test_pythonpip(host):
    p = host.package('python-pip')
    assert p.is_installed
