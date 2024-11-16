from src.models.dish import Dish  # noqa: F401, E261, E501
from pytest import raises
from src.models.ingredient import Ingredient, restriction_map


# Req 2
def test_dish():
    with raises(TypeError):
        Dish('macarronada', 1j)
    with raises(ValueError):
        Dish('macarronada', -1)
    pasta = Dish('macarronada', 1)
    pasta2 = Dish('macarronada', 1)
    assert pasta.name == 'macarronada'
    assert pasta == pasta2
    assert pasta != Dish('fejoada', 2)
    assert hash(pasta) == hash("Dish('macarronada', R$1.00)")
    # sim, vou botar ovo, farinha e bacon no macarrão e não vai ter macarrão,
    # me julguem! 😂
    egg = Ingredient('ovo')
    flour = Ingredient('farinha')
    bacon = Ingredient('bacon')
    pasta.add_ingredient_dependency(egg, 2)
    # muita farinha 😂
    pasta.add_ingredient_dependency(flour, 50)
    pasta.add_ingredient_dependency(bacon, 1)
    assert pasta.get_ingredients() == {egg, flour, bacon}
    RESTRICTIONS = restriction_map()
    expected_restrictions = {
        *RESTRICTIONS[egg.name], *RESTRICTIONS[flour.name],
        *RESTRICTIONS[bacon.name]
    }
    assert pasta.get_restrictions() == expected_restrictions
