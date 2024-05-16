from src.resource_path import ResourceLocation


def test_copy_resource_location():
    assert str(ResourceLocation(ResourceLocation('meow'))) == 'minecraft:meow'
