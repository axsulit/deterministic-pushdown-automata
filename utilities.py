from ast import literal_eval


def get_machine(path):
    with open(path, 'r') as fptr:
        stream = fptr.read()
        lines = stream.splitlines()
        stream = "\n".join(line for line in lines if (not line.startswith(';') and not line == ""))
        return parse(stream)


# Parses string to the internal machine definition
def parse(stream):
    lines = stream.splitlines()
    defs = [literal_eval(strings) for strings in lines]
    return defs
