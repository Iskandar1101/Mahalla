from django.db import models


class Population(models.Model):
    SEX_CHOICE = [
        ('male', 'Erkak'),
        ('female', 'Ayol'),
    ]

    DEPUTAT_CHOICE = [
        ('resp', "Respublika"),
        ('vil', "Viloyat"),
        ('city', "Shahar/Tuman")
    ]

    FAMILY_STATUS_CHOICE = [
        ('married', "Oilali"),
        ('nomarried', "Oilasiz"),
        ('divorce', "Ajrashgan"),
        ('illegal', "Noqonuniy nikoh")
    ]

    SOCIAL_STATUS = [
        ('tdaftar', "Temir daftari"),
        ('adaftar', "Ayollar daftari"),
        ('ydaftar', "Yoshlar dartari")
    ]

    HOUSING_STATUS = [
        ('ijara', 'Ijarada'),
        ('ijarasiz', 'Noturar binoda')
    ]

    EDUCATION_CHOICE = [
        ('orta', "O'rta"),
        ('orta-maxsus', "O'rta maxsus"),
        ('oliy', 'Oliy')
    ]

    CONVICTED_CHOICE = [
        ('sud', "Sudlangan"),
        ('sudlanmagan', "Sudlanmagan")
    ]
    posbon_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255, verbose_name="Shahar/Tuman")
    quarter = models.CharField(max_length=255, verbose_name="MFY nomi")

    # qishloq fieldini qo'shaman

    person_name = models.CharField(max_length=255, verbose_name="Ism/Familiya")
    male = models.CharField(max_length=10, verbose_name="Jinsi", choices=SEX_CHOICE, default=None)
    birthdate = models.DateField(verbose_name="Tug'ilgan sana")
    passport_serie_or_id = models.CharField(max_length=15, verbose_name="Passport seriya yoki ID")
    address = models.CharField(max_length=300, verbose_name="Yashash manzili")
    registration_address = models.CharField(
        max_length=300,
        verbose_name="Doimiy yashash manzili")

    deputat = models.CharField(
        max_length=5,
        choices=DEPUTAT_CHOICE,
        verbose_name="Xalq deputatlari kengashi",
        default="Yo'q")

    family_status = models.CharField(
        max_length=10,
        choices=FAMILY_STATUS_CHOICE,
        verbose_name="Oilaviy ahvoli",
        null=True)

    invalid_group = models.CharField(max_length=30, verbose_name="Nogironligi")
    job = models.CharField(max_length=300, default="Ishsiz", verbose_name="Mehnatga layoqatligi")
    social_status = models.CharField(
        max_length=10,
        verbose_name="Ijtimoiy ahvoli",
        choices=SOCIAL_STATUS,
        null=True)

    housing = models.CharField(
        max_length=20,
        null=True,
        choices=HOUSING_STATUS,
        verbose_name="Uy-joy muhtojligi")

    education = models.CharField(
        max_length=20,
        default=EDUCATION_CHOICE[0][1],
        choices=EDUCATION_CHOICE,
        verbose_name="Ma'lumoti")

    cow = models.PositiveIntegerField(verbose_name="Qoramol, Chorva soni", null=True, default=0)
    poultry = models.PositiveIntegerField(verbose_name="Parrandalar soni", null=True, default=0)
    pet = models.PositiveIntegerField(verbose_name="It, mushuklar soni", null=True, default=0)
    convicted = models.CharField(max_length=15, choices=CONVICTED_CHOICE,  verbose_name="Sudlanganligi")
    long_time = models.CharField(max_length=10, default="Yo'q", verbose_name="Uzoq vaqtga ketgan")
    came_long_time = models.CharField(max_length=10, default="Yo'q", verbose_name="Uzoq muddatdan qaytib kelgan")
    crime = models.CharField(max_length=10, default="Yo'q", verbose_name="Jinoyat sodir etganmi")
    troubled = models.CharField(
        max_length=10,
        default="Yo'q",
        verbose_name="Notinch oila vakili")

    psychotropic = models.CharField(
        max_length=5,
        default="Yo'q",
        verbose_name="Psixotrop, narkotik modda iste'mol qiladi")

    mentally_ill = models.CharField(max_length=5, default="Yo'q", verbose_name="Ruxiy kasal")
    alcoholic_person = models.CharField(max_length=5, default="Yo'q", verbose_name="Spirtli ichimlikka ro'jo qo'ygan")
    whore_woman = models.CharField(max_length=5, default="Yo'q", verbose_name="Yengil tabiat ayol")

    posbon = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.person_name