

from core.src.exceptions import (
    RecipeBusinessException,
    RecipeCreateException,
    RecipeRepositoryException,
)
from core.src.models import Recipe
from core.src.repository import RecipeRepository
from core.src.use_cases.recipe.create.request import CreateRecipeRequest
from core.src.use_cases.recipe.create.response import CreateRecipeResponse


class CreateRecipe:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def __call__(self, request: CreateRecipeRequest) -> CreateRecipeResponse:
        try:
            recipe = Recipe(**request._asdict())

            response = self.recipe_repository.create(recipe)

            if not response:
                raise RecipeCreateException()

            response_dict = response._asdict()
            return CreateRecipeResponse(**response_dict)

        except RecipeRepositoryException as e:
            raise RecipeBusinessException(str(e))
