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
