from flows.example import my_favorite_flow
import pytest
from prefect.testing.utilities import prefect_test_harness


@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    with prefect_test_harness():
        yield


def test_my_favorite_flow():
    assert my_favorite_flow() == 42
