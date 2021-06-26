
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Модель пользователя
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return str(self.user.username)


# class Otdel(models.Model):
#     otdel_name = models.CharField(max_length=1000, verbose_name='Отделение')

#     def __str__(self):
#         return str(self.otdel_name)


# class Specialnost(models.Model):
#     name = models.CharField(max_length=1000, verbose_name='Специальность')
#     otdel = models.ForeignKey(Otdel, on_delete=models.PROTECT)

#     def __str__(self):
#         return '{} {}'.format(self.name, self.otdel)


def add_path(instance, filename):
    return 'spec_{0}/{1}'.format(instance.category.id, filename)



class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,verbose_name='Отделение')
    category_text = models.CharField(max_length=100,verbose_name='Специальность')

    def __str__(self):
        return self.category_text
    


class Card(models.Model):
    '''
    карточка выпускника
    '''
    name = models.CharField(verbose_name='ФИО', max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  null=True, blank=True, verbose_name='специальность')
    kredo = models.TextField(max_length=1000, blank=True)
    ava = models.ImageField(upload_to=add_path, default=None)
    otzyv = models.TextField(max_length=1000)
    god_grad = models.IntegerField('Год выпуска', blank=True)

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return "{0} {1}".format(self.otzyv[:10] + "...", self.kredo[:10] + "...")

        




