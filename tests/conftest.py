"""Defines test fixtures for pytest unit-tests."""
import pytest
from source.library.dataset_types import DatasetsBase, PickledDataLoader, CsvDataLoader


class TestDatasets(DatasetsBase):
    """Creates a fake/mock dataset."""

    def __init__(self, cache: bool) -> None:
        # define the datasets before calling __init__()
        self.dataset_1 = PickledDataLoader(
            description="Dataset description",
            dependencies=['SNOWFLAKE.SCHEMA.TABLE'],
            directory='.',
            cache=cache,
        )
        self.other_dataset_2 = PickledDataLoader(
            description="Other dataset description",
            dependencies=['dataset_1'],
            directory='.',
            cache=cache,
        )
        self.dataset_3_csv = CsvDataLoader(
            description="Other dataset description",
            dependencies=['other_dataset_2'],
            directory='.',
            cache=cache,
        )
        super().__init__()


@pytest.fixture()
def datasets_fake_cache() -> TestDatasets:
    """Returns fake dataset with cache turned on."""
    return TestDatasets(cache=True)


@pytest.fixture()
def datasets_fake_no_cache() -> TestDatasets:
    """Returns fake dataset with cache turned off."""
    return TestDatasets(cache=False)
