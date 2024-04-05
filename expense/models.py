from django.db import models



class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    
class ExpenseTypes(models.Model):
    expense_type_id = models.AutoField(primary_key=True)
    expense_type = models.CharField(max_length=255)

    def __str__(self):
        return self.expense_type

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.ForeignKey(ExpenseTypes, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)


class SplitExpense(models.Model):
    split_expense_id = models.AutoField(primary_key=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount
