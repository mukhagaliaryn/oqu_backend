from django.db import models
from accounts.models import User
from products.models import Product, Task, Question, Answer, Chapter, Lesson, Video


# Profile model
# -----------------------------------------------------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, verbose_name='Продукты', blank=True)

    def __str__(self):
        return f'Профиль: {self.user}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


# User Product model
class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    score = models.DecimalField(verbose_name='Балл', max_digits=5, decimal_places=2, default=0)
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
    score = models.DecimalField(verbose_name='Балл', max_digits=5, decimal_places=2, default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=100)
    is_done = models.BooleanField(verbose_name='Завершено', default=False)
    is_subscribe = models.BooleanField(verbose_name='Подписка', default=False)

    def __str__(self):
        return f'Глава пользователя: {self.user}'

    class Meta:
        verbose_name = 'Глава пользователя'
        verbose_name_plural = 'Главы пользователей'


# User Lesson model
# -----------------------------------------------------------------------------------------------
class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    score = models.DecimalField(verbose_name='Балл', max_digits=5, decimal_places=2,  default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=100)
    is_done = models.BooleanField(verbose_name='Завершено', default=False)

    def __str__(self):
        return f'Урок пользователя: {self.user}'

    class Meta:
        verbose_name = 'Урок пользователя'
        verbose_name_plural = 'Уроки пользователей'


# User video
class UserVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name='Видео')
    score = models.DecimalField(verbose_name='Балл', max_digits=5, decimal_places=2, default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=10)
    is_done = models.BooleanField(verbose_name='Завершено', default=False)

    def __str__(self):
        return f'Видео пользователя: {self.user}'

    class Meta:
        verbose_name = 'Видео пользователя'
        verbose_name_plural = 'Все видео пользователей'


# User task
class UserTask(models.Model):
    STATUS_CHOICE = (
        ('START', 'Старт'),
        ('PROGRESS', 'В процессе'),
        ('CONFIRM', 'Получение оценку'),
        ('FINISH', 'Завершено'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    score = models.DecimalField(verbose_name='Балл', max_digits=5, decimal_places=2, default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=30)
    status = models.CharField(verbose_name='Статус', max_length=255,
                              choices=STATUS_CHOICE, default=STATUS_CHOICE[0][1])

    def __str__(self):
        return f'Задание пользователя: {self.user}'

    class Meta:
        verbose_name = 'Задание пользователя'
        verbose_name_plural = 'Задания пользователей'


# UserQuiz
# -----------------------------------------------------------------------------------------------
class UserQuizData(models.Model):
    STATUS_CHOICE = (
        ('START', 'Старт'),
        ('PROGRESS', 'В процессе'),
        ('FINISH', 'Завершено'),
    )

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Тест')
    questions = models.ManyToManyField(Question, verbose_name='Вопросы', blank=True)
    start_time = models.DateTimeField(verbose_name='Время начинание', auto_now_add=True)
    finish_time = models.DateTimeField(verbose_name='Закончание', blank=True, null=True)
    score = models.DecimalField(verbose_name='Балл', max_digits=5, decimal_places=2, default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=60)
    status = models.CharField(verbose_name='Статус', max_length=255,
                              choices=STATUS_CHOICE, default=STATUS_CHOICE[0][1])

    def __str__(self):
        return f'Тест пользователя: {self.user}'

    class Meta:
        verbose_name = 'Тест пользователя'
        verbose_name_plural = 'Тесты пользователей'
        ordering = ('-start_time', )


# User answer
# -----------------------------------------------------------------------------------------------
class UserAnswer(models.Model):
    user_quiz = models.ForeignKey(UserQuizData, on_delete=models.CASCADE, verbose_name='Тест пользователя')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answers = models.ManyToManyField(Answer, verbose_name='Ответы пользователя', blank=True)
    score = models.PositiveSmallIntegerField(verbose_name='Балл', default=0)
    max_score = models.PositiveSmallIntegerField(verbose_name='Максимальный балл', default=1)

    def __str__(self):
        return '{} ответ: {}'.format(self.user_quiz.user, self.pk)

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'
