from check import Check
from global_tools.cprint.cprint import CPrint
from global_tools.test.test import Test
from global_tools.assert_utils.assert_utils import Assert

# TESTS
tests_results = []


# check_func_name
def test_check_func_name_succeed():
    func_name = "test"
    return Assert.assert_no_exception(Check.check_func_name, func_name)


def test_check_func_name_raise_error_with_wrong_func_name_type():
    func_name = 123
    return Assert.assert_exception_is_raised(Check.check_func_name, None, func_name)


def test_check_func_name_raise_error_with_wrong_func_name_length():
    func_name = ""
    return Assert.assert_exception_is_raised(Check.check_func_name, None, func_name)


tests_results.append({"name": "test_check_func_name_succeed",
                      "result": test_check_func_name_succeed()})
tests_results.append({"name": "test_check_func_name_raise_error_with_wrong_func_name_type",
                      "result": test_check_func_name_raise_error_with_wrong_func_name_type()})
tests_results.append({"name": "test_check_func_name_raise_error_with_wrong_func_name_length",
                      "result": test_check_func_name_raise_error_with_wrong_func_name_length()})


# check_bool
def test_check_bool_succeed_with_true():
    return Assert.assert_no_exception(Check.check_bool, True)


def test_check_bool_succeed_with_false():
    return Assert.assert_no_exception(Check.check_bool, False)


def test_check_bool_raise_error_with_wrong_arg_type():
    return Assert.assert_exception_is_raised(Check.check_bool, TypeError(), "test")


tests_results.append({"name": "test_check_bool_succeed_with_true",
                      "result": test_check_bool_succeed_with_true()})
tests_results.append({"name": "test_check_bool_succeed_with_false",
                      "result": test_check_bool_succeed_with_false()})
tests_results.append({"name": "test_check_bool_raise_error_with_wrong_arg_type",
                      "result": test_check_bool_raise_error_with_wrong_arg_type()})


# check_func
def test_check_func_succeed():
    return Assert.assert_no_exception(Check.check_func, Test.func_for_test_return_true)


def test_check_func_raise_error_with_wrong_func_type():
    try:
        Check.check_func("test")
    except TypeError:
        return True
    return False


tests_results.append({"name": "test_check_func_succeed",
                      "result": test_check_func_succeed()})
tests_results.append({"name": "test_check_func_raise_error_with_wrong_func_type",
                      "result": test_check_func_raise_error_with_wrong_func_type()})


# check_exception
def test_check_exception_succeed():
    return Assert.assert_no_exception(Check.check_exception, TypeError())


def test_check_exception_raise_error_with_wrong_func_type():
    return Assert.assert_exception_is_raised(Check.check_exception, None, "test")


tests_results.append({"name": "test_check_exception_succeed",
                      "result": test_check_exception_succeed()})
tests_results.append({"name": "test_check_exception_raise_error_with_wrong_func_type",
                      "result": test_check_exception_raise_error_with_wrong_func_type()})

# TESTS EXECUTIONS
CPrint("TESTS : check.tests", "info")
Test.show_tests_results(tests_results)
