# Changelog

All notable changes to this project will be documented in this file.

The versioning follows the [Semantic Versioning](https://semver.org/) specification.

## [0.2.1] - 2025-04-20

### Fixed

- Changing Test folder and file name from `test` to `agdp_test`, and class name from `Test` to `AGDPTest` to avoid
  conflicts with Python built-in package.

## [0.2.0] - 2025-04-20

### Added

- Changelog to follow this package evolution.
- `NOTES.md` for developers, containing guidelines for updating the library, including:
    - **Package versioning** (MAJOR.MINOR.PATCH format).
    - Instructions to update the version in `pyproject.toml` and `global_tools/__init__.py`.
    - Steps for committing and tagging the new version (`git tag vx.x.x` and `git push origin main --tags`).

### Changed

- Added detailed instructions in README.md on how to install or upgrade to a specific version from GitHub.
- Global refactoring of the README.md for better readability.
- Added CHANGELOG.md to the MANIFEST to ensure it is included in the package distribution.

### Fixed

- Missing version added to `__init__.py`.

---

## [0.1.0] - 2025-04-19

### Added

- **Initial version**: Created the project with the following core components:
    - `Assert`: A set of utility functions for assertion checks in testing.
    - `CPrint`: A utility for colored console output.
    - `Test`: Basic test structure and setup for running unit tests.
    - `Check`: A set of utility to check values' type and functions' logic.

### Purpose

- Launched as a collection of useful utilities and classes for everyday development tasks, focusing on testing and
  debugging.
