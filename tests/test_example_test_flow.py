from flows.example import my_favorite_flow
import pytest
from prefect.testing.utilities import prefect_test_harness


# See
# https://docs.pytest.org/en/6.2.x/fixture.html#autouse-fixtures-fixtures-you-don-t-have-to-request
# https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    with prefect_test_harness():
        yield


def test_my_favorite_flow():
    assert my_favorite_flow() == 42
