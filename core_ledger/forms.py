from django import forms

from .models import Transaction, Income


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'income_category', 'expense_category', ]


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'category', ]
