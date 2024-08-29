from django.db import models
from django.contrib.auth.hashers import make_password

# Permission Model
class Permission(models.Model):
    permission_name = models.CharField(max_length=100)

    def __str__(self):
        return self.permission_name

# Role Model
class Role(models.Model):
    role_name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission)  # Many-to-many relationship

    def __str__(self):
        return self.role_name

# User Model
class User(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.name
