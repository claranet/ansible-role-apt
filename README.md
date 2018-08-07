apt
===

Install packages and add repositories on apt based distributions :

Requirements
------------

Ansible version >= 2.3

Role Variables
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

- Debian 7
- Debian 8
- Debian 9
- Ubuntu 14.04
- Ubuntu 16.04  
- Ubuntu 18.04
