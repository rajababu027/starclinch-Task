from django.contrib import admin
from .models import User, Expense, ExpenseTypes, SplitExpense

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'mobile_number')
    search_fields = ('name', 'email', 'mobile_number')

class ExpenseTypesAdmin(admin.ModelAdmin):
    list_display = ('expense_type_id', 'expense_type')
    search_fields = ('expense_type',)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'paid_by', 'amount', 'description', 'date')
    list_filter = ('paid_by',)
    search_fields = ('paid_by__name', 'description')

# class SplitExpenseAdmin(admin.ModelAdmin):
#     list_display = ('split_expense_id', 'expense', 'user', 'expense_type', 'amount')
#     list_filter = ('expense__paid_by', 'user', 'expense_type')
#     search_fields = ('expense__paid_by__name', 'user__name')

admin.site.register(User, UserAdmin)
admin.site.register(ExpenseTypes, ExpenseTypesAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(SplitExpense)