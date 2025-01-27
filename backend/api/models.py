from django.db import models
from django.contrib.auth.models import User

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
    event_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class UserFormSubmission(models.Model):
    SAVING_ACCOUNT_CHOICES = [
        ("Time deposit", "Time deposit"),
        ("Children Saving", "Children Saving"),
        ("Business Saving", "Business Saving"),
        ("Time limit saving", "Time limit saving"),
        ("Interest free savings", "Interest free savings"),
        ("Savings of women", "Savings of women"),
    ]

    LOAN_PRODUCT_CHOICES = [
        ("Business Loan", "Business Loan"),
        ("Salary Loan", "Salary Loan"),
        ("Special short-term loans", "Special short-term loans"),
        ("Car Loan", "Car Loan"),
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
