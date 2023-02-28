from flows.example import my_favorite_flow
from prefect.testing.utilities import prefect_test_harness


def test_my_favorite_flow():
  with prefect_test_harness():
      # run the flow against a temporary testing database
      assert my_favorite_flow() == 42