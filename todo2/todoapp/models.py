from django.db import models

class Todo(models.Model):
    ST = (
        ("Bajarilmadi", "Bajarilmadi"),
        ("Bajarildi", "Bajarildi"),
    )
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    time = models.TimeField(auto_now_add=True)
    joyi = models.CharField(max_length=20,blank=True)
    status = models.CharField(max_length=20,choices=ST)
    def __str__(self):
        return self.title
