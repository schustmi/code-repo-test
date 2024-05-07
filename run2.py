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
from zenml.config import DockerSettings


@step
def step_1() -> int:
    """Docstring."""
    return 99


@step(settings={"docker": DockerSettings(environment={"key": "value"})})
def step_2(number: int) -> int:
    return number * 2


@step(step_operator="sagemaker")
def step_3() -> None:
  return


@pipeline(enable_cache=False)
def code_repo_pipeline():
    step_2(step_1())
    step_3()


if __name__ == "__main__":
    code_repo_pipeline()
