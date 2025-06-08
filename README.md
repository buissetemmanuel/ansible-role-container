[![MOLECULE LINT](https://github.com/buissetemmanuel/ansible-role-container/actions/workflows/molecule-lint.yml/badge.svg)](https://github.com/buissetemmanuel/ansible-role-container/actions/workflows/molecule-lint.yml)
[![RELEASE](https://github.com/buissetemmanuel/ansible-role-container/actions/workflows/release.yml/badge.svg)](https://github.com/buissetemmanuel/ansible-role-container/actions/workflows/release.yml)

Ansible Role Container
=========

**Podman Rootless Container** installation from scratch.

Goal
--------------

- manage packages if needed with role [ansible-role-package](https://github.com/buissetemmanuel/ansible-role-package)
- manage users if needed with role [ansible-role-user](https://github.com/buissetemmanuel/ansible-role-user)
- 2 users include group and 1 group to access logs
- owner of files is not the user that manage systemd service for pod
- generate kubernetes yaml consume by `podman play kube...`
- all update restart the service pod
- unshare if needed

Extra
--------------

I create a module [library/podman_manifest.py](library/podman_manifest.py) to check image in remote registry without to pull image.

Requirements
--------------
![ansible](https://img.shields.io/badge/ansible-2.12.3-green.svg)
![molecule](https://img.shields.io/badge/molecule-4.0.4-green.svg)
![vagrant](https://img.shields.io/badge/vagrant-2.0.0-green.svg)

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml) for available variables.

> See [molecule/default/vars/container.yml](molecule/default/vars/container.yml) for example variables.

Example Playbook
----------------

See [molecule/default/converge.yml](molecule/default/converge.yml) for playbook and inventory example.

TODO
-------
- manage Deployment
- manage PersistentVolumeClaim
- manage ConfigMap
- manage Secret

> Based on [podman-kube-play](https://docs.podman.io/en/latest/markdown/podman-kube-play.1.html)

- add pipeline with [Github actions](https://github.com/features/actions)
- add lint with [ansible-lint](https://ansible-lint.readthedocs.io/)

License
-------

[mit license]: https://img.shields.io/badge/License-MIT-blue.svg
[![mit license]](LICENSE.md)

Author Information
------------------

[email]: https://img.shields.io/badge/@-emmanuel@buisset.ch-orange.svg
[![email]](mailto:emmanue@buisset.ch)
