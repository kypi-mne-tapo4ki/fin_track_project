from django import forms
from .models import Transaction, ExpenseCategory, IncomeCategory, Income


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date']

    income_source = forms.ModelChoiceField(queryset=IncomeCategory.objects.all())
    expense_category = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all())


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'date']

    income_source = forms.ModelChoiceField(queryset=IncomeCategory.objects.all())

