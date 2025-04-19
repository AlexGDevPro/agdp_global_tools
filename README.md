# CHANGELOG

[here](./CHANGELOG.md) to see the changelog.

# CHECK

## Introduction

A collection of methods to test values' types and logical functions.

## List

### check_func_name : Returns a formatted function name or raises a ValueError.

### check_bool : Raises a TypeError or nothing for boolean values.

### check_func : Raises a TypeError or nothing for callable values.

### check_exception : Raises a TypeError or nothing for exceptions derived from BaseException.

---

# TEST

## Introduction

A collection of tools and a Class to instantiate if needed.
It is recommended to use the static methods rather than instantiating the class itself.

## List

### show_tests_results : Takes a list of dictionaries as parameters and displays detailed information about the test results.

### func_for_test_return_true : A fake function for testing purposes, always returns `True`.

### func_for_test_return_false : A fake function for testing purposes, always returns `False`.

### func_for_test_return_str : A fake function for testing purposes, always returns a string.

### func_for_test_with_exception : A fake function for testing purposes, raises an exception.

---

# ASSERT UTILS

## Introduction

A collection of assertions used to test functions.

## List

### assert_no_exception : Asserts that no exception is raised.

### assert_exception_is_raised : Asserts that an exception is raised.

### assert_is_true : Asserts that the value is `True`.

### assert_is_false : Asserts that the value is `False`.

---

# CPRINT

## Introduction

A collection of custom print functions with colorization, and dividers.

## List

### line_break : Adds one line break.

### double_line_break : Adds two line breaks.

### divider : A customizable divider with optional line breaks before and after, and a text inside the divider.

---

# PACKAGE INSTALLATION

## Installing agdp_global_tools

### Using a Wheel File (`.whl`)

This is the fastest and recommended method to install the package. It's precompiled and easy to install.

```commandline
pip install dist/agdp_global_tools-0.1.0-py3-none-any.whl
```

### Using a Source Tarball (`.tar.gz`)

This method uses the source files and is suitable for compiling and testing code before installation. It might take
longer and require additional dependencies.

```commandline
pip install dist/agdp-global-tools-0.1.0.tar.gz
```

### From GitHub

#### Install Latest Version

To install the latest version directly from GitHub:

```commandline
pip install git+https://github.com/AlexGDevPro/agdp_global_tools.git
```

#### Install Specific Version

To install a specific version from GitHub:

```commandline
pip install git+https://github.com/AlexGDevPro/agdp_global_tools.git@v0.1.0
```

#### Upgrade to Latest Version

To upgrade to the latest version:

```commandline
pip install --upgrade git+https://github.com/AlexGDevPro/agdp_global_tools.git
```

#### Upgrade to a Specific Version

To upgrade to a specific version:

```commandline
pip install --upgrade git+https://github.com/AlexGDevPro/agdp_global_tools.git@v0.1.1
```

## Uninstalling agdp_global_tools

### Uninstall command

To uninstall the current version:

```commandline
pip uninstall agdp-global-tools
```

---
