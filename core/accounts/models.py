from django.db import models

class Post(models.Model):
    '''
    This is to save details of blog posts.
    
    '''
    author = models.ForeignKey('User', 
                               on_delete=models.CASCADE )
    
    category = models.ForeignKey('Category', 
                                 on_delete=models.SET_NULL, 
                                 null=True, 
                                 blank=True )
    
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    