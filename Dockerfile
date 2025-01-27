# Utilisation d'une image de base Python
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source dans le conteneur
COPY . /app/

# Définir la variable d'environnement pour le port
ENV PORT=8000

# Exposer le port sur lequel l'application Flask va tourner
EXPOSE 8000

# Lancer l'application Flask
CMD ["python", "app.py"]

