from django.db import models

# Create your models here.
class income_balance(models.Model):
  symbol = models.CharField(max_length=10)
  date= models.TextField()
  revenue = models.FloatField()
  costOfRevenue = models.FloatField()
  netIncome = models.FloatField()
  cashAndCashEquivalents = models.FloatField()
  shortTermInvestments = models.FloatField()
  netReceivables = models.FloatField()
  inventory = models.FloatField()
  shortTermDebt = models.FloatField()