# regtech_regex

Python project to provide a reusable python module to other python projects dependent on these regex's for validation of data.

## Dependencies

python >= 3.12.0   
pyyaml >= 6.0.1

## Installation

This project has a pyproject.toml that supports both poetry and hatch

### Poetry
Run `poetry lock` then `poetry install` to install dependencies
Run `poetry run pytest` to test the regex's

### Hatch
Run `hatch -e test run pytest` to test the regex's

#### Note
Due to issues with the package managers including the yaml file outside of the python package structure, the Poetry [build-system]
element in the pyproject.toml has been commented out until a time where the CFPB builds and pushes to PyPI 
this project as a standalone whl/sdist distro.  By leaving the Poetry buildp-system commented out, other Regtech SBL Poetry python
projects can successfully declare this git repo as a dependency.  Note that pyproject.toml still requires a build-system, therefore
a hatch build-system has been defined, for now.  

## Usage
RegexConfigs is designed as a Singleton, so a client must call the RegexConfigs.instance() function.

```
from regtech_regex.regex_config import RegexConfigs

configs = RegexConfigs.instance()
match = configs.lei.match("12345")
```

Current list of RegexConfig objects available are:
 - email
 - lei
 - phone_number
 - rssd_id
 - tin

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

Think you might have a simple regular expression that relates to consumer finance that might be helpful? Create an issue! See [CONTRIBUTING](CONTRIBUTING.md) for more details.

---

## Open source licensing info

1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)
