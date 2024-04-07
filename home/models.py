from django.db import models

class Company(models.Model):
    logo = models.ImageField(upload_to='uploads/')
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    work_time = models.CharField(max_length=100)
    Facebook = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    instgram = models.CharField(max_length=100, null=True, blank=True)

class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

class Service(models.Model):
    svg = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='uploads/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='uploads/', null=True, blank=True)
    countries = models.IntegerField(max_length=100, null=True, blank=True)
    annually_tons_of_cargo = models.IntegerField(max_length=100, null=True, blank=True)
    delivery_cities = models.IntegerField(max_length=100, null=True, blank=True)
    completed_orders = models.IntegerField(max_length=100, null=True, blank=True)

class Review(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

class Video(models.Model):
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

class Process(models.Model):
    svg = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100)

class Images(models.Model):
    quote_background = models.ImageField(upload_to='uploads/')
    ask_question_background = models.ImageField(upload_to='uploads/')
    process_background = models.ImageField(upload_to='uploads/')
    track_background = models.ImageField(upload_to='uploads/', null=True, blank=True)
    track_result_background = models.ImageField(upload_to='uploads/', null=True, blank=True)
    services_page_background = models.ImageField(upload_to='uploads/', null=True, blank=True)
    about_page_background = models.ImageField(upload_to='uploads/', null=True, blank=True)
    contact_page_background = models.ImageField(upload_to='uploads/', null=True, blank=True)

class Instagram(models.Model):
    image = models.ImageField(upload_to='uploads/')
    url = models.CharField(max_length=400, null=True, blank=True)

class Footer(models.Model):
    text = models.CharField(max_length=200)

class Industry(models.Model):
    title = models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')