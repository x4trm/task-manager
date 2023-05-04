from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=100)
    color_code=models.CharField(max_length=7)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
    
class Task(models.Model):
    PRIORITY_CHOICES =[
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High')
    ]
    category = models.ForeignKey(Category,related_name='tasks',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    deadline = models.DateTimeField(auto_now_add=False)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES)

    class Meta:
        ordering = ('-deadline',)
        verbose_name_plural = "Tasks"
    def __str__(self):
        return self.name
