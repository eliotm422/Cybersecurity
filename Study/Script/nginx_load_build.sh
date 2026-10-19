#!/bin/bash


# Principe : écrire des fichiers pour mettre en place une config vulénrable avec un port web exposé au 8080

echo -e "Configuration recherchée :\n\
docker-load-balancer\n\
├── docker-compose.yml\n\
├── nginx-lb/\n\
│   └── default.conf\n\
├── web1/\n\
│   ├── Dockerfile\n\
│   └── index.html\n\
├── web2/\n\
│   ├── Dockerfile\n\
│   └── index.html"

# Installation dépendances
sudo apt install docker.io
sudo apt install docker-compose


echo "Création de l'environnement du load balancer..."

# Créer l'arborescence
mkdir -p nginx-lb/web1 && mkdir -p nginx-lb/web2

# ---------- WEB1 ----------
cat <<EOF > nginx-lb/web1/index.html
<h1>Bonjour depuis Web1 !</h1>
EOF

cat <<EOF > nginx-lb/web1/Dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EOF

# ---------- WEB2 ----------
cat <<EOF > nginx-lb/web2/index.html
<h1>Bonjour depuis Web2 !</h1>
EOF

cat <<EOF > nginx-lb/web2/Dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EOF

# ---------- Load Balancer NGINX ----------
cat <<EOF > nginx-lb/default.conf
upstream backend {
    server web1:80;
    server web2:80;
}

server {
    listen 80;

    location / {
        proxy_pass http://backend;
    }
}
EOF

# ---------- Docker Compose ----------
cat <<EOF > nginx-lb/docker-compose.yml
version: '3'

services:
  web1:
    build: ./web1
    container_name: web1
    expose:
      - "80"

  web2:
    build: ./web2
    container_name: web2
    expose:
      - "80"

  nginx-lb:
    image: nginx:alpine
    container_name: load_balancer
    ports:
      - "8080:80"
    volumes:
      - ./nginx-lb/default.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - web1
      - web2
EOF

echo "✅ Tous les fichiers ont été créés avec succès."

# -------------------------
# Build et lancement
echo " construction et lancement de l'infrastructurearuction des conteneurs..."
sudo docker-compose build

echo "📦 Lancement de l'infrastructure..."
sudo docker-compose up -d

sudoecho " Accès au load balancer sur : http://localhost:8080"
wget http://localhost:8080