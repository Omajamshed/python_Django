from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Transaction(models.Model):
    TRANSACTION_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # transactions = Transaction.objects.filter(user=request.user)

    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, 
                                        choices=TRANSACTION_CHOICES)
    date = models.DateField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.transaction_type}"
    



class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="My Goal")  # 👈 Add default value
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    def __str__(self):
        return self.name




# class Goal(models.Model):
#     title = models.CharField(max_length=100)
#     target_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     deadline = models.DateField()



# def __str__(self):
#     return self.name