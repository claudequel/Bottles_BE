# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    pw = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    preface = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'