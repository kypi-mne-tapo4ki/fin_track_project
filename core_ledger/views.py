from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Category, Operation, Tag, CategoryType
from .forms import OperationForm, CategoryForm, TagForm


def home(request):
    return render(request, 'base.html')


@login_required(login_url='users:login')
def index(request):
    operations = Operation.objects.all()
    last_operations = Operation.objects.filter(date__lte=timezone.now()).order_by("date").reverse()[:5]
    source_categories = Category.objects.filter(category_type=CategoryType.SOURCE)
    storage_categories = Category.objects.filter(category_type=CategoryType.STORAGE)
    expense_categories = Category.objects.filter(category_type=CategoryType.EXPENSE)
    return render(request,
                  'core_ledger/index.html',
                  {
                      'operations': operations,
                      'last_operations': last_operations,
                      'source_categories': source_categories,
                      'storage_categories': storage_categories,
                      'expense_categories': expense_categories,
                  },)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('core_ledger:index')
    else:
        form = CategoryForm()
    return render(request, 'core_ledger/add_category.html', {'form': form})


def add_operation(request):
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            operation = form.save(commit=False)
            operation.date = timezone.now()
            operation.save()
            form.save_m2m()
            return redirect('core_ledger:index')
    else:
        form = OperationForm()
    return render(request, 'core_ledger/add_operation.html', {'form': form})


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            return redirect('core_ledger:index')
    else:
        form = TagForm()
    return render(request, 'core_ledger/add_tag.html', {'form': form})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/confirm_delete.html', {'object': category})


def delete_operation(request, pk):
    operation = get_object_or_404(Operation, pk=pk)
    if request.method == 'POST':
        operation.delete()
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/confirm_delete.html', {'object': operation})


def delete_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('core_ledger:index')
    return render(request, 'core_ledger/confirm_delete.html', {'object': tag})


class CategoryView(DetailView):
    """
    Show operations in a single category
    """
    model = Category
    template_name = 'core_ledger/category_detail.html'
    context_object_name = 'category'


class OperationDetailView(DetailView):
    """
    Show a single operation
    """
    model = Operation
    template_name = 'core_ledger/operation_detail.html'
    context_object_name = 'operation'


class TagDetailView(DetailView):
    """
    Show a single operation
    """
    model = Tag
    template_name = 'core_ledger/tag_detail.html'
    context_object_name = 'tag'


class OperationsView(ListView):
    """
    Show operations for all time
    """
    template_name = 'core_ledger/operations.html'
    context_object_name = 'operations'

    def get_queryset(self):
        return Operation.objects.all().order_by('date').reverse()
