"""
Abstract models for the product images app
"""

from django.db import models
from django.utils.translation import ugettext as _


class AbstractImage(models.Model):
    """
    An image of a product  
    """
    product = models.ForeignKey('product.Item', related_name='images')
    path = models.ImageField(upload_to='product-images/%Y/%m/')
    # Use display_order to determine which is the "primary" image
    display_order = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def is_primary(self):
        return self.display_order == 0
    
    class Meta:
        abstract = True

    def __unicode__(self):
        return "Image of '%s'" % self.product

