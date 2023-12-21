# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2023 IBM Corp. All rights reserved.
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

from ari_core.models import RiskAnnotation, TaskCall, DefaultRiskType, OutboundTransferDetail
from ari_core.annotators.module_annotator_base import ModuleAnnotator, ModuleAnnotatorResult


class URIAnnotator(ModuleAnnotator):
    fqcn: str = "ansible.builtin.uri"
    enabled: bool = True

    def run(self, task: TaskCall) -> ModuleAnnotatorResult:
        method = task.args.get("method")

        annotations = []
        if method in ["PUT", "POST", "PATCH"]:
            url = task.args.get("url")
            body = task.args.get("body")
            annotation = RiskAnnotation.init(
                risk_type=DefaultRiskType.OUTBOUND,
                detail=OutboundTransferDetail(_dest_arg=url, _src_arg=body),
            )
            annotations.append(annotation)
        return ModuleAnnotatorResult(annotations=annotations)
