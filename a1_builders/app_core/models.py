from django.db import models

# Create your models here.
import os
from django.db import models
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from ckeditor.fields import RichTextField

# Opciones para el campo de selección
CATEGORY_CHOICES = [
    ('01', 'Roofing'),
    ('02', 'Flat Roofing'),
    ('04', 'Siding'),
    ('05', 'Gutter'),
    ('06', 'Window'),
    ('07', 'Carpentry'),
    ('08', 'Remodeling'),
]

SOCIAL_MEDIA_CHOICES = [
    ('01', 'Facebook'),
    ('02', 'Twitter'),
    ('03', 'Instagram'),
    ('04', 'TikTok'),
    ('05', 'YouTube'),
    ('06', 'LinkedIn'),
]

STARS_REVIEW_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

FLATICON_ICONS_CHOICES = [
    ('01', 'flaticon-factory'),
    ('02', 'flaticon-factory-1'),
    ('03', 'flaticon-engineer'),
    ('04', 'flaticon-valve'),
    ('05', 'flaticon-conveyor'),
    ('06', 'flaticon-oil'),
    ('07', 'flaticon-truck'),
    ('08', 'flaticon-forklift'),
    ('09', 'flaticon-voltmeter'),
    ('10', 'flaticon-fuel-truck'),
    ('11', 'flaticon-gear'),
    ('12', 'flaticon-fuel-station'),
    ('13', 'flaticon-robotic-arm'),
    ('14', 'flaticon-product'),
    ('15', 'flaticon-worker'),
    ('16', 'flaticon-robot-arm'),
    ('17', 'flaticon-help'),
    ('18', 'flaticon-conveyor-1'),
    ('19', 'flaticon-factory-2'),
    ('20', 'flaticon-optimization'),
    ('21', 'flaticon-wrench'),
    ('22', 'flaticon-crane'),
    ('23', 'flaticon-engineer-1'),
    ('24', 'flaticon-design-tools'),
    ('25', 'flaticon-construction'),
    ('26', 'flaticon-settings'),
    ('27', 'flaticon-idea'),
    ('28', 'flaticon-calculator'),
    ('29', 'flaticon-cpu'),
    ('30', 'flaticon-repair-tools'),
    ('31', 'flaticon-internet'),
    ('32', 'flaticon-analytics'),
    ('33', 'flaticon-printer'),
    ('34', 'flaticon-helmet'),
    ('35', 'flaticon-presentation'),
    ('36', 'flaticon-alarm-clock'),
    ('37', 'flaticon-bar-chart'),
    ('38', 'flaticon-microphone'),
    ('39', 'flaticon-shield'),
    ('40', 'flaticon-loupe'),
    ('41', 'flaticon-settings-1'),
    ('42', 'flaticon-monitor'),
    ('43', 'flaticon-shopping-cart'),
    ('44', 'flaticon-home'),
    ('45', 'flaticon-message'),
    ('46', 'flaticon-heart'),
    ('47', 'flaticon-user'),
    ('48', 'flaticon-play-button'),
    ('49', 'flaticon-planet-earth'),
    ('50', 'flaticon-settings-2'),
]

# Create your models here.
class AuditoriaFecha(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AuditoriaFecha):
    location = models.CharField("Location", max_length=300, null=True, blank=True)
    city = models.CharField("City", max_length=100, null=True, blank=True)
    phone1 = models.CharField("Phone 2", max_length=60, null=True, blank=True)
    phone2 = models.CharField("Phone 1", max_length=60, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    latitude = models.FloatField("latitude", null=True, blank=True)
    longitude = models.FloatField("longitude", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.email))

    class Meta:
        ordering = ['id']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Banner(AuditoriaFecha):
    image = models.ImageField(upload_to='banner/', null=True, blank=True)
    title = models.CharField("Banner title", max_length=300, null=True, blank=True, default="")
    title2 = models.CharField("Banner title2", max_length=300, null=True, blank=True, default="")
    subtitle = models.CharField("Banner subtitle", max_length=300, null=True, blank=True, default="")
    description = models.TextField("Description", max_length=300, null=True, blank=True)
    insurance = models.CharField("Insurance", max_length=300, null=True, blank=True, default="")

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class About(AuditoriaFecha):
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    image_mission_vision = models.ImageField(upload_to='about/', null=True, blank=True)
    about = RichTextField("About", null=True, blank=True)
    mision = RichTextField("Mission", null=True, blank=True)
    vision = RichTextField("Vision", null=True, blank=True)
    image_google = models.ImageField(upload_to='about/', null=True, blank=True)
    url_google = models.URLField("URL Google Business", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.id))

    class Meta:
        ordering = ['id']
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class Skill(AuditoriaFecha):
    title1 = models.CharField("Skill title 1", max_length=300, null=True, blank=True)
    description1 = models.TextField("Description 1", null=True, blank=True)
    title2 = models.CharField("Skill title 2", max_length=300, null=True, blank=True)
    description2 = models.TextField("Description 2", null=True, blank=True)
    title3 = models.CharField("Skill title 3", max_length=300, null=True, blank=True)
    description3 = models.TextField("Description 3", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title1))

    class Meta:
        ordering = ['id']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Counter(AuditoriaFecha):
    title1 = models.CharField("Title 1", max_length=300, null=True, blank=True)
    number1 = models.IntegerField("Number 1", null=True, blank=True)
    symbol1 = models.CharField("Symbol 1", max_length=300, null=True, blank=True)
    title2 = models.CharField("Title 2", max_length=300, null=True, blank=True)
    number2 = models.IntegerField("Number 2", null=True, blank=True)
    symbol2 = models.CharField("Symbol 2", max_length=300, null=True, blank=True)
    title3 = models.CharField("Title 3", max_length=300, null=True, blank=True)
    number3 = models.IntegerField("Number 3", null=True, blank=True)
    symbol3 = models.CharField("Symbol 3", max_length=300, null=True, blank=True)
    title4 = models.CharField("Title 4", max_length=300, null=True, blank=True)
    number4 = models.IntegerField("Number 4", null=True, blank=True)
    symbol4 = models.CharField("Symbol 4", max_length=300, null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title1))

    class Meta:
        ordering = ['id']
        verbose_name = 'Counter'
        verbose_name_plural = 'Counters'


