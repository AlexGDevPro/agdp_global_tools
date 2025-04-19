from typing import Callable, Any

from global_tools.check.check import Check
from global_tools.cprint.cprint import CPrint


class Assert:
    @staticmethod
    def assert_no_exception(func: Callable[..., Any], *func_args):
        """
        Tested
        """
        Check.check_func(func)
        try:
            func(*func_args)
        except Exception as e:
            CPrint(f"Exception: {type(e)} -> {e}", "info")
            CPrint("TEST FAILED", "error")
            return False
        CPrint("TEST SUCCEED", "success")
        return True

    @staticmethod
    def assert_exception_is_raised(func: Callable[..., Any], exception_type: BaseException = None, *func_args):
        """
        Tested
        """
        Check.check_func(func)
        if exception_type is not None:
            Check.check_exception(exception_type)

        try:
            func(*func_args)
        except Exception as e:
            CPrint(f"Exception: {type(e)} -> {e}", "info")
            if exception_type is not None:
                if type(e) == type(exception_type):
                    CPrint(f"TEST SUCCEED - {type(e)}", "success")
                    return True
                else:
                    CPrint(f"TEST FAILED - Exception type {exception_type} is expected. [{type(e)}]", "error")
                    return False
            CPrint("TEST SUCCEED", "success")
            return True
        CPrint("TEST FAILED", "error")
        return False

    @staticmethod
    def assert_is_true(func: Callable[..., Any], *func_args):
        """
        Tested
        """
        Check.check_func(func)
        res = func(*func_args)
        Check.check_bool(res)
        if res:
            CPrint("TEST SUCCEED", "success")
            return True
        CPrint("TEST FAILED", "error")
        return False

    @staticmethod
    def assert_is_false(func: Callable[..., Any], *func_args):
        """
        Tested
        """
        Check.check_func(func)
        res = func(*func_args)
        Check.check_bool(res)
        if not res:
            CPrint("TEST SUCCEED", "success")
            return True
        CPrint("TEST FAILED", "error")
        return False
