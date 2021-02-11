# wpninfra.fluent-bit

[![Build Status](https://github.com/josesolis2201/ansible-role-fluent-bit/workflows/CI/badge.svg)](https://github.com/josesolis2201/ansible-role-fluent-bit/actions)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-ansible-role-fluent-bit.vim-blue.svg)](https://galaxy.ansible.com/wpninfra/fluent-bit/)

An [ansible role](https://galaxy.ansible.com/wpninfra/fluent-bit) to install and configure fluent-bit

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Dependencies

By default this role does not depend on any external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

## Example Playbook

- hosts: servers
  roles:
     - role: wpninfra.fluent-bit
       fluent_bit_package_state: latest

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):

  * Ubuntu Focal
  * Ubuntu Bionic
  * Ubuntu Xenial
  * CentOS 7
  * Debian Buster

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
