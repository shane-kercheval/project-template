"""Provides convenience functions for configuration settings."""

from helpsk.utility import open_yaml

CONFIG = open_yaml('source/config/config.yaml')


DIR_OUTPUT = CONFIG['output']['directory']
DIR_DATA_RAW = CONFIG['data']['raw_directory']
DIR_DATA_INTERIM = CONFIG['data']['interim_directory']
DIR_DATA_EXTERNAL = CONFIG['data']['external_directory']
DIR_DATA_PROCESSED = CONFIG['data']['processed_directory']
DIR_NOTEBOOKS = CONFIG['notebooks']['directory']
