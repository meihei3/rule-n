pattern = {
    "111": "0",
    "110": "0",
    "101": "0",
    "100": "1",
    "011": "1",
    "010": "1",
    "001": "1",
    "000": "0",
}


def print_line(line: str):
    print(line.replace("0", " ").replace("1", "■"))


def generate(line: str) -> str:
    tmp_line = "0" + line + "0"
    return "".join([pattern[tmp_line[i-1:i+2]] for i in range(1, len(line)+1)])


if __name__ == "__main__":
    line = "00000000000000000000000000000000100000000000000000000000000000000"
    for i in range(30):
        print_line(line)
        line = generate(line)
