# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2024 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from .keyutil import get_obj_info_by_key


if __name__ == "__main__":
    keys = [
        "task role:geerlingguy.gitlab#taskfile:tasks/main.yml#task:[0]",
        "taskfile role:geerlingguy.gitlab#taskfile:tasks/main.yml",
        "role role:geerlingguy.gitlab",
        "play collection:debops.debops#playbook:playbooks/virt/dnsmasq-persistent_paths.yml#play:[0]",
        "playbook" " collection:debops.debops#playbook:playbooks/sys/cryptsetup-plain.yml",
        "module collection:debops.debops#module:debops.debops.apache2_module",
    ]
    for k in keys:
        info = get_obj_info_by_key(k)
        print(json.dumps(info, indent=2))
