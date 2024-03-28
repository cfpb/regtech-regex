import os
import re

from pytest_mock import MockerFixture

from regtech_regex.regex_config import ConfigFactory


class TestRegex:
    def test_regex(self, mocker: MockerFixture):
        mock = mocker.patch("regtech_regex.regex_config.os.path.dirname")
        mock.return_value = os.path.join(os.getcwd(), "src")

        configs = ConfigFactory().get_regex_configs()

        good_email = "Jason.Adam@cfpb.gov"
        bad_email = "something@bad_domain"

        good_lei = "1234567890ABCDEFGH00"
        bad_lei = "123"
        another_bad_lei = "1234567890ABCDEFGHIJ"

        good_rssd = "1234"
        bad_rssd = "ABC"

        good_phone = "555-555-5555"
        bad_phone = "12-34-56-78-90"

        good_tin = "98-7654321"
        bad_tin = "123456789"

        assert re.match(configs["email"].regex, good_email)
        assert not re.match(configs["email"].regex, bad_email)

        assert re.match(configs["lei"].regex, good_lei)
        assert not re.match(configs["lei"].regex, bad_lei)
        assert not re.match(configs["lei"].regex, another_bad_lei)

        assert re.match(configs["rssd_id"].regex, good_rssd)
        assert not re.match(configs["rssd_id"].regex, bad_rssd)

        assert re.match(configs["simple_us_phone_number"].regex, good_phone)
        assert not re.match(configs["simple_us_phone_number"].regex, bad_phone)

        assert re.match(configs["tin"].regex, good_tin)
        assert not re.match(configs["tin"].regex, bad_tin)
