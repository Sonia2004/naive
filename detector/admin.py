from django.contrib import admin
from .models import EmailCheckRecord


@admin.register(EmailCheckRecord)
class EmailCheckRecordAdmin(admin.ModelAdmin):
    """Administrador personalizado para EmailCheckRecord."""
    
    list_display = ('subject', 'prediction', 'confidence', 'created_at')
    list_filter = ('prediction', 'created_at')
    search_fields = ('subject', 'email_content')
    readonly_fields = ('email_content', 'created_at')
    
    fieldsets = (
        ('Información del Email', {
            'fields': ('subject', 'email_content')
        }),
        ('Predicción', {
            'fields': ('prediction', 'confidence')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )
    
    def has_add_permission(self, request):
        """Impide agregar registros manualmente desde admin."""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Solo superusuarios pueden eliminar."""
        return request.user.is_superuser
