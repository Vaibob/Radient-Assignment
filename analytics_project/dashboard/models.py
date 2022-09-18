from django.db import models

class Order (models.Model):
    date = models.DateField ()
    returns = models.FloatField()
    equity_id = models.CharField(max_length=5)
    open_v = models.FloatField()
    high = models.FloatField()
    low = models.FloatField ()
    close = models. FloatField()
    adj_close = models.FloatField()
