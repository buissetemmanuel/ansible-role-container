#!/usr/bin/python
# Copyright (c) 2018 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
  module: podman_manifest
  author:
      - BUISSET Emmanuel (@buissetemmanuel)
  short_description: Create and manipulate manifest lists and image indexes
  notes: []
  description:
      - The podman manifest command provides subcommands which can be used to create a working Docker manifest list or OCI image index.
  options:
    name:
      description:
        - List name or index name. It may contain a tag using the format C(image:tag).
      required: True
      type: str
    executable:
      description:
        - Path to C(podman) executable if it is not in the C($PATH) on the machine running C(podman).
      default: 'podman'
      type: str
    ca_cert_dir:
      description:
        - Path to directory containing TLS certificates and keys to use.
      type: 'path'
    tag:
      description:
        - Tag of the image to pull, push, or delete.
      default: "latest"
      type: str
    inspect:
      description: Display a manifest list or image index.
      default: True
      type: bool
    validate_certs:
      description:
        - Require HTTPS and validate certificates when pulling or pushing. Also used during build if a pull or push is necessary.
      type: bool
      aliases:
        - tlsverify
        - tls_verify
    password:
      description:
        - Password to use when authenticating to remote registries.
      type: str
    username:
      description:
        - username to use when authenticating to remote registries.
      type: str
    auth_file:
      description:
        - Path to file containing authorization credentials to the remote registry.
      aliases:
        - authfile
      type: path
