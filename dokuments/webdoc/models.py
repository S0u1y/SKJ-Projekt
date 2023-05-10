from django.db import models


# from django.contrib.auth.models import AbstractUser

# Create your models here.

# model = models.Model


class Address(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Could've created a new user type, but I just had no time
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)

    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    password = models.CharField(max_length=1000)
    permission = models.CharField(max_length=1)
    phone = models.CharField(max_length=15)

    activeUntil = models.DateField('active until', auto_now_add=True)

    def __str__(self):
        return self.email


class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_number_of_pages(self):
        return Page.objects.filter(document=self).count()


class Page(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f'{self.document.title}, ' + str(self.page_number)

    def get_next_page_number(self):
        if len(Page.objects.all()) > self.page_number:
            return Page.objects.get(id=self.id).page_number + 1

        return self.page_number

    def get_prev_page_number(self):
        if 1 < self.page_number:
            return Page.objects.get(id=self.id).page_number - 1

        return self.page_number


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    date = models.DateTimeField('date commented', auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.document.title}, {self.user.email}'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateTimeField('date bought', auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return f'{self.user.email}, {self.date}'
