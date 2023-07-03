import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_version(host):
    p = host.package("nginx")
    assert p.is_installed

    if host.system_info.distribution == 'debian' and host.system_info.codename == 'stretch':
        assert p.version.startswith("1.10")
    elif host.system_info.distribution == 'debian' and host.system_info.codename == 'buster':
        assert p.version.startswith("1.14")
    elif host.system_info.distribution == 'debian' and host.system_info.codename == 'bullseye':
        assert p.version.startswith("1.18")
    elif host.system_info.distribution == 'debian' and host.system_info.codename == 'bookworm':
        assert p.version.startswith("1.22")
