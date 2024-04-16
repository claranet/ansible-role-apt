import os


def test_apt_confd_99ansible(host):
    f = host.file("/etc/apt/apt.conf.d/99ansible")
    assert f.exists
    assert not f.contains("Acquire::https::Proxy")
    assert f.contains('APT::Periodic::Enable "1";')
    assert f.contains('APT::Periodic::AutocleanInterval "7";')


def test_package_unattended_upgrades(host):
    assert host.package("unattended-upgrades").is_installed


def test_package_apt_listchanges(host):
    assert not host.package("apt-listchanges").is_installed
