# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import ray

ray.init()


@ray.remote
def hello(name: str) -> str:
    return f"Hello {name} from Ray!"


def main(name: str):
    hello_object_ref = hello.remote(name)
    if hello_object_ref is None:
        raise TypeError("hello_object_ref is None")
    return ray.get(hello_object_ref)
