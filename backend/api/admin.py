from django.contrib import admin
from django.contrib.admin import display
from django.db.models import Count, Sum
from recipes.models import Cart, Favorite, Ingredient, Recipe, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'count_favorites')
    list_filter = ('author', 'name', 'tags')

    def count_favorites(self, obj):
        return obj.favorites.count()


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'count_ingredients',)
    readonly_fields = ('count_ingredients',)

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'

    @display(description='Количество ингредиентов')
    def count_ingredients(self, obj):
        return (
            obj.recipes.all().annotate(count_ingredients=Count('ingredients'))
            .aggregate(total=Sum('count_ingredients'))['total']
        )


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Cart)
admin.site.register(Favorite)
