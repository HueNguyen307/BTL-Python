from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    description = models.TextField()
    link = models.CharField(max_length=200, default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(default='')
    image_link = models.ImageField(upload_to='static/Product_image/%y/%m/%d', default=None)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', related_name='products', blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
