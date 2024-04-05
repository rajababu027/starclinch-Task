from urllib import response
from django.shortcuts import render, redirect
from .forms import ExpenseForm, SplitExpenseForm


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExpenseForm()
    return render(request, 'expense_form.html', {'form': form})


def create_split_expense(request):
    if request.method == 'POST':
        form = SplitExpenseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SplitExpenseForm()
    return render(request, 'split_expense_form.html', {'form': form})