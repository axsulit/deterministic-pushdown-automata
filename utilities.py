from ast import literal_eval


def get_machine(path):
    with open(path, 'r') as fptr:
        stream = fptr.read()
        lines = stream.splitlines()
        stream = "\n".join(line for line in lines if (not line.startswith(';') and not line == ""))
        return parse_str(stream)


# Parses string to the internal machine definition
def parse_str(stream):
    lines = stream.splitlines()
    return [literal_eval(strings) for strings in lines]
