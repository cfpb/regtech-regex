import os
from re import Pattern, compile
from dataclasses import dataclass
from typing import List

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
            with open(os.path.join(BASE_DIR, "validations.yaml")) as f:
                regex_yamls = yaml.safe_load(f)
                email = RegexConfig(**regex_yamls["email"])
                tin = RegexConfig(**regex_yamls["tin"])
                rssd_id = RegexConfig(**regex_yamls["rssd_id"])
                lei = RegexConfig(**regex_yamls["lei"])
                phone_number = RegexConfig(**regex_yamls["simple_us_phone_number"])
        except yaml.YAMLError as ye:
            raise RuntimeError(
                "Unable to load validations.yaml, regex validations will be unavailable."
            ) from ye
            
regex_config = Configs()
