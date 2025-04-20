from global_tools.check.check import Check
from typing import Callable, Any

from global_tools.cprint.cprint import CPrint


class AGDPTest:
    def __init__(self, func: Callable[..., Any], assert_utils: Callable[..., Any]):
        """
        This class can be used to agdp_test functions one by one or using its static methods like show_test_results to agdp_test
        more.
        """
        Check.check_func(func)
        self.assert_utils = assert_utils
        self.func = func
        self.start_test_tool()
        CPrint(f"Assert result: {assert_utils(func)}", "warning")
        self.end_test_tool()

    def start_test_tool(self):
        """
        Used when Test is instantiated to announce the start of the agdp_test.
        """
        CPrint(f"BEGIN TEST : {self.func.__name__}", "info")
        CPrint(f"Expected result : {self.assert_utils.__name__}", "warning")

    def end_test_tool(self):
        """
        Used when Test is instantiated to announce the end of the agdp_test.
        """
        CPrint(f"END TEST : {self.func.__name__}", "info")

    @staticmethod
    def show_tests_results(tests_results: list[dict]):
        """
        This static method is used to display multiple tests' results with the amount of succeed, failed and total.
        Args:
            tests_results (list[dict]): Each dict is a combination of a agdp_test function name and its result. {"name":
            function_name, "result": function()}
        """
        if not isinstance(tests_results, list):
            raise TypeError('Tests results must be a list of dict.')

        for test_dict in tests_results:
            if not isinstance(test_dict, dict):
                raise TypeError('Test result must be a boolean.')
            if not isinstance(test_dict["name"], str) or len(test_dict["name"]) == 0:
                raise TypeError('Test dict must contains a string name.')
            if not isinstance(test_dict["result"], bool):
                raise TypeError('Test dict must contains a bool res.')

        tests_succeed = 0
        tests_failed = 0
        tests_qty = len(tests_results)
        i = 0

        CPrint.divider("Begin tests", True)
        for test in tests_results:
            i += 1
            if test["result"]:
                tests_succeed += 1
                CPrint(f"agdp_test #{i} {test['name']} done!", "info")
                CPrint("agdp_test succeed !", "success")
            else:
                tests_failed += 1
                CPrint(f"agdp_test #{i} {test['name']} done!", "info")
                CPrint("agdp_test failed !", "error")
            CPrint.line_break()
        CPrint.divider("Final results")
        CPrint(f"tests passed: {tests_succeed}/{tests_qty}", "success")
        CPrint(f"tests failed: {tests_failed}/{tests_qty}", "error")

    @staticmethod
    def func_for_test_return_true():
        return True

    @staticmethod
    def func_for_test_return_false():
        return False

    @staticmethod
    def func_for_test_return_str():
        return "agdp_test"

    @staticmethod
    def func_for_test_with_exception():
        raise SyntaxError('A syntax error for agdp_test.')
