from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import ExpenseCategory, Transaction, Income
from .forms import TransactionForm, IncomeForm


def index(request):
    transactions = Transaction.objects.all()
    incomes = Income.objects.all()
    return render(request,
                  'core_ledger/index.html',
                  {'transactions': transactions, 'incomes': incomes})


def add_transaction(request):
    incomes = Income.objects.all()
    expense_categories = ExpenseCategory.objects.all()

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.expense_category.amount += transaction.amount
            transaction.expense_category.save()
            transaction.income_source.amount -= transaction.amount
            transaction.income_source.save()
            transaction.save()
            return redirect('core_ledger:index')
    else:
        form = TransactionForm()
    return render(
        request,
        'core_ledger/add_transaction.html',
        {'form': form, 'incomes': incomes, 'expense_categories': expense_categories}
    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core_ledger:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ExpenseCategory.objects.create(name=name)
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/add_expense_category.html')


def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core_ledger:index')
    else:
        form = IncomeForm()
    return render(request, 'core_ledger/add_income.html', {'form': form})
