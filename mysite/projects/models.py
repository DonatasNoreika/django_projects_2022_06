from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    start_date = models.DateField(verbose_name='Start date', null=True)
    end_date = models.DateField(verbose_name='End date', null=True)
    client = models.ForeignKey('Client', verbose_name="Client", on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(User, verbose_name="Manager", on_delete=models.SET_NULL, null=True)
    employees = models.ManyToManyField('Employee', verbose_name="Employees")

    # cover = models.ImageField('Cover', upload_to='covers', null=True)
    # description = HTMLField('Description', null=True)

    def __str__(self):
        return f'{self.id} {self.name}'


# class ProjectComment(models.Model):
#     project = models.ForeignKey('Project', verbose_name="Project", on_delete=models.SET_NULL, null=True,
#                                 related_name='comments')
#     reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     content = models.CharField('Comment', max_length=2000)


# class Photo(models.Model):
#     photo = models.ImageField('Cover', upload_to='covers', null=True)
#     project = models.ForeignKey('Project', verbose_name="Project", on_delete=models.SET_NULL, null=True,
#                                 related_name='photos')


class Client(models.Model):
    name = models.CharField('Name', max_length=200, null=True)
    lastname = models.CharField('Lastname', max_length=200, null=True)
    company = models.CharField('Company', max_length=200)
    contacts = models.CharField('Contacts', max_length=200, null=True)

    def __str__(self):
        return f'{self.id} {self.company} {self.name} {self.lastname}'


class Employee(models.Model):
    name = models.CharField('Name', max_length=200)
    lastname = models.CharField('Lastname', max_length=200)
    position = models.CharField('Position', max_length=200, null=True)

    def __str__(self):
        return f'{self.id} {self.name} {self.lastname} {self.position}'


class Job(models.Model):
    title = models.CharField('Title', max_length=200)
    info = models.TextField('Information', null=True)
    project = models.ForeignKey('Project', verbose_name="Project", on_delete=models.CASCADE, null=True,
                                related_name='jobs')

    def __str__(self):
        return f'{self.id} {self.title}'


class Invoice(models.Model):
    date = models.DateTimeField('Date', null=True)
    info = models.TextField('Information', null=True)
    total = models.FloatField('Total')
    project = models.ForeignKey('Project', verbose_name="Project", on_delete=models.SET_NULL, null=True,
                                related_name='invoices')

    def __str__(self):
        return f'{self.id} {self.date} {self.total} {self.info}'
