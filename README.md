# Ansible role - apt
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-apt?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-apt?style=flat-square)](https://github.com/claranet/ansible-role-apt/releases)
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

Name | Type | Description | Default
---------|----------|---------|---------
 apt_packages | list | packages list to install | []
 apt_repositories | list | repositories list to configure | []
 apt_keys | list | keys list to use with repositories | []
 apt_upgrade | string | do an upgrade (no, yes, safe, full, dist) | no
 apt_force | boolean | force installs / removes | no
 apt_autoremove | boolean | remove unused dependency packages | yes
 apt_install_recommends | boolean | install recommended packages | no
 apt_dpkg_options | string | add dpkg options to apt command | ""
 apt_default_release | string | set pin priorities (like apt -t) | ""

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

All these examples could be combined in one playbook


Testing
-------

###How to use it

Testing uses Molecule : https://molecule.readthedocs.io/en/latest/
```
cd ansible-role-apt
molecule test -s name_of_scenario

```

###Scenarios created for ansible-role-apt

- basic-package-install : to check if the role has successfully installed the simple/with dependencies package .
- non-free_contrib_repo : to check if the role has successfully installed the package from a non-free and contrib repository also a dotdeb key and repo .
- ppa-package-install   : to check if the role has successfully installed the package from a ppa repo .
- repo-package-install  : to check if the role has successfully installed the package from a custom repository ( zabbix ) .
- spec-version-package-install : to check if the role has successfully installed the package with a specific version .

Molecule test this role on these docker images :
------------------------------------------------

- Debian 9
- Debian 10
- Debian 11
- Ubuntu 14.04
- Ubuntu 16.04
- Ubuntu 18.04


## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
