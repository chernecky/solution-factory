from django.db import models
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class Poll(models.Model):
    name_poll = models.CharField(verbose_name='Имя_опроса', db_index=True, max_length=100)
    start_date = models.DateTimeField(verbose_name='Дата начала опроса', default=datetime.datetime.now())
    end_date = models.DateTimeField(verbose_name='Дата окончания опроса', default=datetime.datetime.now())
    description = models.TextField(verbose_name='Описание')


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name="Текст вопроса", unique=True)
    type_Question = (
        (1, 'Ответ текстом'),
        (2, 'Ответ выбором варианта'),
        (3, 'Ответ выбором нескольких вариантов'),
    )
    type = models.IntegerField(verbose_name='Тип вопроса', choices=type_Question)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, )
    answer = models.CharField(max_length=200, verbose_name="Ответ")

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
