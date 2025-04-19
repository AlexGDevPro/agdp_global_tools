from assert_utils import Assert
from global_tools.cprint.cprint import CPrint
from global_tools.test.test import Test

# TESTS
tests_results = []


# assert_no_exception
def test_check_assert_no_exception_succeed():
    return Assert.assert_no_exception(Test.func_for_test_return_true)


def test_check_assert_no_exception_fail():
    return not Assert.assert_no_exception(Test.func_for_test_with_exception)


def test_check_assert_no_exception_raise_error_with_wrong_func_type():
    func = 123
    try:
        Assert.assert_no_exception(func)
    except TypeError:
        return True
    return False


tests_results.append({"name": "test_check_assert_no_exception_succeed",
                      "result": test_check_assert_no_exception_succeed()})
tests_results.append({"name": "test_check_assert_no_exception_fail",
                      "result": test_check_assert_no_exception_fail()})
tests_results.append({"name": "test_check_assert_no_exception_raise_error_with_wrong_func_type",
                      "result": test_check_assert_no_exception_raise_error_with_wrong_func_type()})


# assert_exception_is_raised
def test_assert_exception_is_raised_succeed():
    return Assert.assert_exception_is_raised(Test.func_for_test_with_exception)


def test_assert_exception_is_raised_fail():
    return not Assert.assert_exception_is_raised(Test.func_for_test_return_true)


def test_assert_exception_is_raised_raise_error_with_wrong_func_type():
    func = 123
    try:
        Assert.assert_exception_is_raised(func)
    except TypeError:
        return True
    return False


def test_assert_exception_is_raised_raise_error_with_wrong_exception_type_type():
    exception_type = 123
    try:
        Assert.assert_exception_is_raised(Test.func_for_test_return_true, exception_type)
    except TypeError:
        return True
    return False


def test_assert_exception_is_raised_succeed_with_none_as_exception_type():
    return Assert.assert_exception_is_raised(Test.func_for_test_with_exception, None)


def test_assert_exception_is_raised_succeed_with_exception_type():
    return Assert.assert_exception_is_raised(Test.func_for_test_with_exception, SyntaxError())


def test_assert_exception_is_raised_fail_with_exception_type():
    return not Assert.assert_exception_is_raised(Test.func_for_test_with_exception, TypeError())


tests_results.append({"name": "test_assert_exception_is_raised_succeed",
                      "result": test_assert_exception_is_raised_succeed()})
tests_results.append({"name": "test_assert_exception_is_raised_fail",
                      "result": test_assert_exception_is_raised_fail()})
tests_results.append({"name": "test_assert_exception_is_raised_raise_error_with_wrong_func_type",
                      "result": test_assert_exception_is_raised_raise_error_with_wrong_func_type()})
tests_results.append({"name": "test_assert_exception_is_raised_raise_error_with_wrong_exception_type_type",
                      "result": test_assert_exception_is_raised_raise_error_with_wrong_exception_type_type()})
tests_results.append({"name": "test_assert_exception_is_raised_succeed_with_none_as_exception_type",
                      "result": test_assert_exception_is_raised_succeed_with_none_as_exception_type()})
tests_results.append({"name": "test_assert_exception_is_raised_succeed_with_exception_type",
                      "result": test_assert_exception_is_raised_succeed_with_exception_type()})
tests_results.append({"name": "test_assert_exception_is_raised_fail_with_exception_type",
                      "result": test_assert_exception_is_raised_fail_with_exception_type()})


# assert_is_true
def test_assert_is_true_succeed():
    return Assert.assert_is_true(Test.func_for_test_return_true)


def test_assert_is_true_fail():
    return not Assert.assert_is_true(Test.func_for_test_return_false)


def test_assert_is_true_raise_error_with_wrong_func_type():
    func = 123
    try:
        Assert.assert_is_true(func)
    except TypeError:
        return True
    return False


def test_assert_is_true_raise_error_with_wrong_func_return_type():
    try:
        Assert.assert_is_true(Test.func_for_test_return_str)
    except TypeError:
        return True
    return False


tests_results.append({"name": "test_assert_is_true_succeed",
                      "result": test_assert_is_true_succeed()})
tests_results.append({"name": "test_assert_is_true_fail",
                      "result": test_assert_is_true_fail()})
tests_results.append({"name": "test_assert_is_true_raise_error_with_wrong_func_type",
                      "result": test_assert_is_true_raise_error_with_wrong_func_type()})
tests_results.append({"name": "test_assert_is_true_raise_error_with_wrong_func_return_type",
                      "result": test_assert_is_true_raise_error_with_wrong_func_return_type()})


# assert_is_false
def test_assert_is_false_succeed():
    return Assert.assert_is_false(Test.func_for_test_return_false)


def test_assert_is_false_fail():
    return not Assert.assert_is_false(Test.func_for_test_return_true)


def test_assert_is_false_raise_error_with_wrong_func_type():
    func = 123
    try:
        Assert.assert_is_false(func)
    except TypeError:
        return True
    return False


def test_assert_is_false_raise_error_with_wrong_func_return_type():
    try:
        Assert.assert_is_false(Test.func_for_test_return_str)
    except TypeError:
        return True
    return False


tests_results.append({"name": "test_assert_is_false_succeed",
                      "result": test_assert_is_false_succeed()})
tests_results.append({"name": "test_assert_is_false_fail",
                      "result": test_assert_is_false_fail()})
tests_results.append({"name": "test_assert_is_false_raise_error_with_wrong_func_type",
                      "result": test_assert_is_false_raise_error_with_wrong_func_type()})
tests_results.append({"name": "test_assert_is_false_raise_error_with_wrong_func_return_type",
                      "result": test_assert_is_false_raise_error_with_wrong_func_return_type()})

# TESTS EXECUTIONS
CPrint("TESTS : assert_utils.tests", "info")
Test.show_tests_results(tests_results)
