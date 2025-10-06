import sys


def print_args(args):
    for arg in args:
        print(arg)


def write_to_file(filepath, *lines):
    if len(lines) == 0:
        print("No Content Provided")
    with open(filepath, "w") as file:
        for line in lines:
            file.write(line)
            file.write("\n")


def read_file(filepath):
    with open(filepath, "r") as file:
        print(file.read())


def flags(args):
    flags = ["-p", "-i", "-h", "-w", "-r"]
    if args[1] in flags:
        selected_flag = args[1]
    else:
        return False
    if selected_flag == "-p":
        for arg in args[2:]:
            print(arg)
    elif selected_flag == "-i":
        print("Hello World")
    elif selected_flag == "-h":
        print("""Valid flags:
-p : prints out all the command line arguments after the -p
-i : prints "Hello World"
-h : prints out a help command""")
    elif selected_flag == "-w":
        write_to_file(args[2], *args[3:])
    elif selected_flag == "-r":
        read_file(args[2])
    return True


if __name__ == "__main__":
    if not flags(sys.argv):
        print_args(sys.argv)
