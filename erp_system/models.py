from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=_('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=_('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=_('Updated by'))

    class Meta:
        abstract = True

    def get_required_fields(self):
        fields = self._meta.get_fields()
        required_fields = []

        # Required means `blank` is False
        for f in fields:
            # Note - if the field doesn't have a `blank` attribute it is probably
            # a ManyToOne relation (reverse foreign key), which you probably want to ignore.
            if hasattr(f, 'blank') and f.blank is False:
                required_fields.append(f)
        return required_fields

    def get_required_fields_as_names(self):
        str_required_field_names = []
        required_fields = self.get_required_fields()
        for required_field in required_fields:
            str_required_field_names.append(required_field.name)
        return str_required_field_names


class Country(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Country Name'))
    name_slug = models.SlugField(max_length=280, blank=True, null=True, verbose_name=_('Country Slug Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Country Description'))
    area = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Country Area'))
    population = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Country Population'))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return f'Country Name: {self.name}'


    @property
    def dictionary_parse(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'area': self.area,
            'population': self.population
        }

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Employee(BaseModel):
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Last Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, null=True, verbose_name=_('Country'))
    RANKS = (
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    
    rank = models.CharField(max_length=1, choices=RANKS, blank=True, null=True, verbose_name=_('Rank'))
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name=_('E-Mail'))
    point = models.IntegerField(default=0, blank=True, null=True, verbose_name=_('Point'))
    
    def __str__(self):
        return f'Employee Full Name: {self.last_name} {self.first_name}'

    @property
    def dictionary_parse(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'description': self.description,
            'country': self.country,
            'rank': self.rank,
            'email': self.email,
            'point': self.point
        }

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
