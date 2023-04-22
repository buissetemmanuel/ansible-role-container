#!/usr/bin/python
# Copyright (c) 2018 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
  module: podman_image_exists
  author:
      - BUISSET Emmanuel (@buissetemmanuel)
  short_description: Check image exists on guest local registry
  notes: []
  description:
      - The podman image exists command check if image already exists on guest local registry
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
    tag:
      description:
        - Tag of the image to pull, push, or delete.
      default: "latest"
      type: str
'''

EXAMPLES = r"""
- name: Gather info on a specific image
  podman_image_exists:
    name: nginx
- name: Gather info on a speific image:tag
  podman_image_exists:
    name: nginx
    tag: 1.22.1
"""

RETURN = r"""
images:
    description: info from all or specified images
    returned: always
    type: dict
    sample: [
        {
        .....
        }
    ]
"""

import json

from ansible.module_utils.basic import AnsibleModule


def image_exists(module, executable, name):
    command = [executable, 'image', 'exists', name]
    rc, out, err = module.run_command(command)
    if rc == 1:
        return False
    elif 'Command "exists" not found' in err:
        # The 'exists' test is available in podman >= 0.12.1
        command = [executable, 'image', 'ls', '-q', name]
        rc2, out2, err2 = module.run_command(command)
        if rc2 != 0:
            return False
    return True

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
            executable=dict(type='str', default='podman'),
            name=dict(type='str', required=True),
            tag=dict(type='str', default='latest')
        ),
        supports_check_mode=True,
    )

    executable = module.params['executable']
    name = module.params.get('name')
    tag = module.params.get('tag')
    executable = module.get_bin_path(executable, required=True)

    repo, repo_tag = parse_repository_tag(name)
    if repo_tag:
        name = repo
        tag = repo_tag

    image_name = '{image_name}:{image_tag}'.format(image_name=name, image_tag=tag)

    result = image_exists(module, executable, image_name)

    results = dict(
        changed=False,
        image_exists=result
    )

    module.exit_json(**results)


if __name__ == '__main__':
    main()
