from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('electronics', 'Electronics'),
    ('it', 'IT'),
    ('groceries', 'Groceries'),
    ('cosmetics', 'Cosmetics')
)

Color_choices=(
    ('red','Red'),
    ('blue','Blue'),
    ('black','Black')
)
class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    

    def __unicode__(self):
        return self.title

class Details(models.Model):
    ids=models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_details', null=True , blank=True)
    description = models.TextField()
    color=models.CharField(choices=Color_choices, max_length=20)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    