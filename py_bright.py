import sys
import io
import importlib
import os


def read_file_content(file):
    with open(file, "r") as myfile:
        content = myfile.readlines()
    return content


# args:
# [0] = Name of running file
# [1] = Name of file to test
# [2] = Name of tests file
def main(args):
    if len(args) == 3:
        module = importlib.import_module(os.path.splitext(args[2])[0])
        file_lines = read_file_content(args[1])
        test = module.Tests(args[1], file_lines, "foo")
        test.run_tests()


if __name__ == '__main__':
    main(sys.argv)


