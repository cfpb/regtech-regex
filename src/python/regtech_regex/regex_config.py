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


class RegexConfigs(object):
    email: RegexConfig
    lei: RegexConfig
    rssd_id: RegexConfig
    tin: RegexConfig
    phone_number: RegexConfig

    _instance: "RegexConfigs | None" = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            try:
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                with open(os.path.join(BASE_DIR, "validations.yaml")) as f:
                    regex_yamls = yaml.safe_load(f)
                    cls.email = RegexConfig(**regex_yamls["email"])
                    cls.email.regex = compile(cls.email.regex)

                    cls.tin = RegexConfig(**regex_yamls["tin"])
                    cls.tin.regex = compile(cls.tin.regex)

                    cls.rssd_id = RegexConfig(**regex_yamls["rssd_id"])
                    cls.rssd_id.regex = compile(cls.rssd_id.regex)

                    cls.lei = RegexConfig(**regex_yamls["lei"])
                    cls.lei.regex = compile(cls.lei.regex)

                    cls.phone_number = RegexConfig(
                        **regex_yamls["simple_us_phone_number"]
                    )
                    cls.phone_number.regex = compile(cls.phone_number.regex)
                cls._instance = cls.__new__(cls)
            except yaml.YAMLError as ye:
                raise RuntimeError(
                    "Unable to load validations.yaml, regex validations will be unavailable."
                ) from ye
        return cls._instance

    def __init__(self):
        raise NotImplementedError("Use instance() instead")
