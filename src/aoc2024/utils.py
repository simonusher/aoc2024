_INPUTS_DIR = "data"
_INPUT_FILE_NAME = "input.txt"
_EXAMPLE_FILE_NAME = "example.txt"


def _load_input_file(puzzle_num: int, file_name: str) -> str:
    with open(f"{_INPUTS_DIR}/{puzzle_num}/{file_name}", "rt") as f:
        return f.read()


def load_input(puzzle_num: int) -> str:
    return _load_input_file(puzzle_num, _INPUT_FILE_NAME)


def load_example(puzzle_num: int) -> str:
    return _load_input_file(puzzle_num, _EXAMPLE_FILE_NAME)
