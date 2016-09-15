from django.db import models

#Post models
class post(models.Model):
    post_title = models.CharField(max_length=200)
    post_author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    post_article = models.TextField(max_length=10000)
    post_img = models.FileField()

    def __str__(self):
        return "" + self.post_title + " | " + self.post_author
