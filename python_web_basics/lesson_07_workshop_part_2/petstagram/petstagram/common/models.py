from django.core.exceptions import ValidationError
from django.db import models

# validation method(the complex one)
# def is_positive(value):
#     if value <= 0:
#         raise ValidationError


# class Pet(models.Model):
#     TYPE_CHOICE_DOG = 'dog'
#     TYPE_CHOICE_CAT = 'cat'
#     TYPE_CHOICE_PARROT = 'parrot'
#
#     TYPE_CHOICES = (
#         (TYPE_CHOICE_DOG, 'Dog'),
#         (TYPE_CHOICE_CAT, 'Cat'),
#         (TYPE_CHOICE_PARROT, 'Parrot')
#     )
#
#     type = models.CharField(
#         max_length=6,
#         choices=TYPE_CHOICES
#         )
#     name = models.CharField(
#         max_length=6,
#         )
#     age = models.PositiveIntegerField()
#     # age = models.IntegerField(
#     #     null=False,
#     #     blank=False,
#     #     validators=[
#     #         models.Min(1)
#     #     ]
#     # )
#     description = models.TextField()
#     image_url = models.URLField()


# class Like(models.Model):
#     pass