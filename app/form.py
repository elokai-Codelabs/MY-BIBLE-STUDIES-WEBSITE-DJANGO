from django import forms
from .models import Project
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =['title','author','featured_image','verse_content','verse_text']
        # change tags to checkboxes
        
        # loop css styling for the page
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

    # YOU HAVE TO DO FOR EACH ATTRIBUTE, TO AVOID THAT STRESS, WRITE A FOR LOOP FOR THAT

        for name, field in self.fields.items():
             field.widget.attrs.update({'class':'input'})
