# from bk_arogyam_website.first_app.views import product
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    subject = models.CharField(null=True, max_length=255, blank=False)
    mobileno = models.CharField(null=True, max_length=13, blank=False)
    messages = models.TextField(null=True)
    createdon = models.DateTimeField(null=True)


# class Po_Data(models.Model):
#     doctor_name = models.CharField(max_length=255)
#     phoneno = models.CharField(max_length=13, blank=False)
#     product = models.CharField(max_length=55555, blank=False)
#     qty = models.CharField(max_length=50, blank=False)
#     doc_messages = models.TextField(max_length=55555, null=True)
#     createdon = models.DateTimeField(null=True)



class Gallery(models.Model):
    tittle = models.CharField(max_length=255, null=True)
    gallery_img = models.ImageField(upload_to="Gallery_img", default="")
    class Meta:
        ordering = ["gallery_img"]
        verbose_name_plural = "Gallery"

class Testimonial(models.Model):
    name = models.CharField(max_length=55, null=True)
    testimonial = models.TextField(max_length=355, null=True)
    user_img = models.ImageField(upload_to="testimonial_user_img", default="")
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Testimonial"


class Doctor_Slider(models.Model):
    dc_name = models.CharField(max_length=255, default="")
    dc_img = models.ImageField(upload_to="doctor_slider", default="")
    
    class Meta:
        ordering = ["dc_name"]
        verbose_name_plural = "Doctor Slider"


class Employee_Slider(models.Model):
    ep_name = models.CharField(max_length=255, default="")
    ep_img = models.ImageField(upload_to="employee_slider", default="")

    class Meta:
        ordering = ["ep_name"]
        verbose_name_plural = "Employee Slider"

class User_Document(models.Model):
    user_tittle = models.CharField(max_length=255, default="")
    user_cover_image = models.ImageField(upload_to="user_doc/cover_img", default="")
    user_description = models.TextField(null=True)
    user_documet = models.FileField(upload_to="user_doc/doc", default="")

    class Meta:
        ordering = ["user_tittle"]
        verbose_name_plural = "User Document"


class Employee_Document(models.Model):
    employee_tittle = models.CharField(max_length=255, default="")
    employee_cover_image = models.ImageField(upload_to="employee_doc/cover_img", default="")
    employee_description = models.TextField(null=True)
    employee_documet = models.FileField(upload_to="employee_doc/doc", default="")

    class Meta:
        ordering = ["employee_tittle"]
        verbose_name_plural = "Employee Document"

class Doctor_Document(models.Model):
    doctor_tittle = models.CharField(max_length=255, default="")
    doctor_cover_image = models.ImageField(upload_to="doctor_doc/cover_img", default="")
    doctor_description = models.TextField(null=True)
    doctor_documet = models.FileField(upload_to="doctor_doc/doc", default="")

    class Meta:
        ordering = ["doctor_tittle"]
        verbose_name_plural = "Doctor Document"


class Category(models.Model):
    category = models.CharField(max_length=255, default="")
    class Meta:
        ordering = ["category"]
        verbose_name_plural = "Products Category"

    def __str__(self):
        return self.category
        


class Products(models.Model):
    product_cat=models.ForeignKey(Category,on_delete=models.PROTECT)
    product_tittle = models.CharField(max_length=255, default="")
    product_details = models.TextField(default="")
    product_price = models.IntegerField(default="")


    class Meta:
        ordering = ["product_tittle"]
        verbose_name_plural = "Products"


class Product_Order(models.Model):
    product=models.ForeignKey(Products,on_delete=models.PROTECT)
    qty=models.IntegerField()


class User_Order(models.Model):
    products=models.ManyToManyField(Product_Order, blank=True)
    doctor_name = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=13, blank=False)
    doc_messages = models.TextField(max_length=55555, null=True)

    class Meta:
        ordering = ["doctor_name"]
        verbose_name_plural = "Doctor PO"



class Career(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    address = models.CharField(null=True, max_length=255, blank=False)
    mobileno = models.CharField(null=True, max_length=13, blank=False)
    qualification = models.CharField(null=True, max_length=255,)
    applyfor = models.CharField(null=True, max_length=255,)
    img = models.FileField(upload_to="carrerimg", default="")
    createdon = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Login(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(null=True, max_length=255, blank=False)


class DoctorUser(AbstractBaseUser, PermissionsMixin):
    EMPLOYEE = 'EMPLOYEE'
    DOCTOR = 'DOCTOR'
    USER_LOGIN_TYPE = [
        (EMPLOYEE, 'Employee'),
        (DOCTOR, 'Doctor'),
    ]
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    mobileno = models.CharField(null=True, max_length=13, blank=True)
    speciality = models.CharField(null=True, max_length=50, blank=True)
    gender = models.CharField(null=True, max_length=50, blank=True)
    education_qualification = models.CharField(null=True, max_length=50, blank=True)
    registration_img = models.ImageField(upload_to="doctor_registration", default="", blank=True)
    profile_img = models.ImageField(upload_to="doctor_profile", default="", blank=True)
    experience = models.IntegerField(null=True, blank=True)
    doc_about = models.CharField(null=True, max_length=500, blank=True)

    user_type = models.CharField(
        choices=USER_LOGIN_TYPE, max_length=255, default=EMPLOYEE)
    email = models.EmailField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ["username"]
        verbose_name_plural = "Add Doctor & Employee"

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
