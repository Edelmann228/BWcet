from dataclasses import dataclass


@dataclass
class Operation:
    name: str
    operation_type: str
    memory_accesses: int
    branches: int


@dataclass
class ProcessorModel:
    base_cost: int
    cache_miss_penalty: int
    branch_misprediction_penalty: int
    deadline: int
def best_case(operation, processor):
    return processor.base_cost
def worst_case(operation, processor):
    memory_penalty = operation.memory_accesses * processor.cache_miss_penalty
    branch_penalty = operation.branches * processor.branch_misprediction_penalty

    return processor.base_cost + memory_penalty + branch_penalty
def bcet(operations, processor):
    total = 0

    for operation in operations:
        total += best_case(operation, processor)

    return total