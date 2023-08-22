from django import forms
from .models import Transaction, Category


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'title', 'amount', 'date']

    category = forms.ModelChoiceField(queryset=Category.objects.all())
