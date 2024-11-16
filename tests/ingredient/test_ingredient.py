from src.models.ingredient import Ingredient, restriction_map  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    restrictions = restriction_map()
    egg = Ingredient('ovo')
    egg2 = Ingredient('ovo')
    assert egg.restrictions == restrictions['ovo']
    assert egg == egg2
    assert egg == egg
    assert egg.name == 'ovo'
    bacon = Ingredient('bacon')
    assert egg != bacon
    invalid_ingredient = Ingredient('salsa')
    assert invalid_ingredient.restrictions == set()
    assert hash(egg) == hash('ovo')
    assert repr(egg) == "Ingredient('ovo')"
