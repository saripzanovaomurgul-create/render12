from django.db import models

class Task(models.Model):
    # Название задачи
    title = models.CharField(max_length=200, verbose_name="Название задачи")
    # Дата создания
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задачу"
        verbose_name_plural = "Список задач"