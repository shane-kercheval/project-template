import os
import pandas as pd


def test__datasets(datasets_fake):
    data = datasets_fake
    assert data.datasets == ['dataset_1', 'dataset_3_csv', 'other_dataset_2']
    assert data.descriptions == [
        {'dataset': 'dataset_1', 'description': 'Dataset description'},
        {'dataset': 'dataset_3_csv', 'description': 'Other dataset description'},
        {'dataset': 'other_dataset_2', 'description': 'Other dataset description'},
    ]
    assert data.dependencies == [
        {'dataset': 'dataset_1', 'dependencies': ['SNOWFLAKE.SCHEMA.TABLE']},
        {'dataset': 'dataset_3_csv', 'dependencies': ['other_dataset_2']},
        {'dataset': 'other_dataset_2', 'dependencies': ['dataset_1']},
    ]
    assert data.dataset_1._cached_data is None
    assert data.dataset_1.path == './dataset_1.pkl'
    assert not os.path.isfile(data.dataset_1.path)
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    data.dataset_1.save(df)
    assert data.dataset_1._cached_data is not None
    assert os.path.isfile(data.dataset_1.path)
    data.dataset_1.clear_cache()
    assert data.dataset_1._cached_data is None
    df_loaded = data.dataset_1.load()
    assert data.dataset_1._cached_data is not None
    assert (df == df_loaded).all().all()

    assert data.other_dataset_2._cached_data is None
    assert data.other_dataset_2.path == './other_dataset_2.pkl'
    assert not os.path.isfile(data.other_dataset_2.path)
    data.other_dataset_2.save(df.replace(1, 10))
    assert data.other_dataset_2._cached_data is not None
    assert os.path.isfile(data.other_dataset_2.path)
    data.other_dataset_2.clear_cache()
    assert data.other_dataset_2._cached_data is None
    df_loaded = data.other_dataset_2.load()
    assert data.other_dataset_2._cached_data is not None
    assert (df.replace(1, 10) == df_loaded).all().all()

    assert data.dataset_3_csv._cached_data is None
    assert data.dataset_3_csv.path == './dataset_3_csv.csv'
    assert not os.path.isfile(data.dataset_3_csv.path)
    data.dataset_3_csv.save(df.replace(1, 10))
    assert data.dataset_3_csv._cached_data is not None
    assert os.path.isfile(data.dataset_3_csv.path)
    data.dataset_3_csv.clear_cache()
    assert data.dataset_3_csv._cached_data is None
    df_loaded = data.dataset_3_csv.load()
    assert data.dataset_3_csv._cached_data is not None
    assert (df.replace(1, 10) == df_loaded).all().all()

    os.remove('./dataset_1.pkl')
    os.remove('./other_dataset_2.pkl')
    os.remove('./dataset_3_csv.csv')
