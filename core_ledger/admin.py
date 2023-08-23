from django.contrib import admin

from .models import Income, Transaction, ExpenseCategory

admin.site.register(Income)
admin.site.register(Transaction)
admin.site.register(ExpenseCategory)
