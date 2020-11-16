import importlib
import os.path
import sys


class Tests:
    def __init__(self, file_name, file_lines, method_name=""):
        self.module_name = os.path.splitext(file_name)[0]
        importlib.invalidate_caches()
        if os.path.isfile(file_name):
            self.module = importlib.import_module(self.module_name)

        self.file_lines = file_lines
        self.method_name = method_name

    def test_comments_exist(self):
        for line in self.file_lines:
            if "#" in line:
                return True
        return False

    def function_test1(self, desired_value):
        local = {}
        try:
            # exec(f"ret = self.module.{self.method_name}", globals(), local)
            # ret = local.get('ret')
            func = getattr(self.module, self.method_name)
            ret = func()
            return ret == desired_value
        except Exception:
            print("Exception:", sys.exc_info()[1])
            return False

    def run_tests(self):
        print("test_comments_exist result: ", self.test_comments_exist())
        print("function_test1 result: ", self.function_test1("abc"))
