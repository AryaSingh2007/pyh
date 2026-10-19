from django.contrib import admin
from .models import *

# Register your models here.

class tblcontactAdmin(admin.ModelAdmin):
    list_display=("id","name","email","mobile","message")
admin.site.register(tblcontact,tblcontactAdmin)

class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)

class tblteamAdmin(admin.ModelAdmin):
    list_display=("id","name","designation","picture")
admin.site.register(tblteam,tblteamAdmin)

class tbl_registerAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","password","address","profile_picture")
admin.site.register(tbl_register,tbl_registerAdmin)

class tbl_categoryAdmin(admin.ModelAdmin):
    list_display=("id","category_name","cate_picture")
admin.site.register(tbl_category,tbl_categoryAdmin)

class tbl_productAdmin(admin.ModelAdmin):
    list_display=("id","product_name","product_picture","category","price","total_discount",
                  "product_weight","product_description")
admin.site.register(tbl_product,tbl_productAdmin)

class tbl_cartAdmin(admin.ModelAdmin):
    list_display=("id","userid","pid","product_name","product_quantity","product_picture","discount_price","price","product_weight","total_price")
admin.site.register(tbl_cart,tbl_cartAdmin)

class tbl_orderAdmin(admin.ModelAdmin):
   list_display=("id","userid","pid","product_name","product_picture","price","discount_price","product_quantity","product_weight","total_price","status","order_date")
admin.site.register(tbl_order,tbl_orderAdmin)