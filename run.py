#  Copyright (c) ZenML GmbH 2021. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

from zenml import step, pipeline
import sys
from pathlib import Path

import zenml
from zenml.config import DockerSettings


zenml_git_root = Path(zenml.__file__).parents[2]

docker_settings =  DockerSettings(
    dockerfile=str(zenml_git_root / "docker" / "zenml-dev.Dockerfile"),
    build_context_root=str(zenml_git_root),
    build_options={
        "platform": "linux/amd64",
        "buildargs": {
            "PYTHON_VERSION": f"{sys.version_info.major}.{sys.version_info.minor}"
        },
    },
)


@step
def step_1() -> int:
    """Docstring."""
    return 99


@step(enable_cache=True)
def step_2(number: int) -> int:
    return number * 2


@pipeline(
    enable_cache=False,
    settings={
        "docker": docker_settings,
    },
)
def code_repo_pipeline():
    step_2(step_1())


if __name__ == "__main__":
    code_repo_pipeline()
