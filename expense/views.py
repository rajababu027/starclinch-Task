from django.shortcuts import render, redirect
from .models import User, Expense, ExpenseParticipant
from django.db.models import Sum

def add_expense(request):
    users = User.objects.all()
    if request.method == 'POST':
        payer_id = request.user.id
        amount = float(request.POST['amount'])
        expense_type = request.POST['expense_type']
        participants = request.POST.getlist('participants')
        
        expense = Expense.objects.create(payer_id=payer_id, amount=amount, expense_type=expense_type)
        
        if expense_type == Expense.EQUAL:
            split_equally(expense, participants)
        elif expense_type == Expense.PERCENT:
            percentages = [float(p) for p in request.POST.get('percentages').split(",")]
            split_by_percent(expense, participants, percentages)
        elif expense_type == Expense.EXACT:
            shares = [float(s) for s in request.POST.get('shares').split(",")]
            split_exact(expense, participants, shares)

        return redirect('add_expense')
        
    return render(request, 'add_expense.html', {'users': users})

def split_equally(expense, participants):
    amount_per_person = expense.amount / len(participants)
    for participant_id in participants:
        ExpenseParticipant.objects.create(expense=expense, user_id=participant_id, share=amount_per_person)

def split_by_percent(expense, participants, percentages):
    total_percentage = sum(percentages)
    if total_percentage != 100:
        raise ValueError("Total percentage must be 100")
        
    for participant_id, percentage in zip(participants, percentages):
        amount_owed = (percentage / 100) * expense.amount
        ExpenseParticipant.objects.create(expense=expense, user_id=participant_id, share=amount_owed)

def split_exact(expense, participants, shares):
    total_shares = sum(shares)
    if total_shares != expense.amount:
        raise ValueError("Total shares must be equal to the expense amount")
        
    for participant_id, share in zip(participants, shares):
        ExpenseParticipant.objects.create(expense=expense, user_id=participant_id, share=share)


def all_users_balances(request):
    users = User.objects.all()
    balances_data = {}

    for user in users:
        expenses_paid = ExpenseParticipant.objects.filter(user=user).values('expense__payer').annotate(total_share=Sum('share'))
        expenses_owed = ExpenseParticipant.objects.filter(expense__payer=user).values('user').annotate(total_share=Sum('share'))
        
        balance = 0
        for expense in expenses_paid:
            balance -= expense['total_share']
        
        for expense in expenses_owed:
            balance += expense['total_share']
        
        balances_data[user] = balance
    
    balances = [{'user': user, 'amount': amount} for user, amount in balances_data.items() if amount != 0]
    
    return render(request, 'balance_list.html', {'balances': balances})


def show_balances(request, user_id):
    user = User.objects.get(id=user_id)
    expenses_paid = ExpenseParticipant.objects.filter(user=user).values('expense__payer').annotate(total_share=Sum('share'))
    expenses_owed = ExpenseParticipant.objects.filter(expense__payer=user).values('user').annotate(total_share=Sum('share'))
    balance_data = {}
    for expense in expenses_paid:
        balance_data[expense['expense__payer']] = balance_data.get(expense['expense__payer'], 0) - expense['total_share']
    
    for expense in expenses_owed:
        balance_data[user] = balance_data.get(user, 0) + expense['total_share']
    
    balances = [{'user': u, 'amount': amount} for u, amount in balance_data.items() if amount != 0]
    
    return render(request, 'user_balance.html', {'user': user, 'balances': balances})



