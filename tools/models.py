from django.db import models

# Create your models here.

class AiTool(models.Model):

    name=models.CharField(max_length=200,unique=True)

    company=models.CharField(max_length=200)

    purpose=models.TextField()

    current_version=models.CharField(max_length=200)

    CATEGORY_OPTIONS=(
        ("chat","chat"),
        ("ai search","ai search"),
        ("image generation","image generation"),
        ("vedio generation","vedio generation"),
        ("coding assistant","coding assistant"),
        ("document","document"),
        ("multi model","multi model"),
        ("other","other")
    )

    category=models.CharField(max_length=200,choices=CATEGORY_OPTIONS,default="chat")

    
    #__str__ string representation of an object
    
    def __str__(self):

        return self.name




