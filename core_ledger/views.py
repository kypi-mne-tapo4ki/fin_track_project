from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import ExpenseCategory, Transaction, IncomeCategory, Income
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
    transactions = Transaction.objects.filter(date__lte=timezone.now()).order_by("date").reverse()[:5]
    incomes = IncomeCategory.objects.all()
    expense_category = ExpenseCategory.objects.all()
    return render(request,
                  'core_ledger/index.html',
                  {
                      'transactions': transactions,
                      'incomes': incomes,
                      'expense_category': expense_category,
                  },)


def add_expense_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ExpenseCategory.objects.create(name=name)
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/add_expense_category.html')


def add_income_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        IncomeCategory.objects.create(name=name)
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/add_income_category.html')


def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            new_income = form.save(commit=False)
            new_income.save()
            return redirect('core_ledger:index')
    else:
        form = IncomeForm()
    return render(request, 'core_ledger/add_income.html', {'form': form})


def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        return redirect('core_ledger:index')
    # return render(request, 'core_ledger/confirm_delete.html', {'transaction': transaction})


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
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


class ExpenseCategoryView(DetailView):
    """
    Shows transactions in a single category
    """
    model = ExpenseCategory
    template_name = 'core_ledger/expense_category.html'
    context_object_name = 'expense_category'


class TransactionDetailView(DetailView):
    """
    Shows a single transaction
    """
    model = Transaction
    template_name = 'core_ledger/transaction_detail.html'
    context_object_name = 'transaction'


class TransactionsView(ListView):
    """
    Shows transactions for all time
    """
    template_name = 'core_ledger/transactions.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.all().order_by('date').reverse()


class IncomeCategoryView(DetailView):
    """
    Shows incomes in a single category
    """
    model = IncomeCategory
    template_name = 'core_ledger/income_category.html'
    context_object_name = 'income_category'


class IncomeDetailView(DetailView):
    """
    Shows a single income
    """
    model = Income
    template_name = 'core_ledger/income_detail.html'
    context_object_name = 'income'


class IncomesView(ListView):
    """
    Shows incomes for all time
    """
    template_name = 'core_ledger/incomes.html'
    context_object_name = 'incomes'

    def get_queryset(self):
        return Income.objects.all().order_by('date').reverse()
