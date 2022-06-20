from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    measurement_unit = models.CharField(max_length=200, verbose_name='Единица измерения')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            models.UniqueConstraint(fields=['name', 'measurement_unit'],
                                    name='unique ingredient')
        ]

    def __str__(self):
        return self.name


class Tag(models.Model):
    RED = '#FF0080'
    GREEN = '#00FF00'
    BLUE = '#0000FF'

    COLOR_CHOICES = [
        (RED, 'Красный'),
        (GREEN, 'Зеленый'),
        (BLUE, 'Синий'),
    ]
    name = models.CharField(max_length=200, unique=True,
                            verbose_name='Название тега')
    color_code = models.CharField(max_length=7, unique=True, choices=COLOR_CHOICES,
                             verbose_name='Цвет в HEX-формате')
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name='Уникальный слаг')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

# --------------------------- ddddddddddddddddddddddd ------------------------------------


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





class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.SmallIntegerField("Количество")