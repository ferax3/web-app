from django.db import models

# Create your models here.

class Dragon(models.Model):
    id = models.AutoField('ID_дракона', primary_key=True)
    name = models.CharField('Назва дракона', max_length=30)
    description = models.TextField('Опис')
    availability = models.BooleanField('Чи є в заповіднику?', default=False)
    photo = models.CharField('Посилання на фото', max_length=60)
    bg_photo = models.CharField('Посилання на клас фото', max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дракон'
        verbose_name_plural = 'Дракони'

class Visitor(models.Model):
    id = models.AutoField('ID_відвідувача', primary_key=True)
    first_name = models.CharField('Ім\'я', max_length=20)
    last_name = models.CharField('Прізвище', max_length=20)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Відвідувач'
        verbose_name_plural = 'Відвідувачі'

class Visit(models.Model):
    date = models.DateField('Дата')
    time = models.TimeField('Час')
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    dragon = models.ForeignKey(Dragon, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.time} - {self.visitor.first_name} {self.visitor.last_name}'

    class Meta:
        verbose_name = 'Візит'
        verbose_name_plural = 'Візит'
