from django.db import models
from django.contrib.auth.models import AbstractUser  
from django.utils import timezone

class User(AbstractUser):  
    name=models.CharField(max_length=70) 
    email=models.EmailField(unique=True) 
    mobilenumber=models.CharField(max_length=10) 
    def __str__(self): 
        return self.name
    class Meta:
        db_table='custom_user'
        swappable = 'AUTH_USER_MODEL'
        
class Profile(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='profile',related_query_name='profile') 
    name=models.CharField(max_length=50) 
    email=models.EmailField() 
    username=models.CharField(max_length=50) 
    address=models.TextField()  
    def __str__(self): 
        return self.user

class Merchant(models.Model): 
    merchantId=models.UUIDField(primary_key=True) 
    name=models.CharField(max_length=50) 
    email=models.EmailField() 
    companyInfo=models.CharField(max_length=200)    
    def __str__(self): 
        return self.name 
    
class Category(models.Model): 
    categoryId=models.UUIDField(primary_key=True)   
    name=models.CharField(max_length=30)
    category_desc=models.CharField(max_length=50)   
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model): 
    productId=models.UUIDField(primary_key=True) 
    name=models.CharField(max_length=30)
    Product_desc=models.CharField(max_length=50)  
    price=models.IntegerField() 
    stock_quantity=models.IntegerField() 
    merchant=models.ForeignKey(Merchant,related_name='product',related_query_name='product',on_delete=models.CASCADE) 
    category=models.ForeignKey(Category,related_name="category_products",related_query_name='category_products',on_delete=models.CASCADE)   
    def __str__(self) -> str:
        return self.name
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)

    date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Assuming UserID refers to a user in the auth.User model. This sets up a foreign key relationship to the User model:
    user = models.ForeignKey(User, related_name="user_ordered",related_query_name='user_ordered',on_delete=models.CASCADE) 
    status_choices=[
        ('P','Pending'), 
        ('x','Cancelled'), 
        ('o','Ordered')
    ]
    status=models.CharField(max_length=1,choices=status_choices,default='P') 
    def __str__(self): 
        return self.order_id

class OrderItem(models.Model):
    orderItemId=models.UUIDField(primary_key=True) 
    order= models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_orderitem',related_query_name='order_orderitem')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_orderitem',related_query_name='product_orderitem')
    price=models.DecimalField(max_digits=10,decimal_places=2) 
    quantity=models.IntegerField() 
    def __str__(self): 
        return self.order


class Cart(models.Model): 
    cartId=models.UUIDField(primary_key=True) 
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_cart',related_query_name='user_cart')
    DateCreated=models.DateTimeField(default=timezone.now) 
    def __str__(self) -> str:
        return self.cartId
    
class Payment(models.Model): 
    paymentId=models.UUIDField(primary_key=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_payment',related_query_name='user_payment') 
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
    def __str__(self) -> str:
        return self.paymentId
    
class Address(models.Model): 
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_address',related_query_name='user_address')  
    pincode=models.DecimalField(max_digits=6,decimal_places=0) 
    permanent_address=models.TextField() 
    country=models.CharField(max_length=60) 
    def __str__(self) -> str:
        return self.country

