from pytest import raises

from src.exception import ProviderStringifyError
from tests.fixtures import *


def test_get_str_args_error(entity):
    with raises(ProviderStringifyError):
        entity.get_str_args()
