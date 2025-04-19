# CHECK
## Introduction
A collection of method to test values' type, of logical functions.

## List
### check_func_name : Return a formatted function name or raise a ValueError.
### check_bool : Raise a TypeError or nothing for boolean.
### check_func : Raise a TypeError or nothing for Callable.
### check_exception : Raise a TypeError or nothing for BaseException.

---

# TEST
## Introduction
A collection of tools and a Class to instantiate if needed.
It's better to use the static method than the class itself.

## List
### show_tests_results : Take a list of dict as parameter and display a lot of information about the tests resolution.
### func_for_test_return_true : A fake function for test purpose only.
### func_for_test_return_false : A fake function for test purpose only.
### func_for_test_return_str : A fake function for test purpose only.
### func_for_test_with_exception : A fake function for test purpose only.

---

# ASSERT UTILS
## Introduction
A collection of assertions used to test functions.

## List
### assert_no_exception : Assert there's no exception to raise.
### assert_exception_is_raised : Assert there's an exception to raise.
### assert_is_true : Assert the value is True.
### assert_is_false : Assert the value is False.

---

# CPRINT
## Introduction
A Collection of custom print with coloration, or some dividers.

## List

### line_break : Add one line break.
### double_line_break : Add two line break.
### divider : A customizable Divider with a possible line break before, and another one after, and a text inside the divider.

---

# PACKAGE INSTALLATION
## agdp_global_tools-0.1.0-py3-none-any.whl
The fastest and recommended method to install a package.

```
pip install dist/agdp_global_tools-0.1.0-py3-none-any.whl
```

## agdp_global_tools-0.1.0.tar.gz
This method use the source files. Used to compile and test code before installation.
```
pip install dist/agdp-global-tools-0.1.0.tar.gz
```

## from GitHub
```
pip install git+https://github.com/AlexGDevPro/agdp_global_tools.git
```