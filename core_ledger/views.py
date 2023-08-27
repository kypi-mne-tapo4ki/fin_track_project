from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import ExpenseCategory, Transaction, Income
from .forms import TransactionForm, IncomeForm


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


def index(request):
    transactions = Transaction.objects.all()
    incomes = Income.objects.all()
    expense_category = ExpenseCategory.objects.all()
    return render(request,
                  'core_ledger/index.html',
                  {
                      'transactions': transactions,
                      'incomes': incomes,
                      'expense_category': expense_category,
                  }
                  )


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.take_from_income()
            transaction.add_to_expenses()
            transaction.save()
            return redirect('core_ledger:index')
    else:
        form = TransactionForm()
    return render(request, 'core_ledger/add_transaction.html', {'form': form})


def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/confirm_delete.html', {'transaction': transaction})


def add_expense_category(request):
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


class CategoryTransactionsView(DetailView):
    model = ExpenseCategory
    template_name = 'core_ledger/category_transactions.html'
    context_object_name = 'category'
