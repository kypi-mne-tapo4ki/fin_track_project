from django import forms
from .models import Transaction, ExpenseCategory, Income


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'date']

    income_source = forms.ModelChoiceField(queryset=Income.objects.all())
    expense_category = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all())


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date']
