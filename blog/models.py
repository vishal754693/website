from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    public_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]  # Return the first 100 characters of the body as a summary


    def pub_date(self):
        return self.public_date.strftime('%b %e %Y')


    def __str__(self):
        return self.title
