# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class BoardManager(models.Manager):
    pass


class Board(models.Model):
    user = models.ForeignKey(User, verbose_name="创建的用户")
    content = models.TextField("内容", max_length=512)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    ip = models.CharField('ip', max_length=64)

    objects = BoardManager()

    def __unicode__(self):
        return self.title
