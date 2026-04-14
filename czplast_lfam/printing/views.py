from django.shortcuts import render, get_object_or_404
from django import forms

from .models import Project

class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(required=False)

# Create your views here.
def index(request):

    if request.method == "post":
        pass # TODO

    return render(request, "printing/index.html", {
        "contact_form": ContactForm(),
        "projects": Project.objects.all()
    })

def project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    return render(request, "printing/project.html", {
        "project": project,
    })