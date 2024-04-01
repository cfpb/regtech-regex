import os

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

        assert configs["email"].regex.match(good_email)
        assert not configs["email"].regex.match(bad_email)

        assert configs["lei"].regex.match(good_lei)
        assert not configs["lei"].regex.match(bad_lei)
        assert not configs["lei"].regex.match(another_bad_lei)

        assert configs["rssd_id"].regex.match(good_rssd)
        assert not configs["rssd_id"].regex.match(bad_rssd)

        assert configs["simple_us_phone_number"].regex.match(good_phone)
        assert not configs["simple_us_phone_number"].regex.match(bad_phone)

        assert configs["tin"].regex.match(good_tin)
        assert not configs["tin"].regex.match(bad_tin)
