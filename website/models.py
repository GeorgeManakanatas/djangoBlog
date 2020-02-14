from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class StaticText(models.Model):
    """ Class defining the model for storing the blog static content """
    services_general = models.CharField(max_length=8000, help_text='The general services desciption')
    services_webdesign = models.CharField(max_length=8000, help_text='The webdesign services desciption')
    services_branding = models.CharField(max_length=8000, help_text='The branding services desciption')
    services_photography = models.CharField(max_length=8000, help_text='The photography services desciption')
    services_development = models.CharField(max_length=8000, help_text='The development services desciption')
    services_ui = models.CharField(max_length=8000, help_text='The ui services desciption')
    services_printing = models.CharField(max_length=8000, help_text='The printing services desciption')
    portfolio_general = models.CharField(max_length=8000, help_text='The portfolio general desciption')

    def __str__(self):
        return self.services_general

class ContentCreator(models.Model):
    """ Class defining the model for peole creating content on the blog """
    creator_first_name = models.CharField(max_length=30, help_text='The person first name')
    creator_middle_name = models.CharField(max_length=30, help_text='The person middle name')
    creator_last_name = models.CharField(max_length=30, help_text='The person last name')
    creator_email = models.EmailField()
    creator_profile_pic = models.BinaryField() # may change this to imagefield in the future depending\


class BlogPost(models.Model):
    """ Class defining the model for a single blog post """
    # Fields
    post_title = models.CharField(max_length=300, help_text='The title of the post')
    post_text = models.CharField(max_length=8000, help_text='The contents of the post')
    content_creator = models.ForeignKey(ContentCreator, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    comments = JSONField()
    post_image = models.BinaryField()



class Tags(models.Model):
    """"""
    tag = models.CharField(max_length=50,help_text='The tag text')


class Categories(models.Model):
    """"""
    Category_name = models.CharField(max_length=50,help_text='The category name')

class PostTagAssociation(models.Model):
    """"""
    post_key = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    tag_key = models.ForeignKey(Tags, on_delete=models.CASCADE)


class PostCategoriesAssociation(models.Model):
    """"""
    post_key = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    category_key = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    # Metadata
    # Methods