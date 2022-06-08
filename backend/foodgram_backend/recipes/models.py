from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    caption = models.TextField()
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        return self.text

# Рецепт должен описываться такими полями:
# Автор публикации (пользователь).
# Название.
# Картинка.
# Текстовое описание.
# Ингредиенты: продукты для приготовления блюда по рецепту. Множественное поле, выбор из предустановленного списка, с указанием количества и единицы измерения.
# Тег (можно установить несколько тегов на один рецепт, выбор из предустановленных).
# Время приготовления в минутах.
# Все поля обязательны для заполнения.