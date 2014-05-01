from django.db import models
from django.contrib.auth.models import User

import hashlib

from problem.models import Problem

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User)

    solved_problems = models.ManyToManyField(Problem)

    def __unicode__(self):
        return self.user.username

    def score(self):
        score = 0

        for problem in self.solved_problems:
            score += problem.score

        return score

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.username).hexdigest()
