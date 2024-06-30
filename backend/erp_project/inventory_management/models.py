from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=50)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('sale', 'Sale'),
        ('return', 'Return'),
        ('adjustment', 'Adjustment')
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    date = models.DateField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class InventoryLog(models.Model):
    date = models.DateField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_changed = models.IntegerField()
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} - {self.item.name} - {self.quantity_changed}"
