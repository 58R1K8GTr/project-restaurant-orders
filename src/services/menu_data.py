# Req 3
import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, 'r', encoding='utf8') as file:
            content_file = csv.reader(file)
            next(content_file)
            aux_dishes = dict()
            for dish, price, ingredient, recipe_amount in content_file:
                dish = Dish(dish, float(price))
                if dish not in aux_dishes:
                    aux_dishes[dish] = dish
                else:
                    # dish != aux_dishes -> pois são instâncias diferentes.
                    dish = aux_dishes[dish]
                dish.add_ingredient_dependency(
                    Ingredient(ingredient), int(recipe_amount)
                )
            self.dishes = set(aux_dishes)
