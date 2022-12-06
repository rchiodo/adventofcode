import os

def read_input(input_file: str) -> list[str]:
    input_txt = os.path.join(os.path.dirname(__file__), input_file)
    lines: list[str] = []

    with open(input_txt, "r") as f:
        lines = f.read().splitlines()
    return lines
