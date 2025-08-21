# portfolio/views.py

from django.shortcuts import render, get_object_or_404
from .models import Profile, Project, Review
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    """
    Homepage view:
    - Fetches the user profile (with CV + profile image)
    - Fetches all projects
    - Fetches all reviews
    - Handles the contact form
    """
    profile = Profile.objects.first()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    form = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()

            # Optional: Send email notification
            send_mail(
                subject=f"New message from {message.name}",
                message=message.message,
                from_email=message.email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )

            success = True
            form = ContactForm()  # reset form after success

    # ✅ Added cv_url to context
    context = {
        'user': profile,
        'projects': projects,
        'reviews': reviews,
        'form': form,
        'success': success,
        'cv_url': profile.cv.url if profile and profile.cv else None,
    }
    return render(request, 'portfolio/home.html', context)


def project_detail(request, pk):
    """
    Project detail view
    """
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})
