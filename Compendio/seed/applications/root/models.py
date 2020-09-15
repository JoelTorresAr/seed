from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


class Suscription(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    life_span = models.IntegerField(max_length=2)
    level = models.IntegerField(max_length=1)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=20)
    percentage = models.IntegerField(max_length=2)
    expiry = models.BooleanField(default=False)
    expiry_at = models.DateField(null=True)
    limit = models.BooleanField(default=False)
    limit_number = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)


class Membership(models.Model):
    suscription = models.ForeignKey(Suscription, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


