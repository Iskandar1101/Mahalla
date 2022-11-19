from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


# class CustomUserManager(BaseUserManager):
#
#     def create_user(self, username, password=None, **extra_fields):  # **kwargs
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         user = self.model.objects.create(username=username, **extra_fields)  # create(email=email, a=1, b=2)
#         if password:
#             user.set_password(password)
#             user.save()
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(username, password, **extra_fields)
#
#     @property
#     def get_mahalla(self):
#         return MahhalaFY.objects.get(staff_member__username=self.username)


class User(AbstractUser):
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='regions', blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField('Username',max_length=50, unique=True)
    is_staff = models.BooleanField(default=False,
                                   help_text='Designates whether the user can log into this admin site.',
                                   )
    is_active = models.BooleanField('active', default=True,
                                    help_text=(
                                        'Designates whether this user should be treated as active. '
                                        'Unselect this instead of deleting accounts.'
                                    ),
                                    )
    date_joined = models.DateTimeField('Date joined', default=timezone.now)

    USERNAME_FIELD = 'username'  # null=False, unique=True

    REQUIRED_FIELDS = []

    @property
    def get_mahalla(self):
        return MahhalaFY.objects.get(staff_member__username=self.username)


    def __str__(self):
        return self.username


class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tuman/Shahar nomi")
    quarters = models.ManyToManyField('MahhalaFY', blank=True, verbose_name="Mahalla")

    def __str__(self):
        return self.name


# class Posbon(User):
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, related_query_name='region', related_name='regions')
#
#     @property
#     def _get_mahalla(self):
#         mahalla = MahhalaFY.objects.get(staff_member__username=self.username)
#         return mahalla.quarter_name
#
#     def save(self, *args, **kwargs):
#         self.is_staff = True
#         self.password = make_password(self.password)
#         super(Posbon, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return f'{self.username}'
#
#     class Meta:
#         db_table = 'Posbon'


class MahhalaFY(models.Model):
    quarter_name = models.CharField(max_length=255, verbose_name="MFY nomi")
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Shahar")
    staff_member = models.OneToOneField(
        'User',
        verbose_name="Mahalla Posboni",
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True, 'is_superuser': False},
        primary_key=True,
        related_name='posbonbek'
    )

    def __str__(self):
        return f'{self.quarter_name} mahallasi'



