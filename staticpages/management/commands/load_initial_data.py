from django.core.management.base import BaseCommand
from staticpages.models import SiteSettings, Service, Advantage, PageSection, Marketplace


class Command(BaseCommand):
    help = 'Загружает начальные данные для сайта КаргоСтар'

    def handle(self, *args, **options):
        self.stdout.write('Загружаем данные...')

        # Создаем настройки сайта
        settings, created = SiteSettings.objects.get_or_create(
            pk=1,
            defaults={
                'site_title': 'КАРГОСТАР',
                'site_description': 'Комплексные решения в сфере ВЭД, сертификации и таможенного оформления',
                'logo_url': 'https://images.reg.solutions/x70/https://files.reg.solutions/23-05-2025/7b05e480-0170-4851-bbb3-e5a29b946145-Без заголовка.png',
                'email': 'mail@kargostar.ru',
                'phone_1': '+7 (905) 273-10-25',
                'phone_2': '+7 (905) 234-19-59',
                'phone_3': '+7 (921) 565-36-41',
            }
        )
        if created:
            self.stdout.write('✓ Настройки сайта созданы')

        # Создаем секции страниц
        sections_data = [
            {
                'section_type': 'hero',
                'title': 'КАРГОСТАР',
                'content': 'Комплексные решения в сфере ВЭД, сертификации и таможенного оформления',
                'background_image': 'https://images.reg.solutions/1000x/https://files.reg.solutions/675eb099-5b19-4d6e-a3dc-50b4490b7d69/images/1b6c4298-1856-4b9b-9b94-69cce7a7b638-logistics-means-transport-together-with-technological-futuristic-holograms.jpg',
            },
            {
                'section_type': 'about',
                'title': 'О компании',
                'subtitle': 'Комплексные решения в сфере ВЭД, сертификации и таможенного оформления',
                'content': '''Мы — команда профессионалов, предлагающая комплексные решения в сфере внешнеэкономической деятельности (ВЭД), сертификации и таможенного оформления. Наша цель — упростить для вас все процессы, связанные с международной торговлей и разрешительной документацией.

Работая на территории Российской Федерации и в рамках Евразийского экономического союза (ЕАЭС), мы обеспечиваем полный цикл сопровождения: от получения необходимых сертификатов и разрешений до оперативного и корректного таможенного оформления грузов.

Нам доверяют компании разных масштабов — от малого бизнеса до крупных предприятий. Мы ценим это доверие и всегда стремимся к тому, чтобы быть для вас надёжным партнёром, который берёт на себя весь комплекс задач во внешнеэкономической сфере.

С нами вы можете быть уверены: всё будет сделано точно, в срок и с учётом всех действующих требований законодательства.''',
            },
            {
                'section_type': 'customs',
                'title': 'ТАМОЖЕННОЕ ОФОРМЛЕНИЕ',
                'subtitle': '''Стоимость услуг по таможенному оформлению
от 8000 рублей* за декларацию на товары.

*Стоимость услуг за таможенное оформление зависит от: географии оформления, номенклатуры, количества товаров и артикулов в декларации, количества транспортных средств и таможенной процедуры. Тариф может быть пересмотрен. Тариф не включает налог на добавленную стоимость. Не является офертой.''',
            },
            {
                'section_type': 'permits',
                'title': 'РАЗРЕШИТЕЛЬНАЯ ДОКУМЕНТАЦИЯ',
            },
            {
                'section_type': 'classification',
                'title': 'КЛАССИФИКАЦИЯ И ЗАЩИТА ИНТЕРЕСОВ',
            },
            {
                'section_type': 'advantages',
                'title': 'Почему выбирают нас?',
            },
            {
                'section_type': 'contacts',
                'title': 'КОНТАКТЫ',
                'subtitle': 'Первая консультация — БЕСПЛАТНО.\nПолучите чёткий план действий и оценку сроков уже при первом обращении!',
            },
        ]

        for section_data in sections_data:
            section, created = PageSection.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'✓ Секция "{section.get_section_type_display()}" создана')

        # Создаем услуги
        services_data = [
            # Таможенное оформление
            {
                'title': 'Импорт / экспорт — от подачи ДТ до выпуска товара',
                'icon': 'document',
                'section': 'customs',
                'order': 1,
            },
            {
                'title': 'Сопровождение сделок, расчёт пошлин',
                'icon': 'wallet',
                'section': 'customs',
                'order': 2,
            },
            {
                'title': 'Консультации по логистике и оптимизации затрат',
                'icon': 'lamp-charge',
                'section': 'customs',
                'order': 3,
            },
            # Разрешительная документация
            {
                'title': 'Декларации о соответствии ТР ТС — от 5000 ₽ / 1 день',
                'icon': 'document',
                'section': 'permits',
                'order': 1,
            },
            {
                'title': 'Сертификаты ТР ТС, ГОСТ Р, добровольные отказные письма, заключения лабораторий',
                'icon': 'security',
                'section': 'permits',
                'order': 2,
            },
            {
                'title': 'Сертификация для маркетплейсов',
                'icon': 'note',
                'section': 'permits',
                'order': 3,
            },
            {
                'title': 'ЭПТС, СБКТС, ЭПСМ для автотехники и спецтехники',
                'icon': 'autotransport',
                'section': 'permits',
                'order': 4,
            },
            # Классификация и защита интересов
            {
                'title': 'Определение кода ТН ВЭД',
                'icon': 'lamp-charge',
                'section': 'classification',
                'order': 1,
            },
            {
                'title': 'Подготовка экспертных заключений',
                'icon': 'security',
                'section': 'classification',
                'order': 2,
            },
            {
                'title': 'Подтверждение таможенной стоимости',
                'icon': 'note',
                'section': 'classification',
                'order': 3,
            },
            {
                'title': 'Представление ваших интересов в ФТС',
                'icon': 'case',
                'section': 'classification',
                'order': 4,
            },
        ]

        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'✓ Услуга "{service.title}" создана')

        # Создаем преимущества
        advantages_data = [
            {
                'title': 'Оперативность',
                'description': 'От обращения до готового документа - 1 рабочий день',
                'image_url': 'https://images.reg.solutions/200x200/https://files.reg.solutions/675eb099-5b19-4d6e-a3dc-50b4490b7d69/images/03e9734f-0f6c-460e-a0ff-730fbf8b7ea6-lightning_thunderbolt_thunder_icon_185978.png',
                'order': 1,
            },
            {
                'title': 'Прозрачность',
                'description': 'Без скрытых платежей и навязанных услуг',
                'image_url': 'https://images.reg.solutions/200x200/https://files.reg.solutions/675eb099-5b19-4d6e-a3dc-50b4490b7d69/images/8542e097-e002-4fef-81e5-041500a5d918-shield_icon_185994.png',
                'order': 2,
            },
            {
                'title': 'Компетентность',
                'description': 'Юристы и специалисты с 10+ лет опыта в ВЭД',
                'image_url': 'https://images.reg.solutions/200x200/https://files.reg.solutions/675eb099-5b19-4d6e-a3dc-50b4490b7d69/images/ed0359b3-5738-4c29-a92c-61817c45a616-education_graduate_cap_hat_university_student_icon_185968.png',
                'order': 3,
            },
        ]

        for advantage_data in advantages_data:
            advantage, created = Advantage.objects.get_or_create(
                title=advantage_data['title'],
                defaults=advantage_data
            )
            if created:
                self.stdout.write(f'✓ Преимущество "{advantage.title}" создано')

        # Создаем маркетплейсы
        marketplaces_data = [
            {'name': 'Wildberries', 'order': 1},
            {'name': 'Ozon', 'order': 2},
            {'name': 'Яндекс.Маркет', 'order': 3},
        ]

        for marketplace_data in marketplaces_data:
            marketplace, created = Marketplace.objects.get_or_create(
                name=marketplace_data['name'],
                defaults=marketplace_data
            )
            if created:
                self.stdout.write(f'✓ Маркетплейс "{marketplace.name}" создан')

        self.stdout.write(
            self.style.SUCCESS('Все данные успешно загружены!')
        )