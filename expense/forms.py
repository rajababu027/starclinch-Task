# from django import forms
# from .models import Expense, SplitExpense

# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = ['paid_by', 'amount','description']

#     def __init__(self, *args, **kwargs):
#         super(ExpenseForm, self).__init__(*args, **kwargs)
        
#         self.fields['paid_by'].widget.attrs.update({'class': 'form-control mb-3'})
#         self.fields['amount'].widget.attrs.update({'class': 'form-control mb-3'})
#         self.fields['description'].widget.attrs.update({'class': 'form-control mb-3', 'rows': 3})


# class SplitExpenseForm(forms.ModelForm):
#     class Meta:
#         model = SplitExpense
#         fields = ['expense', 'user', 'expense_type', 'amount']

#     def __init__(self, *args, **kwargs):
#         super(SplitExpenseForm, self).__init__(*args, **kwargs)

#         self.fields['expense'].widget.attrs.update({'class': 'form-control mb-3'})
#         self.fields['expense_type'].widget.attrs.update({'class': 'form-control mb-3'})
#         self.fields['amount'].widget.attrs.update({'class': 'form-control mb-3'})
#         self.fields['user'].widget.attrs.update({'class': 'form-control mb-3', 'multiple': 'multiple'})