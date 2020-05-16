from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('electronics', 'Electronics'),
    ('it', 'IT'),
    ('groceries', 'Groceries'),
    ('cosmetics', 'Cosmetics')
)
class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
