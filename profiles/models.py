from django.db import models
from accounts.models import User
from products.models import Task, Question, Answer, Chapter, Lesson


# Profile model
# -----------------------------------------------------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(to='products.Product', verbose_name='Продукты', blank=True)

    def __str__(self):
        return f'Профиль: {self.user}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


# User Product model
class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    score = models.PositiveSmallIntegerField(verbose_name='Балл', default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=100)
    is_subscribe = models.BooleanField(verbose_name='Подписка', default=False)

    def __str__(self):
        return f'Продукт пользователя {self.user}'

    class Meta:
        verbose_name = 'Продукт пользователя'
        verbose_name_plural = 'Продукты пользователей'


# User Chapter model
# -----------------------------------------------------------------------------------------------
class UserChapter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='Раздел')
    score = models.PositiveSmallIntegerField(verbose_name='Балл', default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=100)
    is_done = models.BooleanField(verbose_name='Завершено', default=False)

    def __str__(self):
        return f'Глава пользователя: {self.user.username}'

    class Meta:
        verbose_name = 'Глава пользователя'
        verbose_name_plural = 'Главы пользователей'


# User Lesson model
# -----------------------------------------------------------------------------------------------
class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    score = models.PositiveSmallIntegerField(verbose_name='Балл', default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=100)
    is_done = models.BooleanField(verbose_name='Завершено', default=False)

    def __str__(self):
        return f'Урок пользователя: {self.user.username}'

    class Meta:
        verbose_name = 'Урок пользователя'
        verbose_name_plural = 'Уроки пользователей'


# UserQuiz
# ---------------------------------------------------------------------------------------------------------------------
class UserQuizData(models.Model):
    STATUS_CHOICE = (
        ('START', 'Старт'),
        ('PROGRESS', 'В процессе'),
        ('FINISH', 'Завершено'),
    )
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Тест')
    questions = models.ManyToManyField(Question, verbose_name='Вопросы')
    start_time = models.DateTimeField(verbose_name='Время начинание', auto_now_add=True)
    finish_time = models.DateTimeField(verbose_name='Закончание', blank=True, null=True)
    status = models.CharField(verbose_name='Статус', max_length=255,
                              choices=STATUS_CHOICE, default=STATUS_CHOICE[0][1])

    def __str__(self):
        return f'Тестовые данные: {self.user.username}'

    def get_user_answers(self):
        return self.useranswer_set.all()

    class Meta:
        verbose_name = 'Тест данные пользователя'
        verbose_name_plural = 'Тесты данные пользователей'
        ordering = ('-start_time', )


# User answer
# ---------------------------------------------------------------------------------------------------------------------
class UserAnswer(models.Model):
    user_quiz_data = models.ForeignKey(UserQuizData, on_delete=models.CASCADE, verbose_name='Тест данные пользователя')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answers = models.ManyToManyField(Answer, verbose_name='Ответ пользователя')
    score = models.PositiveSmallIntegerField(verbose_name='Балл', default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=1)

    def __str__(self):
        return '{} ответ: {}'.format(self.user_quiz_data.user.username, self.pk)

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'
