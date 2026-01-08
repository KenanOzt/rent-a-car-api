# 1. Zemin olarak resmi Python sürümünü kullan (İnce sürüm)
FROM python:3.10-slim

# 2. Çalışma klasörünü ayarla
WORKDIR /app

# 3. Önce gereksinim dosyasını kopyala (Cache avantajı için)
COPY requirements.txt .

# 4. Kütüphaneleri kur
RUN pip install --no-cache-dir -r requirements.txt

# 5. Projenin geri kalanını kopyala
COPY . .

# 6. Uygulamayı çalıştır (0.0.0.0 dışarıdan erişim için şart)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]