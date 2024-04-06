from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    EQUAL = 'EQUAL'
    EXACT = 'EXACT'
    PERCENT = 'PERCENT'

    EXPENSE_TYPES = [
        (EQUAL, 'Equal'),
        (EXACT, 'Exact'),
        (PERCENT, 'Percent'),
    ]

    payer = models.ForeignKey(User, related_name='paid_expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPES)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)
    
class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(Expense, related_name='participants', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)
    share = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.expense} - {self.user.name} - {str(self.share)}"