class Service(AuditoriaFecha):
    image = models.ImageField(upload_to='service/', null=True, blank=True)
    image_large = models.ImageField(upload_to='service/', null=True, blank=True)
    icon = models.CharField("Icon", max_length=2, choices=FLATICON_ICONS_CHOICES, null=True, blank=True)
    title = models.CharField("Service Name", max_length=300, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)
    description_finish = RichTextField("Finish Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class SubService(AuditoriaFecha):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_subservice')
    image = models.ImageField(upload_to='subservice/', null=True, blank=True)
    title = models.CharField("Subservice Name", max_length=300, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'SubService'
        verbose_name_plural = 'SubServices'


class WorkImage(AuditoriaFecha):
    category = models.CharField("Category", null=True, blank=True, max_length=2, choices=CATEGORY_CHOICES)
    title = models.CharField("Image title", max_length=300, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    image = models.ImageField(upload_to='work_image/')

    def __str__(self):
        return "{0}".format(str(self.title))

    def bytes_to_mb(self, bytes):
        mb = bytes / 1000000
        return mb

    def save(self, *args, **kwargs):
        if not self._state.adding:
            super().save(*args, **kwargs)
            return
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        # Obtiene el tamaño de la imagen en bytes
        image_size = os.path.getsize(self.image.path)
        img_size_mb = self.bytes_to_mb(image_size)

        if img_size_mb < 1:
            img_quality = 50
        elif img_size_mb > 3:
            img_quality = 18
        else:
            img_quality = 30

        # Obtiene el ancho y alto de la imagen
        width, height = img.size
        if width > 1920 or height > 1920:
            # Definir el nuevo ancho máximo
            max_size = 1920
            # Redimensionar la imagen con el ancho máximo proporcionado
            img.thumbnail((max_size, max_size))

        img.save(self.image.path, quality=img_quality)

    class Meta:
        ordering = ['id']
        verbose_name = 'WorkImage'
        verbose_name_plural = 'WorkImages'


@receiver(pre_delete, sender=WorkImage)
def delete_gallery_image(sender, instance, **kwargs):
    file_path = instance.image.path
    if os.path.exists(file_path):
        os.remove(file_path)


class Testimonial(AuditoriaFecha):
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)
    name = models.CharField("Name", max_length=300, null=True, blank=True)
    location = models.CharField("Location", max_length=300, null=True, blank=True)
    stars = models.CharField("Stars", max_length=1, choices=STARS_REVIEW_CHOICES, null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.name))

    class Meta:
        ordering = ['id']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class Partner(AuditoriaFecha):
    image = models.ImageField(upload_to='partner/', null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.id))

    class Meta:
        ordering = ['id']
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


class Faq(AuditoriaFecha):
    title = models.CharField("Title", max_length=300, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'


class Privacy(AuditoriaFecha):
    title = models.CharField("Title", max_length=300, null=True, blank=True)
    description = RichTextField("Description", null=True, blank=True)

    def __str__(self):
        return "{0}".format(str(self.title))

    class Meta:
        ordering = ['id']
        verbose_name = 'Privacy'
        verbose_name_plural = 'Privacies'


class SocialMedia(AuditoriaFecha):
    name = models.CharField("Name", max_length=2, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField("URL")
    icon_class = models.CharField("Icon class", max_length=150)
    icon_class_footer = models.CharField("Icon class footer", max_length=150)

    def __str__(self):
        return "{0}".format(str(self.get_name_display()))

    class Meta:
        ordering = ['id']
        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'