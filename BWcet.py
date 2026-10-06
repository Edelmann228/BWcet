from dataclasses import dataclass


import json

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

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    processor_data = data["processor"]

    processor = ProcessorModel(
        base_cost=processor_data["base_cost"],
        cache_miss_penalty=processor_data["cache_miss_penalty"],
        branch_misprediction_penalty=processor_data[
            "branch_misprediction_penalty"
        ],
        deadline=processor_data["deadline"]
    )

    operations = []

    for item in data["operations"]:
        operation = Operation(
            name=item["name"],
            operation_type=item["type"],
            memory_accesses=item["memory_accesses"],
            branches=item["branches"]
        )

        operations.append(operation)

    return processor, operations

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
def wcet(operations, processor):
    total = 0

    for operation in operations:
        total += worst_case(operation, processor)

    return total
def nondeterminism_ratio(operations, processor):
    best_time = bcet(operations, processor)
    worst_time = wcet(operations, processor)

    if best_time == 0:
        return 0.0

    return worst_time / best_time
def source_breakdown(operations, processor):
    memory = 0
    branches = 0

    for operation in operations:
        memory += operation.memory_accesses * processor.cache_miss_penalty
        branches += operation.branches * processor.branch_misprediction_penalty

    return memory, branches
def print_operations(operations, processor):
    print()
    print(
        f"{'Операция':<28}"
        f"{'Тип':<22}"
        f"{'Память':<10}"
        f"{'Ветвления':<12}"
        f"{'Лучшее':<10}"
        f"{'Худшее':<10}"
    )

    print("-" * 92)

    for operation in operations:
        best = best_case(operation, processor)
        worst = worst_case(operation, processor)

        print(
            f"{operation.name:<28}"
            f"{operation.operation_type:<22}"
            f"{operation.memory_accesses:<10}"
            f"{operation.branches:<12}"
            f"{best:<10}"
            f"{worst:<10}"
        )
