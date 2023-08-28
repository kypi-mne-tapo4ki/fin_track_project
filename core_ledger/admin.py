from django.contrib import admin

from .models import Income, Transaction, ExpenseCategory, IncomeCategory

admin.site.register(Transaction)
admin.site.register(Income)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
