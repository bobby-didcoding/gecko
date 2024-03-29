from django.contrib import admin
from .models import Pool, Network, Token, Dex, TokenPair


@admin.register(Pool)
class PoolAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
    )
    search_fields = ("external_id",)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
    )
    search_fields = ("external_id",)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
    )
    search_fields = ("external_id",)


@admin.register(TokenPair)
class TokenPairAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
    )
    search_fields = ("external_id",)


@admin.register(Dex)
class DexAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
    )
    search_fields = ("external_id",)
