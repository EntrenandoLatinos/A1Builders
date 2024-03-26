import logging
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_core.models import Contact, Banner, About, Skill, Counter, Service, SubService, WorkImage, Testimonial, \
    Partner, Faq, Privacy, SocialMedia

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    contact = Contact.objects.all().last()
    banner = Banner.objects.all().last()
    about = About.objects.all().last()
    skills = Skill.objects.all().last()
    indicators = Counter.objects.all().last()
    servicios = Service.objects.all()
    works = WorkImage.objects.all().order_by('?')[:6]
    testimonials = Testimonial.objects.all().order_by('?')
    partners = Partner.objects.all()
    social_media = SocialMedia.objects.all()
    context = {
        'contact': contact,
        'banner': banner,
        'about': about,
        'skills': skills,
        'indicators': indicators,
        'servicios': servicios,
        'works': works,
        'testimonials': testimonials,
        'partners': partners,
        'social_media': social_media
    }

    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/index.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/index.html', context)


def about(request):
    contact = Contact.objects.all().last()
    about = About.objects.all().last()
    skills = Skill.objects.all().last()
    servicios = Service.objects.all()
    indicators = Counter.objects.all().last()
    testimonials = Testimonial.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    partners = Partner.objects.all()
    context = {
        'contact': contact,
        'servicios': servicios,
        'about': about,
        'indicators': indicators,
        'skills': skills,
        'testimonials': testimonials,
        'works': works,
        'social_media': social_media,
        'partners': partners
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/about.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/about.html', context)


def services(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    social_media = SocialMedia.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    context = {
        'contact': contact,
        'servicios': servicios,
        'works': works,
        'social_media': social_media
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/services.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/services.html', context)


def services_view(request, pk):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    servicio = Service.objects.get(pk=pk)
    subservicios = SubService.objects.filter(service=pk)
    works = WorkImage.objects.all().order_by('?')[:1]
    social_media = SocialMedia.objects.all()
    testimonials = Testimonial.objects.all().order_by('?')
    context = {
        'contact': contact,
        'servicio': servicio,
        'servicios': servicios,
        'subservicios': subservicios,
        'works': works,
        'social_media': social_media,
        'testimonials': testimonials
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/service.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/service.html', context)


def works(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    gallery = WorkImage.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    about = About.objects.all().last()
    context = {
        'contact': contact,
        'servicios': servicios,
        'works': gallery,
        'about': about,
        'social_media': social_media
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/works.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/works.html', context)


def faq(request):
    contact = Contact.objects.all().last()
    faqs = Faq.objects.all()
    servicios = Service.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    social_media = SocialMedia.objects.all()
    context = {
        'contact': contact,
        'servicios': servicios,
        'faqs': faqs,
        'social_media': social_media,
        'works': works
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/faq.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/faq.html', context)


def contact(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    testimonials = Testimonial.objects.all().order_by('?')
    social_media = SocialMedia.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    about = About.objects.all().last()
    context = {
        'servicios': servicios,
        'contact': contact,
        'about': about,
        'testimonials': testimonials,
        'social_media': social_media,
        'works': works
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/contact.html', context)

        elif 'contact_us_form' in request.POST:
            username = request.POST.get('userName')
            email = request.POST.get('userEmail')
            phone = request.POST.get('userPhone')
            message = request.POST.get('userMessage')
            send_msg_contact_us(username, email, phone, message)
            return render(request, 'app_core/pages/contact.html', context)
        else:
            return render(request, 'app_core/pages/contact.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/contact.html', context)


def privacy(request):
    contact = Contact.objects.all().last()
    servicios = Service.objects.all()
    privacy = Privacy.objects.all().last()
    social_media = SocialMedia.objects.all()
    works = WorkImage.objects.all().order_by('?')[:1]
    testimonials = Testimonial.objects.all().order_by('?')
    partners = Partner.objects.all()
    context = {
        'contact': contact,
        'servicios': servicios,
        'privacy': privacy,
        'social_media': social_media,
        'works': works,
        'testimonials': testimonials,
        'partners': partners
    }
    if request.method == 'POST':
        if 'stay_connected' in request.POST:
            email = request.POST.get('userEmail')
            send_msg_stay_connected(email)
            return render(request, 'app_core/pages/privacy.html', context)
    else:
        # Renderizar el template con ambos formularios
        return render(request, 'app_core/pages/privacy.html', context)


def send_msg_stay_connected(email):
    subject = 'You got a subscribe message from A1 Builders website'
    message = f'Hello A1 Builders! someone has contact you and wants to be a new subscriber: \n\nEmail: {email}.'
    from_email = 'Roofing Messenger <roofing.messenger.service@gmail.com>'
    recipient_list = ['camilobentrenandolatinos@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


def send_msg_contact_us(username, email, phone, get_message):
    subject = 'You got a contact message from A1 Builders website'
    message = f'Hello A1 Builders! you got a contact message from website: \n\nUsername: {username} \nEmail: {email} \nPhone: {phone} \n\nMessage: {get_message}'
    from_email = 'Roofing Messenger <roofing.messenger.service@gmail.com>'
    recipient_list = ['camilobentrenandolatinos@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


def mail_view(request):
    return HttpResponseRedirect(
        'https://accounts.zoho.com/signin?servicename=VirtualOffice&signupurl=https://www.zoho.com/workplace/pricing.html/')
