from django.db import models


class EmailCheckRecord(models.Model):
    """Modelo para guardar el historial de emails analizados."""
    STATUS_CHOICES = [
        ('spam', 'SPAM'),
        ('ham', 'No es SPAM'),
    ]
    
    email_content = models.TextField()
    subject = models.CharField(max_length=255, blank=True)
    prediction = models.CharField(max_length=10, choices=STATUS_CHOICES)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Email Check Records"
    
    def __str__(self):
        return f"{self.subject} - {self.prediction} ({self.confidence:.2%})"
