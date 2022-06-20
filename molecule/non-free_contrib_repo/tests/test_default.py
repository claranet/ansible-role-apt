import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_album(host):
    p = host.package('album')
    assert p.is_installed


def test_java_package(host):
    p = host.package('java-package')
    assert p.is_installed
