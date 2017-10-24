Role Name
=========

Install packages, manage repository, configure apt for debian based distributions :

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

Name | Type | Description | Default
---------|----------|---------|---------
 pkg | list | package name to install | ""

Dependencies
------------

No dependencies

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
---
- hosts: localhost
  roles:
    - { role: apt, package_name: ['nginx','curl'] }
```
