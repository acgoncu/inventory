import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):

        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Request(models.Model):
    requester=models.ForeignKey('auth.User',related_name='Requester',on_delete=models.PROTECT)
    request_date=models.DateField(default=datetime.date.today)
    branch=models.ForeignKey('Location',on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    description=models.CharField(max_length=200)
    product_ID=models.CharField(max_length=50,blank=True,null=True)
    unit_price=models.DecimalField(decimal_places=2,max_digits=10)
    reason=models.TextField()
    vendor=models.ForeignKey('Vendor',on_delete=models.PROTECT)
    approver=models.ForeignKey('Approver',on_delete=models.PROTECT,blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    munis_GL_number=models.PositiveIntegerField(blank=True,null=True)
    munis_PO_number=models.PositiveIntegerField(blank=True,null=True)
    munis_PO_date=models.DateField(blank=True,null=True)
    receive_date=models.DateField(blank=True,null=True)
    receiver=models.ForeignKey('auth.User',related_name='Receiver',on_delete=models.PROTECT,blank=True,null=True)
    order_status=models.ForeignKey('Status',on_delete=models.PROTECT,default=6)
    def __str__(self):
        return self.description

class Location(models.Model):
    branch=models.CharField(max_length=200)
    def __str__(self):
        return self.branch

class Department(models.Model):
    department=models.CharField(max_length=200)
    def __str__(self):
        return self.department

class Status(models.Model):
    class Meta:
        verbose_name_plural='statuses'
    status=models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Vendor(models.Model):
    VendorName=models.CharField(max_length=200)
    VendorWebsite=models.CharField(max_length=200)
    VendorPhone=models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.VendorName

class Purchase(models.Model):
    purchase_request=models.ForeignKey('Request',on_delete=models.PROTECT,default=1)
    purchaser=models.ForeignKey('auth.User',on_delete=models.PROTECT)
    purchase_date=models.DateField(default=datetime.date.today)
    account=models.PositiveIntegerField()
    def __str__(self):
        return str(self.purchase_request)

class Product(models.Model):
    order=models.ForeignKey('Request',on_delete=models.PROTECT,blank=True,null=True)
    quantity=models.PositiveSmallIntegerField()
    manufacturer=models.CharField(max_length=100)
    model_num=models.CharField(max_length=50,blank=True,null=True)
    description=models.CharField(max_length=200)
    purpose=models.TextField()
    serial_number=models.CharField(max_length=100,blank=True,null=True)
    tag_number=models.CharField(max_length=25,blank=True,null=True)
    branch=models.ForeignKey('Location',on_delete=models.PROTECT)
    department=models.ForeignKey('Department',on_delete=models.PROTECT)
    place=models.CharField(max_length=200,blank=True,null=True)
    comments=models.TextField(default='',blank=True,null=True)
    def __str__(self):
        return self.description

class Approver(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

#Simple is better than complex tutorial
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

#Django Girls tutorial
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

