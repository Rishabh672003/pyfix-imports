def get_file_text(filename: str) -> str:
    output = ""
    try:
        with open(filename, "r") as file:
            for i in file:
                output += i

    except Exception as e:
        print(e)

    return output.lstrip().rstrip()


def write_to_file(filename: str, text: str):
    try:
        with open(filename, "w") as file:
            file.write(text)
    except Exception:
        return None
