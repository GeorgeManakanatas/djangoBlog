from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class BlogPost(models.Model):
    """ Class defining the model for a single blog post """
    # Fields
    post_title = models.CharField(max_length=300, help_text='The title of the post')
    post_text = models.CharField(max_length=8000, help_text='The contents of the post')
    content_creator = models.CharField(max_length=100, help_text='The identity of the post creator')
    date_published = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    comments = JSONField()
    post_image = models.BinaryField()


class ContentCreator(models.Model):
    """ Class defining the model for peole creating content on the blog """
    creator_first_name = models.CharField(max_length=30, help_text='The person first name')
    creator_middle_name = models.CharField(max_length=30, help_text='The person middle name')
    creator_last_name = models.CharField(max_length=30, help_text='The person last name')
    creator_email = models.EmailField()
    creator_profile_pic = models.BinaryField() # may change this to imagefield in the future depending


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