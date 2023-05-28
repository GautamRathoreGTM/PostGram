from django.db import models

# Create your models here.


class UserTable(models.Model):
    STATUS = (
        ("PUBLIC", "PUBLIC"),
        ("PRIVATE", "PRIVATE")
    )
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PostBlog(models.Model):
    user_id = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Like(models.Model):
    user_id = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    post_id = models.ForeignKey(PostBlog, on_delete=models.CASCADE)
    like_id = models.IntegerField(primary_key=True)
    like_status = models.BooleanField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.like_id
