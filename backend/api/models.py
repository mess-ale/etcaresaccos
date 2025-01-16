from django.db import models
from django.contrib.auth.models import User

class ProfileUser(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.DateField()
    gender = models.CharField(max_length=255) 
    country = models.CharField(max_length=255) 
    first_name = models.CharField(max_length=255, null=True) 
    last_name = models.CharField(max_length=255, null=True) 
    user_image = models.ImageField(
        upload_to='user_images/',  # Directory to store uploaded images
        blank=True,                # Allow this field to be optional
        null=True,                 # Allow database to store NULL if no image is uploaded
        default='default.jpg'      # Default image if none is provided (optional)
    )

class Savings(models.Model):
    savings_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.account_type}"


class EqubGroup(models.Model):
    equb_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    group_size = models.IntegerField()
    cycle_period = models.IntegerField()  # number of days for each cycle
    amount_per_cycle = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EqubMembership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    equb_group = models.ForeignKey(EqubGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.equb_group.name}"


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    blog_image = models.ImageField(
        upload_to='blog_images/',  # Directory to store uploaded images
        blank=False,                # Allow this field to be optional
        null=False,                 # Allow database to store NULL if no image is uploaded
        default='default.jpg'      # Default image if none is provided (optional)
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"

class UserFormSubmission(models.Model):
    SAVING_ACCOUNT_CHOICES = [
        ("Time deposit", "Time deposit"),
        ("Children Saving", "Children Saving"),
        ("Business Saving", "Business Saving"),
    ]

    LOAN_PRODUCT_CHOICES = [
        ("Business Loan", "Business Loan"),
        ("Vehicle Loan", "Vehicle Loan"),
        ("Home Loan", "Home Loan"),
    ]

    first_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    grandfather_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    saving_account = models.CharField(max_length=50, choices=SAVING_ACCOUNT_CHOICES)
    loan_product = models.CharField(max_length=50, choices=LOAN_PRODUCT_CHOICES, blank=True, null=True)
    receipt = models.FileField(upload_to="receipts/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.father_name} - {self.email}"
