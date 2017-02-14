import os
import uuid
import re
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


def random_name_upload_to(instance, filename):
    name = uuid.uuid4().hex
    ext = os.path.splitext(filename)[-1].lower()
    # datetime.datetime.now() # XXX
    dir_path = timezone.now().strftime('%Y')  #/%m/%d/%H')
    return os.path.join(dir_path, name[:2], name[2:4], name[4:] + ext)
    # return os.path.join(dir_path, name + ext)


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    user = models.ForeignKey(User, related_name='blog_post_set')
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,
            validators=[MinLengthValidator(10)],
            verbose_name='제목', help_text='포스팅 제목으로 노출됩니다. 최대 100자까지 지원됩니다.')  # descriptor syntax
    content = models.TextField(verbose_name='내용')
    photo = models.ImageField(upload_to=random_name_upload_to)
    lnglat = models.CharField(max_length=50, blank=True,
            validators=[lnglat_validator])
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[-1]
        return None

    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]
        return None


class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()

    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


