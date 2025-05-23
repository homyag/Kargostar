from django.contrib import admin
from .models import SiteSettings, Service, Advantage, PageSection, Marketplace


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'email', 'phone_1', 'updated_at')
    fieldsets = (
        ('Основные настройки', {
            'fields': ('site_title', 'site_description', 'logo_url')
        }),
        ('Контакты', {
            'fields': ('email', 'phone_1', 'phone_2', 'phone_3')
        }),
    )

    def has_add_permission(self, request):
        # Разрешаем создание только если нет записей
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'icon', 'order', 'is_active')
    list_filter = ('section', 'icon', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)
    ordering = ('section', 'order')


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('section_type', 'title', 'is_active', 'updated_at')
    list_filter = ('section_type', 'is_active')
    search_fields = ('title', 'subtitle', 'content')
    fieldsets = (
        ('Основные данные', {
            'fields': ('section_type', 'title', 'subtitle')
        }),
        ('Содержимое', {
            'fields': ('content',)
        }),
        ('Дополнительно', {
            'fields': ('background_image', 'is_active')
        }),
    )


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)
    ordering = ('order',)