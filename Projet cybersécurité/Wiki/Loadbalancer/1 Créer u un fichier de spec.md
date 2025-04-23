
## Install dépendances

```bash
sudo apt install docker.io
sudo apt install docker-compose
```

## Structure shell

 ```linuyx
 load-balancer-project/
├── docker-compose.yml
├── nginx-lb/
│   ├── default.conf
├── web1/
│   ├── Dockerfile
│   └── index.html
├── web2/
│   ├── Dockerfile
│   └── index.html
```

## Créer des dossiers


Crée un dossier pour ton projet :

```bash
mkdir docker-load-balancer && cd docker-load-balancer
mkdir web1 && mkdir web2
```



Voici un exemple de fichier **`docker-compose.yml`** qui simule le comportement par défaut d’un **load balancer** (équilibreur de charge) en utilisant **NGINX** comme reverse proxy, avec plusieurs instances d’une application web en backend :

```yaml
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
      - web20"

```

Et voici un fichier **`nginx-lb/default.conf`** associé, à placer dans le même répertoire que le `docker-compose.yml`, qui fait du round-robin (par défaut) entre les deux backends :

```nginx
events {}

http {
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
}

```

**web1/Dockerfile**

```bash
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
```
# Build avec ansible

```yaml
- name: Déploiement Load Balancer NGINX
  hosts: loadbalancer
  become: yes

  tasks:
    - name: Installer NGINX
      apt:
        name: nginx
        state: present

    - name: Copier le fichier de conf
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf

    - name: Recharger NGINX
      service:
        name: nginx
        state: reloaded
```

Fichier nginx :

```nginx
http {
    upstream backend {
        {% for host in groups['backends'] %}
        server {{ host }}:80;
        {% endfor %}
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend;
        }
    }
}
```