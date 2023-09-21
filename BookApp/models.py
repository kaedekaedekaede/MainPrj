from django.db import models

class Book(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()

  def __str__(self):
    return '< Book id:{} name:{} price:{} >'.format(str(self.id),self.name,str(self.price))

  class Meta:
    db_table = 'm_Book'
