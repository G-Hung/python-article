from typing import Tuple


# example: add function
def add(a: int = 1, b: int = 2) -> int:
    return a + b


# example: give type hint more meaningful name
Seconds = float


def launch_task(delay: Seconds):
    pass


# example: give type hint more meaningful name
Client = Tuple[int, str]


def process_clients(clients: list[Client]):
    print(clients)
    pass
