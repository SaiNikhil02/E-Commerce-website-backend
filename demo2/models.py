from django.db import models
from django.contrib.auth.models import AbstractUser  
from django.utils import timezone

class User(AbstractUser):  
    name=models.CharField(max_length=70) 
    email=models.EmailField(unique=True) 
    mobilenumber=models.CharField(max_length=10) 
class Profile(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True) 
    name=models.CharField(max_length=50) 
    email=models.EmailField() 
    username=models.CharField(max_length=50) 
    address=models.TextField() 

class Merchant(models.Model): 
    merchantId=models.UUIDField(primary_key=True) 
    name=models.CharField(max_length=50) 
    email=models.EmailField() 
    companyInfo=models.CharField(max_length=200)    
    
class Category(models.Model): 
    categoryId=models.UUIDField(primary_key=True)   
    name=models.CharField(max_length=30)
    category_desc=models.CharField(max_length=50)  
    
class Product(models.Model): 
    productId=models.UUIDField(primary_key=True) 
    name=models.CharField(max_length=30)
    Product_desc=models.CharField(max_length=50)  
    price=models.IntegerField() 
    stock_quantity=models.IntegerField() 
    merchant=models.ForeignKey(Merchant,related_name='merchant_products',on_delete=models.CASCADE) 
    category=models.ForeignKey(Category,related_name="category_products",on_delete=models.CASCADE)   
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)

    date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Assuming UserID refers to a user in the auth.User model. This sets up a foreign key relationship to the User model:
    user = models.ForeignKey(User, related_name="user_ordered",on_delete=models.CASCADE) 
    status_choices=[
        ('P','Pending'), 
        ('x','Cancelled'), 
        ('o','Ordered')
    ]
    status=models.CharField(max_length=1,choices=status_choices,default='P')

class OrderItem(models.Model):
    orderItemId=models.UUIDField(PRIMARY_KEY=True) 
    order= models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2) 
    quantity=models.IntegerField()


class Cart(models.Model): 
    cartId=models.UUIDField(primary_key=True) 
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    DateCreated=models.DateTimeField(default=timezone.now)
    
class Payment(models.Model): 
    paymentId=models.UUIDField(primary_key=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    card_details=models.CharField(max_length=45)
    PAYMENT_TYPE_CHOICES = [
        ('CC', 'Credit Card'),
        ('PP', 'PayPal'),
        # Add other payment types as needed
        ('DC', 'Debit Card'),
        ('BT', 'Bank Transfer'),
    ]

    # Payment type field
    payment_type = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPE_CHOICES,
        default='CC'  # Set a default value if desired
    ) 
    
    
    
     
    
    
    
    

# Create your models here.
