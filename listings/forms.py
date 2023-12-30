from django.forms import ModelForm
from listings.models import Listings

class ListingsForm(ModelForm):
    class Meta:
        model = Listings
        fields = [
            'title',
            'price',
            'num_b',
            'sq_footage',
            'addess',
            'image'
        ]