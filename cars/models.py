from django.db import models

class Car(models.Model):
    # Marka (örn: BMW) - max 50 karakter
    brand = models.CharField(max_length=50) 
    
    # Model (örn: i5) - max 50 karakter
    model = models.CharField(max_length=50) 
    
    # Yıl (örn: 2023)
    year = models.IntegerField() 
    
    # Günlük Ücret (örn: 1500.50)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    # Müsait mi? (Varsayılan: Evet)
    is_available = models.BooleanField(default=True) 
    
    # Kayıt tarihi (Otomatik eklenir)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"