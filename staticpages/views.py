from django.shortcuts import render
from .models import SiteSettings, Service, Advantage, PageSection, Marketplace


def index(request):
    """Главная страница сайта КаргоСтар"""

    # Получаем настройки сайта
    settings = SiteSettings.get_settings()

    # Получаем все секции страниц
    sections = {
        section.section_type: section
        for section in PageSection.objects.filter(is_active=True)
    }

    # Получаем услуги по разделам
    customs_services = Service.objects.filter(
        section='customs',
        is_active=True
    ).order_by('order')

    permits_services = Service.objects.filter(
        section='permits',
        is_active=True
    ).order_by('order')

    classification_services = Service.objects.filter(
        section='classification',
        is_active=True
    ).order_by('order')

    # Получаем преимущества
    advantages = Advantage.objects.filter(is_active=True).order_by('order')

    # Получаем маркетплейсы
    marketplaces = Marketplace.objects.filter(is_active=True).order_by('order')

    # Подготавливаем данные для шаблона
    context = {
        'site_title': settings.site_title,
        'site_description': settings.site_description,
        'logo_url': settings.logo_url,
        'year': 2025,

        # Данные для баннера
        'hero': {
            'title': sections.get('hero').title if sections.get('hero') else settings.site_title,
            'description': sections.get('hero').content if sections.get('hero') else settings.site_description,
            'background_image': sections.get('hero').background_image if sections.get('hero') and sections.get('hero').background_image else '/static/staticpages/img/hero_background.jpg',
            'cta_text': 'Получить консультацию',
            'cta_link': '#contacts'
        },

        # О компании
        'about': {
            'title': sections.get('about').title if sections.get('about') else 'О компании',
            'subtitle': sections.get('about').subtitle if sections.get('about') else settings.site_description,
            'description': sections.get('about').content if sections.get('about') else '''Мы — команда профессионалов, предлагающая комплексные решения в сфере внешнеэкономической деятельности (ВЭД), сертификации и таможенного оформления. Наша цель — упростить для вас все процессы, связанные с международной торговлей и разрешительной документацией.

Работая на территории Российской Федерации и в рамках Евразийского экономического союза (ЕАЭС), мы обеспечиваем полный цикл сопровождения: от получения необходимых сертификатов и разрешений до оперативного и корректного таможенного оформления грузов.

Нам доверяют компании разных масштабов — от малого бизнеса до крупных предприятий. Мы ценим это доверие и всегда стремимся к тому, чтобы быть для вас надёжным партнёром, который берёт на себя весь комплекс задач во внешнеэкономической сфере.

С нами вы можете быть уверены: всё будет сделано точно, в срок и с учётом всех действующих требований законодательства.'''
        },

        # Услуги таможенного оформления
        'customs_services': {
            'title': sections.get('customs').title if sections.get('customs') else 'ТАМОЖЕННОЕ ОФОРМЛЕНИЕ',
            'subtitle': sections.get('customs').subtitle if sections.get('customs') else '''Стоимость услуг по таможенному оформлению
от 8000 рублей* за декларацию на товары.

*Стоимость услуг за таможенное оформление зависит от: географии оформления, номенклатуры, количества товаров и артикулов в декларации, количества транспортных средств и таможенной процедуры. Тариф может быть пересмотрен. Тариф не включает налог на добавленную стоимость. Не является офертой.''',
            'services': customs_services
        },

        # Разрешительная документация
        'permits': {
            'title': sections.get('permits').title if sections.get('permits') else 'РАЗРЕШИТЕЛЬНАЯ ДОКУМЕНТАЦИЯ',
            'services': permits_services,
            'marketplaces': marketplaces
        },

        # Классификация и защита интересов
        'classification': {
            'title': sections.get('classification').title if sections.get(
                'classification') else 'КЛАССИФИКАЦИЯ И ЗАЩИТА ИНТЕРЕСОВ',
            'services': classification_services
        },

        # Почему выбирают нас
        'advantages': {
            'title': sections.get('advantages').title if sections.get('advantages') else 'Почему выбирают нас?',
            'items': advantages
        },

        # Контакты
        'contacts': {
            'title': sections.get('contacts').title if sections.get('contacts') else 'КОНТАКТЫ',
            'subtitle': sections.get('contacts').subtitle if sections.get(
                'contacts') else 'Первая консультация — БЕСПЛАТНО.\nПолучите чёткий план действий и оценку сроков уже при первом обращении!',
            'phones': [phone for phone in [settings.phone_1, settings.phone_2, settings.phone_3] if phone],
            'email': settings.email
        }
    }

    return render(request, 'staticpages/index.html', context)