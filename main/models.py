from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Info(models.Model):
    completed_projects = models.IntegerField()
    employees = models.IntegerField()
    partners = models.IntegerField()
    experience = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.pk:
            super().save(*args, **kwargs)
        else:
            existing_instance = Info.objects.first()
            if existing_instance:
                raise ValidationError("Only one instance of Info model is allowed.")
            super().save(*args, **kwargs)


class IpAddress(models.Model):
    ip = models.CharField(max_length=255)

    def __str__(self):
        return self.ip


class Portfolio(models.Model):
    name = models.CharField(max_length=150, blank=False)
    logo = models.ImageField(null=True, blank=True, upload_to='portfolio/logos')
    cover = models.ImageField(null=True, blank=True, upload_to='portfolio/covers')
    screenshots = models.ManyToManyField('PortfolioScreenshots', blank=True)
    done_things = models.ManyToManyField('PortfolioDoneThings')
    likes_count = models.IntegerField(default=0)
    views = models.ManyToManyField(IpAddress, blank=True)

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def __str__(self):
        return self.name


class PortfolioScreenshots(models.Model):
    screenshots = models.ImageField(upload_to='portfolio/screenshots')

    def __str__(self):
        return self.screenshots.name


class PortfolioDoneThings(models.Model):
    done_things = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.done_things


class Reviews(models.Model):
    company_name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    image = models.ImageField(upload_to='review_authors', blank=True, default='review_authors/default_profile_pic.jpg')
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.stars_given} by {self.company_name}'


class Services(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(blank=True, default='services/pen_tool_red.png', upload_to='services/')

    def __str__(self):
        return self.name


class ContactUsModel(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Like(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
