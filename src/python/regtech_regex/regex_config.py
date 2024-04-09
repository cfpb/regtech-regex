import os
from re import Pattern, compile
from dataclasses import dataclass
from typing import List
import importlib.resources

import yaml


@dataclass
class RegexConfig:
    description: str
    error_text: str
    regex: Pattern
    examples: List[str] | None = None
    link: str | None = None
    references: List[str] | None = None


class Configs(object):
    email: RegexConfig
    lei: RegexConfig
    rssd_id: RegexConfig
    tin: RegexConfig
    phone_number: RegexConfig

    def __init__(self):
        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            with importlib.resources.files("regtech_regex").joinpath("validations.yaml").open() as f:
                regex_yamls = yaml.safe_load(f)
                self.email = RegexConfig(**regex_yamls["email"])
                self.email.regex = compile(self.email.regex)

                self.tin = RegexConfig(**regex_yamls["tin"])
                self.tin.regex = compile(self.tin.regex)

                self.rssd_id = RegexConfig(**regex_yamls["rssd_id"])
                self.rssd_id.regex = compile(self.rssd_id.regex)

                self.lei = RegexConfig(**regex_yamls["lei"])
                self.lei.regex = compile(self.lei.regex)

                self.phone_number = RegexConfig(**regex_yamls["simple_us_phone_number"])
                self.phone_number.regex = compile(self.phone_number.regex)
        except yaml.YAMLError as ye:
            raise RuntimeError(
                "Unable to load validations.yaml, regex validations will be unavailable."
            ) from ye


regex_config = Configs()
