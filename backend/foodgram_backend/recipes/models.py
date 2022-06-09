from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
    )
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    image = models.ImageField(
        upload_to='recipes/', null=False, blank=True)
    text = models.TextField(null=False, verbose_name='Описание')
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    tag = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    cooking_time = models.IntegerField()

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
    )
    color_code = models.CharField(
        max_length=256,
        verbose_name='Цветовой код',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug',
    )


class Ingredient(models.Model):
    name = models.CharField("Название", max_length=200)
    measurement_unit = models.CharField("Единица измерения", max_length=25)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.SmallIntegerField("Количество")