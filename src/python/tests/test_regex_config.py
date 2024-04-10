import os
import pytest

from pytest_mock import MockerFixture

from regtech_regex.regex_config import RegexConfigs


class TestRegex:
    def test_singleton_instance(self, mocker: MockerFixture):
        mock = mocker.patch("regtech_regex.regex_config.os.path.dirname")
        mock.return_value = os.path.join(os.getcwd(), "src")

        with pytest.raises(Exception) as e:
            configs = RegexConfigs()

        assert isinstance(e.value, NotImplementedError)
        assert str(e.value) == "Use instance() instead"

        configs = RegexConfigs.instance()
        assert set(["email", "lei", "rssd_id", "tin", "phone_number"]).issubset(
            set(dir(configs))
        )

    def test_regex(self, mocker: MockerFixture):
        mock = mocker.patch("regtech_regex.regex_config.os.path.dirname")
        mock.return_value = os.path.join(os.getcwd(), "src")

        configs = RegexConfigs.instance()

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

        assert configs.email.regex.match(good_email)
        assert not configs.email.regex.match(bad_email)

        assert configs.lei.regex.match(good_lei)
        assert not configs.lei.regex.match(bad_lei)
        assert not configs.lei.regex.match(another_bad_lei)

        assert configs.rssd_id.regex.match(good_rssd)
        assert not configs.rssd_id.regex.match(bad_rssd)

        assert configs.phone_number.regex.match(good_phone)
        assert not configs.phone_number.regex.match(bad_phone)

        assert configs.tin.regex.match(good_tin)
        assert not configs.tin.regex.match(bad_tin)
