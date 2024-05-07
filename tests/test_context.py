from pytest import raises

from src.entity import Entity
from src.exception import ProviderStringifyError


def test_get_str_args_error(entity: Entity):
    with raises(ProviderStringifyError):
        entity.get_str_args()
