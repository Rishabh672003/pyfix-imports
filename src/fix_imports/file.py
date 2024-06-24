def file_handling(filename) -> str:
    output = ""
    try:
        with open(filename, "r") as file:
            for i in file:
                output += i

    except Exception as e:
        print(e)

    return output.lstrip().rstrip()
