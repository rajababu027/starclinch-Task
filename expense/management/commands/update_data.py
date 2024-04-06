# data_update/management/commands/update_data.py

import csv
import boto3
from django.core.management.base import BaseCommand
from expense.models import User, Expense, ExpenseParticipant  # Import your models

class Command(BaseCommand):
    help = 'Update user data and expenses on Amazon S3 in CSV format'

    def handle(self, *args, **options):
        users = User.objects.all()
        user_expenses = {}
        for user in users:
            expenses = Expense.objects.filter(payer=user)
            user_expenses[user] = expenses

        csv_data = []
        for user, expenses in user_expenses.items():
            for expense in expenses:
                participants = ExpenseParticipant.objects.filter(expense=expense)
                for participant in participants:
                    csv_data.append([
                        user.userId,
                        user.name,
                        user.email,
                        user.mobile_number,
                        expense.amount,
                        expense.expense_type,
                        participant.share
                    ])

        csv_file_path = '/starclinch/user_expense_data.csv'
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['User ID', 'Name', 'Email', 'Mobile Number', 'Expense Amount', 'Expense Type', 'Participant Share'])
            csv_writer.writerows(csv_data)

        s3 = boto3.client('s3')
        bucket_name = 'your-bucket-name'
        s3.upload_file(csv_file_path, bucket_name, 'user_expense_data.csv')
