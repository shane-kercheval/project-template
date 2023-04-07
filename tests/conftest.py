"""This file defines test fixtures for pytest unit-tests."""
import pytest
from source.service.datasets import DatasetsBase, PickledDataLoader, CsvDataLoader


class TestDatasets(DatasetsBase):
    def __init__(self) -> None:
        # define the datasets before calling __init__()
        self.dataset_1 = PickledDataLoader(
            description="Dataset description",
            dependencies=['SNOWFLAKE.SCHEMA.TABLE'],
            directory='.',
            cache=True,
        )
        self.other_dataset_2 = PickledDataLoader(
            description="Other dataset description",
            dependencies=['dataset_1'],
            directory='.',
            cache=True,
        )
        self.dataset_3_csv = CsvDataLoader(
            description="Other dataset description",
            dependencies=['other_dataset_2'],
            directory='.',
            cache=True,
        )
        super().__init__()


@pytest.fixture(scope='function')
def datasets_fake():
    return TestDatasets()