'''

EXAMPLES = r"""
- name: Inspect an image to the remote registry
  podman_manifest:
    name: quay.io/bitnami/wildfly
- name: Inspect a specific version of an image to the remote registry
  podman_manifest:
    name: redis
    tag: 4
- name: Inspect an image using username and password
  podman_manifest:
    name: nginx
    username: bugs
    password: "{{ vault_registry_password }}"
- name: Inspect an image to multiple remote registries
  podman_manifest:
    name: "{{ item }}"
    auth_file: /etc/containers/auth.json
    loop:
    - quay.io/acme/nginx
    - docker.io/acme/nginx
"""

RETURN = r"""
  image:
    description:
      - Image inspection results for the image from remote registry.
    returned: success
    type: dict
    sample: [
      {
        "Annotations": {},
        "Architecture": "amd64",
        "Author": "",
        "Comment": "from Bitnami with love",
        "ContainerConfig": {
          "Cmd": [
            "/run.sh"
          ],
          "Entrypoint": [
            "/app-entrypoint.sh"
          ],
          "Env": [
            "PATH=/opt/bitnami/java/bin:/opt/bitnami/wildfly/bin:/opt/bitnami/nami/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "IMAGE_OS=debian-9",
            "NAMI_VERSION=1.0.0-1",
            "GPG_KEY_SERVERS_LIST=ha.pool.sks-keyservers.net",
            "TINI_VERSION=v0.13.2",
            "TINI_GPG_KEY=595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7",
            "GOSU_VERSION=1.10",
            "GOSU_GPG_KEY=B42F6819007F00F88E364FD4036A9C25BF357DD4",
            "BITNAMI_IMAGE_VERSION=16.0.0-debian-9-r27",
            "BITNAMI_PKG_CHMOD=-R g+rwX",
            "BITNAMI_PKG_EXTRA_DIRS=/home/wildfly",
            "HOME=/",
            "BITNAMI_APP_NAME=wildfly",
            "NAMI_PREFIX=/.nami",
            "WILDFLY_HOME=/home/wildfly",
            "WILDFLY_JAVA_HOME=",
            "WILDFLY_JAVA_OPTS=",
            "WILDFLY_MANAGEMENT_HTTP_PORT_NUMBER=9990",
            "WILDFLY_PASSWORD=bitnami",
            "WILDFLY_PUBLIC_CONSOLE=true",
            "WILDFLY_SERVER_AJP_PORT_NUMBER=8009",
            "WILDFLY_SERVER_HTTP_PORT_NUMBER=8080",
            "WILDFLY_SERVER_INTERFACE=0.0.0.0",
            "WILDFLY_USERNAME=user",
            "WILDFLY_WILDFLY_HOME=/home/wildfly",
            "WILDFLY_WILDFLY_OPTS=-Dwildfly.as.deployment.ondemand=false"
          ],
          "ExposedPorts": {
            "8080/tcp": {},
            "9990/tcp": {}
          },
          "Labels": {
            "maintainer": "Bitnami <containers@bitnami.com>"
          },
          "User": "1001"
        },
        "Created": "2019-04-10T05:48:03.553887623Z",
        "Digest": "sha256:5a8ab28e314c2222de3feaf6dac94a0436a37fc08979d2722c99d2bef2619a9b",
        "GraphDriver": {
          "Data": {
            "LowerDir": "/var/lib/containers/storage/overlay/142c1beadf1bb09fbd929465ec98c9dca3256638220450efb4214727d0d0680e/diff:/var/lib/containers/s",
            "MergedDir": "/var/lib/containers/storage/overlay/9aa10191f5bddb59e28508e721fdeb43505e5b395845fa99723ed787878dbfea/merged",
            "UpperDir": "/var/lib/containers/storage/overlay/9aa10191f5bddb59e28508e721fdeb43505e5b395845fa99723ed787878dbfea/diff",
            "WorkDir": "/var/lib/containers/storage/overlay/9aa10191f5bddb59e28508e721fdeb43505e5b395845fa99723ed787878dbfea/work"
          },
          "Name": "overlay"
        },
        "History": [
          {
            "comment": "from Bitnami with love",
            "created": "2019-04-09T22:27:40.659377677Z"
          },
          {
            "created": "2019-04-09T22:38:53.86336555Z",
            "created_by": "/bin/sh -c #(nop)  LABEL maintainer=Bitnami <containers@bitnami.com>",
            "empty_layer": true
          },
          {
            "created": "2019-04-09T22:38:54.022778765Z",
            "created_by": "/bin/sh -c #(nop)  ENV IMAGE_OS=debian-9",
            "empty_layer": true
          },
        ],
        "Id": "ace34da54e4af2145e1ad277005adb235a214e4dfe1114c2db9ab460b840f785",
        "Labels": {
          "maintainer": "Bitnami <containers@bitnami.com>"
        },
        "ManifestType": "application/vnd.docker.distribution.manifest.v1+prettyjws",
        "Os": "linux",
        "Parent": "",
        "RepoDigests": [
          "quay.io/bitnami/wildfly@sha256:5a8ab28e314c2222de3feaf6dac94a0436a37fc08979d2722c99d2bef2619a9b"
        ],
        "RepoTags": [
          "quay.io/bitnami/wildfly:latest"
        ],
        "RootFS": {
          "Layers": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
          ],
          "Type": "layers"
        },
        "Size": 466180019,
        "User": "1001",
        "Version": "18.09.3",
        "VirtualSize": 466180019
      }
    ]
"""
import json
import re
import shlex

from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule


class PodmanManifestManager(object):

    def __init__(self, module, results):

        super(PodmanManifestManager, self).__init__()

        self.manifest = 'manifest'

        self.module = module
        self.results = results
        self.executable = self.module.get_bin_path(module.params.get('executable'), required=True)
        self.name = self.module.params.get('name')
        self.tag = self.module.params.get('tag')
        self.inspect = self.module.params.get('inspect')
        self.validate_certs = self.module.params.get('validate_certs')
        self.auth_file = self.module.params.get('auth_file')
        self.username = self.module.params.get('username')
        self.password = self.module.params.get('password')
        self.ca_cert_dir = self.module.params.get('ca_cert_dir')

        repo, repo_tag = parse_repository_tag(self.name)
        if repo_tag:
            self.name = repo
            self.tag = repo_tag

        self.image_name = '{name}:{tag}'.format(name=self.name, tag=self.tag)

        if self.inspect:
            self.inspect_image()

    def _run(self, args, expected_rc=0, ignore_errors=False):
        cmd = " ".join([self.executable]
                       + [to_native(i) for i in args])
        self.module.log("PODMAN-MANIFEST-DEBUG: %s" % cmd)
        self.results['podman_actions'].append(cmd)
        return run_podman_command(
            module=self.module,
            executable=self.executable,
            args=args,
            expected_rc=expected_rc,
            ignore_errors=ignore_errors)

    def inspect_image(self, image_name=None):
        if image_name is None:
            image_name = self.image_name

        args = [self.manifest, 'inspect', image_name]

        if self.validate_certs is not None:
            if self.validate_certs:
                args.append('--tls-verify')
            else:
                args.append('--tls-verify=false')
        if self.auth_file is not None:
            if self.auth_file:
                args.append('--authfile', self.auth_file)
        rc, image_data, err = self._run(args)
        if len(image_data) > 0:
            return json.loads(image_data)
        else:
            return None


def run_podman_command(module, executable='podman', args=None, expected_rc=0, ignore_errors=False):
    if not isinstance(executable, list):
        command = [executable]
    if args is not None:
        command.extend(args)
    rc, out, err = module.run_command(command)
    if not ignore_errors and rc != expected_rc:
        module.fail_json(
            msg='Failed to run {command} {args}: {err}'.format(
                command=command, args=args, err=err))
    return rc, out, err

def parse_repository_tag(repo_name):
    parts = repo_name.rsplit('@', 1)
    if len(parts) == 2:
        return tuple(parts)
    parts = repo_name.rsplit(':', 1)
    if len(parts) == 2 and '/' not in parts[1]:
        return tuple(parts)
    return repo_name, None


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            tag=dict(type='str', default='latest'),
            inspect=dict(type='bool', default=True),
            validate_certs=dict(type='bool', aliases=['tlsverify', 'tls_verify']),
            executable=dict(type='str', default='podman'),
            auth_file=dict(type='path', aliases=['authfile']),
            username=dict(type='str'),
            password=dict(type='str', no_log=True),
            ca_cert_dir=dict(type='path'),
        ),
        supports_check_mode=True,
        required_together=(
            ['username', 'password'],
        ),
        mutually_exclusive=(
            ['auth_file', 'username'],
            ['auth_file', 'password'],
        ),
    )

    results = dict(
        changed=False,
        actions=[],
        podman_actions=[],
        image={},
    )

    PodmanManifestManager(module, results)
    module.exit_json(**results)


if __name__ == '__main__':
    main()
