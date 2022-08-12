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

Variable | Default value | Description
---------|----------|---------|---------
apt_upgrade                  | **false**   | do an upgrade (no, yes, safe, full, dist)
apt_autoremove               | **true**    | remove packages that are no longer needed for dependencies
apt_packages                 | **[]**      | packages list to install
apt_repositories             | **[]**      | repositories list to configure
apt_keys                     | **[]**      | keys list to use with external repositories
apt_force                    | **false**   | force installs / removes
apt_install_recommends       | **false**   | install recommended packages
apt_dpkg_options             | **""**      | add dpkg options to apt command
apt_default_release          | **""**      | set pin priorities (like apt -t)
aptconfig_default            | **{}**      | Hash of apt options

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

Add repositories and install packages from those

```yaml
- name: bootstrap instance
  hosts: all
  tasks:
    - include_role:
        name: apt
      vars:
        - apt_repositories:
          # contrib repo
          - repo: deb http://deb.debian.org/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} contrib
          # non-free repo
          - repo: deb http://deb.debian.org/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} non-free
          # nginx ppa repo
          - repo: ppa:nginx/stable
            # not needed on ubuntu distribution
            codename: trusty
        - apt_keys:
          # dotdeb key
          - url: https://www.dotdeb.org/dotdeb.gpg
        - apt_packages:
          # package from contrib repo
          - name: java-package
          # package from non-free repo
          - name: album
          # package from dotdeb repo
          - name: php7.0
          # package from nginx ppa repo
          - name: nginx
```

Do an upgrade

```yaml
- hosts: localhost
  tasks:
    - include_role:
        name: apt
      vars:
        # could be safe | full | dist
        - apt_upgrade: yes
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
