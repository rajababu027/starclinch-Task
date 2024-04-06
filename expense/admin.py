from django.contrib import admin
# from .models import User, Expense, ExpenseTypes, SplitExpense
from .models import User, Expense, ExpenseParticipant


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'name', 'email', 'mobile_number')
    search_fields = ('name', 'email', 'mobile_number')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'payer', 'amount', 'expense_type', 'created_at')
    list_filter = ('payer', 'expense_type')
    search_fields = ('payer__name',)

class ExpenseParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'expense', 'user', 'share')

admin.site.register(User, UserAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseParticipant, ExpenseParticipantAdmin)
