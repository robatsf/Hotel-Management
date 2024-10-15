from django.db import models
from django.contrib.auth.models import User

# Room Model
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=[('available', 'Available'), ('booked', 'Booked'), 
                                                      ('cleaning', 'Cleaning'), ('maintenance', 'Maintenance')])

# Employee Model
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('manager', 'Manager'), ('receptionist', 'Receptionist'), 
                                                    ('housekeeping', 'Housekeeping'),('waiter','Waiter'),('security','Security')])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    work_schedule = models.TextField()  # e.g., JSON for flexible work hours

# Inventory Model
class InventoryItem(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=30)  # e.g., Cleaning, Equipment, Linens

# Financial Transactions (includes booking payments and salaries)
# Payment model
class Payment(models.Model):
    # Foreign keys to link payments to specific transactions
    employee = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL)  # For salary payments
    # booking = models.ForeignKey('Booking', null=True, blank=True, on_delete=models.SET_NULL)  # For customer payments
    inventory_item = models.ForeignKey('InventoryItem', null=True, blank=True, on_delete=models.SET_NULL)  # For purchases
    
    # Transaction details
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of payment
    payment_date = models.DateTimeField(auto_now_add=True)  # When the payment was made
    description = models.TextField()  # Short description of the transaction
    
    # Method of payment (e.g., cash, credit card)
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='cash')

    # Optional: Flag for completed or pending payments
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return f"Payment of {self.amount} made on {self.payment_date}"

# Audit Model
class Audit(models.Model):
    audit_date = models.DateField(auto_now_add=True)
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(blank=True)

