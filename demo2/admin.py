from django.contrib import admin 

from demo2.models import User,Merchant,Profile,Payment,Product,Order,OrderItem,Category,Cart,Address

admin.site.register(User)
admin.site.register(Merchant)
admin.site.register(Profile)
admin.site.register(Product) 
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Address)



# Register your models here.
