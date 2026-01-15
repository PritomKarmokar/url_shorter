from django.contrib import admin

from shortener.models import UrlShortener

@admin.register(UrlShortener)
class UrlShortenerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "url",
    )
    readonly_fields = ("id",)
    fieldsets = [
        (
            None,
            {
                "fields": ["url", "hashed_token"],
            },
        ),
        (
            "Date Information",
            {
                "classes": ["collapse"],
                "fields": ["created_at"],
            }
        )
    ]
    ordering = ("-created_at",)