from django.shortcuts import render, get_object_or_404

from .models import Project
from .forms import ContactForm

# Create your views here.
def index(request):

    if request.method == "post":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid:
            email = contact_form.cleaned_data["email"]
            subject = contact_form.cleaned_data["subject"]
            body = contact_form.cleaned_data["body"]
            file = contact_form.cleaned_data["file"]
            # TODO: send and email to myself functionality

    return render(request, "printing/index.html", {
        "contact_form": ContactForm(),
        "projects": Project.objects.all()
    })

def project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    return render(request, "printing/project.html", {
        "project": project,
    })