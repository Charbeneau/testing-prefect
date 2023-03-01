from flows.common import encode_string, semver_str_to_int


def test_encode_string():
    assert encode_string("123.4.56.789") == "MTIzLjQuNTYuNzg5"


def test_semver_str_to_int():
    assert semver_str_to_int("2.3.0") == 2
