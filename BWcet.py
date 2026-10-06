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
