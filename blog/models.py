from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        if len(self.title) > 20:
            return "{}{}-- {}".format(self.title[:20],"....", self.author)
        else:
            return "{}-- {}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs = {"pk": self.pk})
