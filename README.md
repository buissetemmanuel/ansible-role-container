Ansible Role Container
=========

**Podman Rootless Container** installation from scratch.

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml) for available variables.

If you whant to manage `packages`, `users` or `systems`, use one or more variable listed below:

    packages_managed: false
    users_managed: false
    systems_managed: false

> See [molecule/default/vars/container.yml](molecule/default/vars/container.yml) for example variables.

Example Playbook
----------------

See [molecule/default/converge.yml](molecule/default/converge.yml) for playbook and inventory example.

License
-------

[mit license]: https://img.shields.io/badge/License-MIT-blue.svg
[![mit license]](LICENSE.md)

Author Information
------------------

[email]: https://img.shields.io/badge/BUISSET-Emmanuel-orange.svg
[![email]](mailto:emmanue@buisset.ch)
