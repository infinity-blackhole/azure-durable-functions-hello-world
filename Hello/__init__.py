# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import ray
from ray import workflow


@ray.remote
def hello(name: str) -> str:
    return f"Hello {name} from Ray!"


def main(name: str, workflow_id: str):
    workflow.run_async(hello.bind(name), workflow_id=workflow_id)
