from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Contact, Career, DoctorUser, Doctor_Slider, Employee_Slider, Employee_Document, Doctor_Document, Category, Gallery, Products, Testimonial, User_Document, User_Order
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


class DoctorUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = DoctorUser
    list_display = ('username', 'name', 'last_name', 'email', 'mobileno','speciality','education_qualification','experience', 'user_type', 'is_active',)
    list_filter = ('username', 'email', 'is_active',)
    fieldsets = (
        (None, {'fields': ('name','username', 'last_name', 'email','mobileno','speciality','gender','education_qualification','registration_img','profile_img','experience', 'doc_about', 'password', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',  'name', 'last_name','email', 'mobileno','speciality','gender','education_qualification','registration_img','profile_img','experience', 'doc_about', 'password1', 'password2', 'is_staff', 'is_active', 'user_type')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'mobileno',
                    'qualification', 'applyfor', 'img')
    search_fields = ('name', 'applyfor', 'email',)
    ordering = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'mobileno', 'messages',)
    search_fields = ('name', 'mobileno',)
    ordering = ('name',)


class Doctor_Slider_Admin(admin.ModelAdmin):
    list_display = ('dc_name', 'dc_img',)


class Employee_Slider_Admin(admin.ModelAdmin):
    list_display = ('ep_name', 'ep_img',)

class User_Document_Admin(admin.ModelAdmin):
    list_display = ('user_tittle', 'user_cover_image',
                    'user_description', 'user_documet',)

class Employee_Document_Admin(admin.ModelAdmin):
    list_display = ('employee_tittle', 'employee_cover_image',
                    'employee_description', 'employee_documet',)


class Doctor_Document_Admin(admin.ModelAdmin):
    list_display = ('doctor_tittle', 'doctor_cover_image',
                    'doctor_description', 'doctor_documet',)

class Product_Category_Admin(admin.ModelAdmin):
    list_display = ('category',)

class Products_Admin(admin.ModelAdmin):
    list_display = ('product_cat','product_tittle', 'product_details', 'product_price',)


class User_Order_Admin(admin.ModelAdmin):
    list_display = ('id' ,'products_and_qty','doctor_name', 'phoneno', 'doc_messages',)

    def products_and_qty(self, obj):
        return ", ".join([str(p.product.product_tittle)+" - "+str(p.qty) for p in obj.products.all()])


class Gallery_Admin(admin.ModelAdmin):
    list_display = ('tittle','gallery_img',)
    search_fields = ('tittle','gallery_img',)
    ordering = ('gallery_img',)


class Testimonial_Admin(admin.ModelAdmin):
    list_display = ('name','testimonial', 'user_img',)
    search_fields = ('name','testimonial',)
    ordering = ('name',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(DoctorUser, DoctorUserAdmin)
admin.site.register(Doctor_Slider, Doctor_Slider_Admin)
admin.site.register(Employee_Slider, Employee_Slider_Admin)
admin.site.register(Employee_Document, Employee_Document_Admin)
admin.site.register(Doctor_Document, Doctor_Document_Admin)
admin.site.register(Category, Product_Category_Admin)
admin.site.register(Products, Products_Admin)
admin.site.register(User_Document, User_Document_Admin)
admin.site.register(User_Order, User_Order_Admin)
admin.site.register(Gallery, Gallery_Admin)
admin.site.register(Testimonial, Testimonial_Admin)