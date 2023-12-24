from django import forms
from . import models 
from PIL import Image
from django.core.exceptions import ValidationError




class BlogPostForm(forms.ModelForm):


    class Meta:
        model = models.BlogPost
        fields = ['titulo', 'subtitulo', 'contenido', 'post_image']

    # image size conditions #
    
    def clean_post_image(self):
        post_image = self.cleaned_data.get('post_image')

        if post_image:
            # Open the image using Pillow
            img = Image.open(post_image)
            
            # Set the minimum required width and height
            min_width = 800
            min_height = 600
            
            # Check if the image meets the minimum size requirements
            if img.width < min_width or img.height < min_height:
                raise ValidationError(
                    f'The image dimensions must be at least {min_width}x{min_height} pixels.'
                )

        return post_image