import os

from pytest_mock import MockerFixture

from regtech_regex.regex_config import Configs


class TestRegex:
    def test_regex(self, mocker: MockerFixture):
        mock = mocker.patch("regtech_regex.regex_config.os.path.dirname")
        mock.return_value = os.path.join(os.getcwd(), "src")

        regex_config = Configs.instance()

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

        assert regex_config.email.regex.match(good_email)
        assert not regex_config.email.regex.match(bad_email)

        assert regex_config.lei.regex.match(good_lei)
        assert not regex_config.lei.regex.match(bad_lei)
        assert not regex_config.lei.regex.match(another_bad_lei)

        assert regex_config.rssd_id.regex.match(good_rssd)
        assert not regex_config.rssd_id.regex.match(bad_rssd)

        assert regex_config.phone_number.regex.match(good_phone)
        assert not regex_config.phone_number.regex.match(bad_phone)

        assert regex_config.tin.regex.match(good_tin)
        assert not regex_config.tin.regex.match(bad_tin)
