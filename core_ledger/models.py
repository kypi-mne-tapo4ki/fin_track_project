from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    total = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class ExpenseCategory(Category):
    pass


class IncomeCategory(Category):
    pass


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def move_operation(self):
        self.category.total += self.amount
        self.category.save()

    def save(self, *args, **kwargs):
        self.move_operation()
        super().save(*args, **kwargs)

    def delete_operation(self):
        self.category.total -= self.amount
        self.category.save()

    def delete(self, *args, **kwargs):
        self.delete_operation()
        super().delete(*args, **kwargs)


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    income_category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)

    def move_operation(self):
        self.income_category.total -= self.amount
        self.income_category.save()

        self.expense_category.total += self.amount
        self.expense_category.save()

    def save(self, *args, **kwargs):
        self.move_operation()
        super().save(*args, **kwargs)

    def delete_operation(self):
        self.income_category.total += self.amount
        self.income_category.save()

        self.expense_category.total -= self.amount
        self.expense_category.save()

    def delete(self, *args, **kwargs):
        self.delete_operation()
        super().delete(*args, **kwargs)

#
# class Tag(models.Model):
#     pass
#