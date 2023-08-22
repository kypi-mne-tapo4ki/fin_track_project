from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Category, Transaction
from .forms import TransactionForm


def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'core_ledger/index.html', {'transactions': transactions})


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('core_ledger:index')
    else:
        form = TransactionForm()
    return render(request, 'core_ledger/add_transaction.html', {'form': form})


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
        Category.objects.create(name=name)
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/add_category.html')
