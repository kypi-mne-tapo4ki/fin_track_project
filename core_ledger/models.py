from django.db import models
from users.models import CustomUser as User


class CategoryType(models.TextChoices):
    EXPENSE = 'Expense'
    STORAGE = 'Storage'
    SOURCE = 'Source'


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=30, unique=True, blank=False)
    category_type = models.CharField(max_length=10, choices=CategoryType.choices, db_index=True)

    def __str__(self):
        return self.title

    def category_operations(self):
        if self.category_type != CategoryType.SOURCE:
            return [operation for operation in Operation.objects.filter(destination=self.id)]
        return [operation for operation in Operation.objects.filter(source=self.id)]

    def total(self):
        operations = self.category_operations()
        return sum([operation.amount for operation in operations])


class Tag(models.Model):
    title = models.CharField(max_length=15)
    binding = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def tag_operations(self):
        return [operation for operation in Operation.objects.filter(tag=self.id, )][::-1]


class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='operation_source')
    destination = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='operation_destination')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'{self.source} --> {self.destination} : {self.amount}'

    def operation_tags(self):
        return [tag for tag in self.tag.all()]
