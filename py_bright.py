import sys
import io
import importlib
import os


def read_file_content(file):
    if os.path.isfile(file):
        with open(file, "r") as file_stream:
            content = file_stream.readlines()
        return content
    return ""


# args:
# [0] = Name of running file
# [1] = Name of file to test
# [2] = Name of tests file
def main(args):
    if len(args) >= 3:
        try:
            module = importlib.import_module(os.path.splitext(args[2])[0])
        except Exception:
            print("Exception:", sys.exc_info()[1])
    if len(args) >= 2:
        file_lines = read_file_content(args[1])
        test = module.Tests(args[1], file_lines, "foo")
        # test = module.Tests(args[1], file_lines)
    test.run_tests()


if __name__ == '__main__':
    main(sys.argv)


