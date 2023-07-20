import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ppa_package(host):
    assert host.package('nodejs').is_installed
    assert host.package('nginx').is_installed
