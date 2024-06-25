from django.db import models


class Member(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  golf_club = models.CharField(default="", max_length=10)
  golf_id = models.CharField(max_length=10, null=True)
  hcp = models.FloatField(null=True)
  wins = models.PositiveSmallIntegerField(default=0)
  score = models.PositiveSmallIntegerField(default=0)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
