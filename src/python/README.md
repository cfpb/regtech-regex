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
Due to issues with the package managers including the yaml file outside of the python package structure, the [build-system]
elements in the pyproject.toml have intionally been commented out until a time where the CFPB builds and pushes to PyPI 
this project as a standalone whl/sdist distro.  By leaving the buildp-systems commented out, other Regtech SBL python
projects can successfully declare this git repo as a dependency.  

## Usage

```
from regtech_regex.regex_config import ConfigFactory

config_factory = ConfigFactory()

...

configs = config_factory.get_regex_configs()

match = re.match(configs["lei"].regex, self.lei)
```

The ConfigFactory was written to so that a single instance of ConfigFactory will maintain the dict of RegexConfig objects without having
to parse the yaml each time get_regex_configs() is called (though the time it takes to do that is negligible).

The config dict has keys that match the validations.yaml.  Each RegexConfig contains the full set of data defined in yaml for that key.


## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

Think you might have a simple regular expression that relates to consumer finance that might be helpful? Create an issue! See [CONTRIBUTING](CONTRIBUTING.md) for more details.

---

## Open source licensing info

1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)
