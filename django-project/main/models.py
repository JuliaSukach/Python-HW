from datetime import date, datetime

from django.db import models
from django_countries.fields import CountryField


class User(models.Model):
    class Meta:
        verbose_name = u'User'

    GOAL = (
        ('lose', 'Lose Weight'),
        ('maintain', 'Maintain Weight'),
        ('gain', 'Gain Weight')
    )
    ACTIVITY_LEVEL = (
        ('not_active', 'Not Very Active'),
        ('lightly_active', 'Lightly Active'),
        ('active', 'Active'),
        ('very_active', 'Very Active')
    )
    SEX = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    WEAK_GOAL = (
        ('one-quarter', 'Lose 0.25 kilograms per week'),
        ('one-half', 'Lose 0.5 kilograms per week (Recommended)'),
        ('three-fourths', 'Lose 0.75 kilograms per week'),
        ('kilo', 'Lose 1 kilograms per week')
    )
    # goal = models.CharField(
    #     max_length=20,
    #     choices=GOAL,
    #     default='maintain',
    #     verbose_name=u'Goal'
    # )
    # activity_level = models.CharField(
    #     max_length=20,
    #     choices=ACTIVITY_LEVEL,
    #     default='active',
    #     verbose_name=u'Level'
    # )
    # sex = models.CharField(
    #     max_length=10,
    #     choices=SEX,
    #     default='email',
    #     verbose_name=u'Sex'
    # )
    # birthday = models.DateTimeField(
    #     max_length=40,
    #     default=datetime.now,
    #     verbose_name=u'Birthday'
    # )
    # country = CountryField(
    #     default='Poland',
    #     verbose_name=u'Country'
    # )
    height = models.FloatField(
        default=170,
        verbose_name=u'Height'
    )
    current_weight = models.FloatField(
        default=70,
        verbose_name=u'Current Weight'
    )
    goal_weight = models.FloatField(
        default=57,
        verbose_name=u'Goal Weight'
    )
    # week_goal = models.CharField(
    #     max_length=30,
    #     choices=WEAK_GOAL,
    #     default='three-fourths',
    #     verbose_name=u'Week Goal'
    # )
    email = models.EmailField(
        max_length=254,
        verbose_name=u'Email',
        default='user@gmail.com'
    )
    username = models.CharField(
        default='anonymous',
        max_length=100,
        verbose_name=u'Username',
        unique=True
    )

    def __repr__(self):
        return f'<User {self.username}>'


class Post(models.Model):
    user = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'<User {self.user} {self.body}>'

