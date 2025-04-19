from typing import Callable, Any


class Check:
    @staticmethod
    def check_func_name(func_name):
        """
        Tested
        """
        if not isinstance(func_name, str):
            raise TypeError('The func name must be a string.')

        func_name = func_name.replace(" ", "")
        func_name = func_name.lower()

        if len(func_name) == 0:
            raise ValueError('The func name is required.')
        return func_name

    @staticmethod
    def check_bool(bool_to_test: bool):
        """
        Tested
        """
        if not isinstance(bool_to_test, bool):
            raise TypeError('The bool_to_test is not a bool.')

    @staticmethod
    def check_func(func_to_test: Callable[..., Any]):
        """
        Tested
        """
        if not isinstance(func_to_test, Callable):
            raise TypeError('The func argument must be a function.')

    @staticmethod
    def check_exception(exception_type: BaseException):
        """
        Tested
        """
        if not isinstance(exception_type, BaseException):
            raise TypeError('The exception_type argument must inherit from BaseException.')
