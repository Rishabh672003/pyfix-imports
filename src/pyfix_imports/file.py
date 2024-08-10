import sys


def get_file_text(filename: str) -> str:
    try:
        with open(filename, "r") as file:
            output = file.read().lstrip()
    except Exception as e:
        print(f"Error occured while reading a file: {e}", file=sys.stderr)
        sys.exit(1)

    return output


def write_to_file(filename: str, text: str):
    try:
        with open(filename, "w") as file:
            file.write(text)
    except Exception as e:
        print(f"Error occured while writing to a file: {e}", file=sys.stderr)
        sys.exit(1)
