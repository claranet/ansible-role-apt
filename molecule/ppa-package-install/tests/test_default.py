import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ppa_package(host):
    pkgnode = host.package('nodejs')
    pkgngnix = host.package('nginx')
    assert pkgnode.is_installed
    assert pkgngnix.is_installed
