from django.db import models


class SiteSettings(models.Model):
    """Общие настройки сайта"""
    site_title = models.CharField('Название сайта', max_length=100, default='КАРГОСТАР')
    site_description = models.TextField('Описание сайта',
                                        default='Комплексные решения в сфере ВЭД, сертификации и таможенного оформления')
    logo_url = models.URLField('URL логотипа', max_length=500, blank=True)

    # Контакты
    email = models.EmailField('Email', default='mail@kargostar.ru')
    phone_1 = models.CharField('Телефон 1', max_length=20, default='+7 (905) 273-10-25')
    phone_2 = models.CharField('Телефон 2', max_length=20, default='+7 (905) 234-19-59', blank=True)
    phone_3 = models.CharField('Телефон 3', max_length=20, default='+7 (921) 565-36-41', blank=True)

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.site_title

    @classmethod
    def get_settings(cls):
        """Получить единственный экземпляр настроек"""
        settings, created = cls.objects.get_or_create(pk=1)
        return settings


class Service(models.Model):
    """Модель для услуг"""

    ICON_CHOICES = [
        ('document', 'Документ'),
        ('wallet', 'Кошелек'),
        ('lamp-charge', 'Лампочка с молнией'),
        ('security', 'Безопасность'),
        ('note', 'Заметка'),
        ('autotransport', 'Автотранспорт'),
        ('case', 'Портфель'),
        ('checkmark', 'Галочка'),
    ]

    SECTION_CHOICES = [
        ('customs', 'Таможенное оформление'),
        ('permits', 'Разрешительная документация'),
        ('classification', 'Классификация и защита интересов'),
    ]

    title = models.CharField('Название услуги', max_length=200)
    icon = models.CharField('Иконка', max_length=50, choices=ICON_CHOICES, default='document')
    section = models.CharField('Раздел', max_length=50, choices=SECTION_CHOICES, default='customs')
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['section', 'order', 'title']

    def __str__(self):
        return self.title


class Advantage(models.Model):
    """Преимущества компании"""
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image_url = models.URLField('URL изображения', max_length=500)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class PageSection(models.Model):
    """Секции страниц"""

    SECTION_TYPES = [
        ('hero', 'Главный баннер'),
        ('about', 'О компании'),
        ('customs', 'Таможенное оформление'),
        ('permits', 'Разрешительная документация'),
        ('classification', 'Классификация и защита интересов'),
        ('advantages', 'Преимущества'),
        ('contacts', 'Контакты'),
    ]

    section_type = models.CharField('Тип секции', max_length=50, choices=SECTION_TYPES, unique=True)
    title = models.CharField('Заголовок', max_length=200)
    subtitle = models.TextField('Подзаголовок', blank=True)
    content = models.TextField('Содержимое', blank=True)
    background_image = models.URLField('Фоновое изображение', max_length=500, blank=True)
    is_active = models.BooleanField('Активно', default=True)

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Секция страницы'
        verbose_name_plural = 'Секции страниц'
        ordering = ['section_type']

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"


class Marketplace(models.Model):
    """Маркетплейсы для сертификации"""
    name = models.CharField('Название', max_length=100)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Маркетплейс'
        verbose_name_plural = 'Маркетплейсы'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name