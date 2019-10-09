from django.contrib import admin
from . models import ShowcaseIntro, Service, About, Skill, Portfolio, Testimonial, Contact, Footer

# Register your models here.


class ShowcaseIntroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job1', 'job2')
    list_display_links = ('id', 'name', 'job1', 'job2')
    list_filter = ('name', 'job1', 'job2')
    search_fields = ('name', 'job1', 'job2')
    list_per_page = 25


admin.site.register(ShowcaseIntro, ShowcaseIntroAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'text')
    list_display_links = ('id', 'profession', 'text')
    list_filter = ('profession', 'text')
    search_fields = ('profession', 'text')
    list_per_page = 25


admin.site.register(Service, ServiceAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')
    list_per_page = 25


admin.site.register(About, AboutAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'carreer', 'percentage')
    list_display_links = ('id', 'carreer', 'percentage')
    list_filter = ('carreer', 'percentage')
    search_fields = ('carreer', 'percentage')
    list_per_page = 25


admin.site.register(Skill, SkillAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_pub', 'client', 'website','site_link')
    list_display_links = ('id', 'title', 'date_pub', 'client', 'website','site_link')
    list_filter = ('title', 'date_pub', 'client', 'website')
    search_fields = ('title', 'date_pub', 'client', 'website')
    list_per_page = 25


admin.site.register(Portfolio, PortfolioAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'date_create', 'is_approved')
    list_display_links = ('id', 'full_name', 'date_create', 'is_approved')
    list_filter = ('full_name', 'date_create', 'is_approved')
    search_fields = ('full_name', 'date_create', 'is_approved')
    list_per_page = 25


admin.site.register(Testimonial, TestimonialAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'contact_date')
    list_display_links = ('id', 'first_name', 'last_name',
                          'email', 'contact_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'state', 'country',)
    list_display_links = ('id', 'city', 'state', 'country',)
    list_filter = ('city', 'state', 'country',)
    search_fields = ('city', 'state', 'country',)
    list_per_page = 25


admin.site.register(Footer, FooterAdmin)
