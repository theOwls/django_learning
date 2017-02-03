import datetime

#The model is a class, with subclasses dhango.db.models.Model
from django.db import models
#Makes sure python plays nice. Thanks everyone.
from django.utils.encoding import python_2_unicode_compatible

#An instance of the models class.
class Question(models.Model):
    #These two attributes are fields in the db.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #This method also ensure python 2.7 display of string
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
#The self in those methods reference parent class methods

class Choice(models.Model):
    #This question is a foreignkey for the question. What is on delete doing?
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
