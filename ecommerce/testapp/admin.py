from django.contrib import admin

from testapp.models import Product,Confirmation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','discounted_price','category','description','image']


class ConfirmationAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone_no','alternate_number','email_id',
    'address','city','pincode','state']



admin.site.register(Product,ProductAdmin)

admin.site.register(Confirmation,ConfirmationAdmin)
