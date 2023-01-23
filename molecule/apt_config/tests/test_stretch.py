import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("stretch")

# have a look at https://testinfra.readthedocs.io/en/latest/modules.html to see the different possible tests


def test_apt_config_dump(host):
    apt_config_dump = host.check_output("apt-config dump | grep -e '^Acquire::https?::Proxy' -e ^APT::Periodic:: -e ^Unattended-Upgrade:: -e ^Acquire::AllowReleaseInfoChange:: | LC_ALL=C sort")
    apt_config_dump_expected = """\
APT::Periodic::AutocleanInterval "7";
APT::Periodic::BackupArchiveInterval "0";
APT::Periodic::BackupLevel "3";
APT::Periodic::CleanInterval "0";
APT::Periodic::Download-Upgradeable-Packages "0";
APT::Periodic::Enable "1";
APT::Periodic::Unattended-Upgrade "1";
APT::Periodic::Update-Package-Lists "1";
Acquire::AllowReleaseInfoChange::Suite "true";
Unattended-Upgrade::Allow-APT-Mark-Fallback "true";
Unattended-Upgrade::Allow-downgrade "false";
Unattended-Upgrade::AutoFixInterruptedDpkg "true";
Unattended-Upgrade::Automatic-Reboot "false";
Unattended-Upgrade::Automatic-Reboot-Time "now";
Unattended-Upgrade::Automatic-Reboot-WithUsers "true";
Unattended-Upgrade::Debug "false";
Unattended-Upgrade::IgnoreAppsRequireRestart "false";
Unattended-Upgrade::InstallOnShutdown "false";
Unattended-Upgrade::MailReport "on-change";
Unattended-Upgrade::MinimalSteps "true";
Unattended-Upgrade::OnlyOnACPower "false";
Unattended-Upgrade::Origins-Pattern "";
Unattended-Upgrade::Origins-Pattern:: "origin=Debian,codename=${distro_codename},label=Debian-Security";
Unattended-Upgrade::Remove-New-Unused-Dependencies "false";
Unattended-Upgrade::Remove-Unused-Dependencies "false";
Unattended-Upgrade::Remove-Unused-Kernel-Packages "true";
Unattended-Upgrade::Skip-Updates-On-Metered-Connections "true";
Unattended-Upgrade::SyslogEnable "false";
Unattended-Upgrade::SyslogFacility "daemon";
Unattended-Upgrade::Verbose "false";"""
    assert apt_config_dump == apt_config_dump_expected


def test_unattended_upgrades_override(host):
    assert host.file("/etc/systemd/system/apt-daily-upgrade.timer.d/ansible_aptconfig.conf").exists
    timer = host.check_output("systemctl list-timers apt-daily-upgrade.timer")
    assert re.search(r'\w{3} \d{4}-\d\d-\d\d 22:[01]\d:\d\d UTC', timer)
