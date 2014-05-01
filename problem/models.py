from django.db import models

# Create your models here.
class Problem(models.Model):
    CONTEXT_CHOICES = (
        ('V', 'Vulnerable'),
        ('B', 'Binary'),
        ('N', 'Network'),
        ('F', 'Forensics'),
        ('M', 'Misc'),
    )
    context = models.CharField(max_length=1, choices=CONTEXT_CHOICES)

    SCORE_CHOICES = (
        (100, 'Novoice'),
        (200, 'Normal'),
        (300, 'Expert'),
        (400, 'Master'),
        (500, 'Torment'),
    )
    score = models.IntegerField(default=100, choices=SCORE_CHOICES)

    link = models.URLField(null=True)
    file = models.FileField(null=True)

    def __unicode__(self):
        return self.context + " - " + score
