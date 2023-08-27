from django.db import models
from django.contrib.auth.models import User


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Income(models.Model):
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

    def __str__(self):
        return self.source


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    income_source = models.ForeignKey(Income, on_delete=models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)

    def take_from_income(self):
        if self.income_source.amount >= self.amount:
            self.income_source.amount -= self.amount
            self.income_source.save()

    def add_to_expenses(self):
        self.expense_category.total += self.amount
        self.expense_category.save()

    def save(self, *args, **kwargs):
        self.take_from_income()
        self.add_to_expenses()
        super().save(*args, **kwargs)

    def delete_from_income(self):
        self.income_source.amount += self.amount
        self.income_source.save()

    def remove_from_expenses(self):
        self.expense_category.total -= self.amount
        self.expense_category.save()

    def delete(self, *args, **kwargs):
        self.delete_from_income()
        self.remove_from_expenses()
        super().delete(*args, **kwargs)

#
# class Tag(models.Model):
#     pass
#