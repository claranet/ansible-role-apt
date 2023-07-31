# Ansible role - apt
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-apt?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-apt?style=flat-square)](https://github.com/claranet/ansible-role-aot/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-apt/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-apt/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/apt)

> :star: Star us on GitHub — it motivates us a lot!*

Install packages and add repositories on apt based distributions :

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.apt
```
## :gear: Role variables
--------------

Variable                                      | Default value                                              | Description
----------------------------------------------|------------------------------------------------------------|--------------------------------------
apt_upgrade                                   | **false**                                                  | Do an upgrade (no, yes, safe, full, dist)
apt_autoremove                                | **true**                                                   | Remove packages that are no longer needed for dependencies
apt_packages                                  | **[]**                                                     | Packages list to install
apt_repositories                              | **[[]](molecule/ppa-package-install/converge.yml#L12)**    | Repositories list to configure
apt_ppas                                      | **[[]](molecule/ppa-package-install/converge.yml#L19)**    | PPA repositories to add
apt_force                                     | **false**                                                  | Force installs / removes
apt_install_recommends                        | **false**                                                  | Install recommended packages
apt_dpkg_options                              | **""**                                                     | Add dpkg options to apt command
apt_default_release                           | **""**                                                     | Set pin priorities (like apt -t)
apt_config_default                            | **[defaults/main.yml](defaults/main.yml#L16)**             | Defaut config for apt, every new config will be merge with it
apt_config                                    | **{}**                                                     | New config to set, it will be merge with apt_default_config
apt_config_additional_preformatted_config     | **''**                                                     | Additional preformatted config
apt_config_listchanges_mail                   | **null**                                                   | List changes mail
apt_config_unattended_upgrades_package_state  | **'auto'**                                                 | Unattended upgrades package state
apt_config_unattended_upgrades_timer_override | **null**                                                   | Unattended upgrades timer override
apt_config_listchanges_package_state          | **'auto'**                                                 | List changes package state

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

Install packages

```yaml
- name: bootstrap instance
  hosts: all
  tasks:
    - include_role:
        name: apt
      vars:
        - apt_packages:
          # latest packages
          - name: tree
          - name: python-pip
          # specific package version
          - name: vim=2:8.*
          # deb file
          - deb: "http://repo.zabbix.com/zabbix/6.1/{{ ansible_distribution | lower }}/pool/main/z/zabbix-release/zabbix-release_6.1-2+{{ ansible_distribution |lower }}{{ ansible_distribution_version }}_all.deb"ansible_distribution_release }}_all.deb
```

PPA package installation

```yaml
- name: ppa-package-install
  hosts: all
  become: true
  roles:
    - role: claranet.apt
  vars:
    apt_upgrade: true
    apt_ppas:
      # nginx ppa repo
      - repo: ppa:nginx/stable
        # not needed on ubuntu distribution
        codename: trusty
    apt_repositories_new:
      - types: deb # can be string or list
        urls: "https://deb.nodesource.com/node_18.x"
        suites: "{{ ansible_distribution_release | lower }}"
        components: "main"
        key: https://deb.nodesource.com/gpgkey/nodesource.gpg.key # can be url or content of file
    apt_packages:
      - name: nginx
      - name: nodejs
```

Do an upgrade

```yaml
- hosts: all
  vars:
    # could be safe | full | dist
    - apt_upgrade: true
  roles:
    - apt
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
