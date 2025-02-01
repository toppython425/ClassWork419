import pytest


@pytest.fixture
def string_for_test():
    return ["", "Some text", "Some text.", ",", ",.", ",.:;'!?"]
