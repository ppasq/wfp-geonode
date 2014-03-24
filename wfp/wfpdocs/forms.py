from django import forms
from models import WFPDocument, Category
from geonode.base.models import Region
from geonode.documents.forms import DocumentForm
import datetime

#class DocumentForm(forms.Form):
#class DocumentForm(forms.ModelForm):
class DocumentForm(DocumentForm):
    publication_date = forms.DateField(initial=datetime.date.today)
    source = forms.CharField()
    orientation = forms.ChoiceField(WFPDocument.ORIENTATION_CHOICES)
    page_format = forms.ChoiceField(WFPDocument.FORMAT_CHOICES)
    categories = forms.ModelMultipleChoiceField(Category.objects.all())
    regions = forms.ModelMultipleChoiceField(Region.objects.all())
    # TODO we need to implement the logic to store metadata fields for wfpdocs!
