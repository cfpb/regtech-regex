import os
from re import Pattern, compile
from dataclasses import dataclass

import yaml


@dataclass
class RegexConfig:
    description: str
    error_text: str
    regex: Pattern
    examples: [str] = None
    link: str = None
    references: [str] = None


class ConfigFactory:
    _configs = None

    def get_regex_configs(self):
        if not self._configs:
            try:
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(BASE_DIR, "validations.yaml")) as f:
                    regex_yamls = yaml.safe_load(f)
                _configs = {}
                for k in regex_yamls.keys():
                    regex = RegexConfig(**regex_yamls[k])
                    regex.regex = compile(regex.regex)
                    _configs[k] = regex
            except yaml.YAMLError as ye:
                raise RuntimeError(
                    "Unable to load validations.yaml, regex validations will be unavailable."
                ) from ye
        return _configs
