from django.db import models
from django.conf import settings

class Equipment(models.Model):
    EQUIPMENT_TYPES = (
        ('robot', 'Industrial Robot'),
        ('machine', 'Manufacturing Machine'),
        ('qc', 'Quality Control System'),
    )

    type = models.CharField(max_length=100, choices=EQUIPMENT_TYPES)
    model = models.CharField(max_length=100)
    installation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='added_equipment')
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='responsible_equipment')

    def __str__(self):
        return f"{self.get_type_display()} - {self.model}"

class Data(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='data')
    timestamp = models.DateTimeField()
    temperature = models.FloatField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"Data for {self.equipment} at {self.timestamp}"

class Alerts(models.Model):
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='alerts')
    timestamp = models.DateTimeField()
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='low')
    detected_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='detected_alerts')
    resolved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='resolved_alerts', blank=True)

    def __str__(self):
        return f"Alert for {self.equipment} at {self.timestamp}"