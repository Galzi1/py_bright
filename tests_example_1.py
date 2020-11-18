import importlib
import os.path
import sys
from subprocess import Popen, PIPE, STDOUT, CalledProcessError


class Tests:
    def __init__(self, file_name, file_lines, method_name=""):
        self.file_name = file_name

        if method_name != "":
            try:
                self.module_name = os.path.splitext(file_name)[0]
                importlib.invalidate_caches()
                if os.path.isfile(file_name):
                    self.module = importlib.import_module(self.module_name)
            except Exception:
                print("Exception Tests.__init__", sys.exc_info()[1])

        self.file_lines = file_lines
        self.method_name = method_name

    def test_comments_exist(self):
        for line in self.file_lines:
            if "#" in line:
                return True
        return False

    def function_test1(self, correct_output, inputs=[]):
        if self.method_name == "":
            if type(inputs) is not list:
                 inputs = [inputs]
            out = []
            try:
                p = Popen(["python", self.file_name], stdin=PIPE, stdout=PIPE, stderr=PIPE)
                for inp in inputs:
                    out_encoded = p.communicate(input=inp.encode('utf-8'))[0]
                    out_decoded = out_encoded.decode('utf-8').strip()
                    out.append(out_decoded)
            except Exception:
                print("Exception in test1:", sys.exc_info()[1])
                return False

            if out is None or len(out) == 0:
                return False
            else:
                return out == correct_output
        else:
            try:
                func = getattr(self.module, self.method_name)
                if inputs is None or len(inputs) == 0:
                    ret = func()
                else:
                    if type(inputs) is not list:
                        inputs = [inputs]
                    ret = func(*inputs)
                return ret == correct_output
            except Exception:
                print("Exception in test1:", sys.exc_info()[1])
                return False

    def run_tests(self):
        print("test_comments_exist result: ", self.test_comments_exist())
        print("function_test1 result: ", self.function_test1("abcefg", ["efg"]))
        # print("function_test1 result: ", self.function_test1(["4"], "3"))
