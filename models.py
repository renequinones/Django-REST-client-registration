from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Clients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200)
    email_address = models.CharField(max_length=50)
    created = models.DateTimeField(default=True)

class Meta:
    ordering = ('name',)
    verbose_name = 'client'
    verbose_name_plural = 'clients'

def __str__(self):
    return self.name



class SocialApplication(models.Model):
    user = models.ForeignKey(Clients,
                              related_name='clients',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'social application'
        verbose_name_plural = 'social applications'

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category,
                                  related_name='products',
                                  on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=True)
    updated = models.DateTimeField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name




# Create your models here.
