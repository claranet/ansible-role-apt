Role Name
=========

Install packages and add repositories on apt based distributions :

Requirements
------------

Ansible version >= 2.1

Role Variables
--------------

Name | Type | Description | Default
---------|----------|---------|---------
 apt_packages | list | package name to install | []
 apt_repositories | list | package name to install | []
 apt_keys | list | package name to install | []
 apt_upgrade | string | package name to install | no
 apt_force | boolean | package name to install | no
 apt_autoremove | boolean | package name to install | yes
 apt_install_recommends | boolean | package name to install | no
 apt_dpkg_options | string | package name to install | ""
 apt_default_release | string | package name to install | ""

Dependencies
------------

No dependencies

Example Playbook
----------------

Install packages

```
---
- hosts: localhost
  roles:
    - role: apt
  vars:
    - apt_packages:
      # latest packages
      - name: tree
      - name: python-pip
      # specific package version
      - name: vim=2:8.*
      # deb file
      - deb: http://repo.zabbix.com/zabbix/3.2/{{ ansible_distribution | lower }}/pool/main/z/zabbix-release/zabbix-release_3.2-1+{{ ansible_distribution_release }}_all.deb
```

Add repositories and install packages from those 

```
---
- hosts: localhost
  roles:
    - role: apt
  vars:
    - apt_repositories:
      # contrib repo
      - repo: deb http://deb.debian.org/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} contrib
      # non-free repo
      - repo: deb http://deb.debian.org/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} non-free
      # dotdeb repo
      - repo: deb http://packages.dotdeb.org {{ ansible_distribution_release }} all
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
      - name: rar
      # package from dotdeb repo
      - name: php7.0
      # package from nginx ppa repo
      - name: nginx
```

Do an upgrade

```
---
- hosts: localhost
  roles:
    - role: apt
  vars:
    # could be safe | full | dist
    - apt_upgrade: yes
```

All these examples could be combined in one playbook
