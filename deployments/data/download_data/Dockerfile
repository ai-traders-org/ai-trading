# Użyj obrazu z Pythonem jako podstawy
FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj całą zawartość projektu do obrazu
COPY . .

# Zainstaluj wymagania aplikacji
RUN pip install --no-cache-dir -r requirements.txt

# Ustaw domyślny punkt wejścia do uruchomienia aplikacji
CMD ["python", "main.py"]
