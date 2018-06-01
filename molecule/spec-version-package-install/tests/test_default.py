import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_version(host):
    p = host.package("nginx")
    assert p.is_installed
    assert p.version.startswith("1.10")
