
# Install

```bash
# Installation
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common


# Install the latest version
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Install clé
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Ajout dépot
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Maj depot et install
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Check install
docker --version

# Activer et démarrer
sudo systemctl start docker
sudo systemctl enable docker

# Test
sudo docker run hello-world
```


````bash
# Docker 
sudo nano /etc/apt/sources.list.d/docker.list

# Docker
deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian bullseye stable

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io

sudo systemctl enable docker
sudo systemctl start docker

sudo docker run hello-world

````

# Utilisation


## Trouver et installer les images

```` bash
# Cherche
sudo docker search <nom_de_l_image>
sudo docker search ubuntu

# Install
sudo docker pull <nom_de_l_image>
sudo docker pull ubuntu

# Run
sudo docker run <nom_de_l_image>
# Run intéractif
sudo docker run -it <nom_de_l_image>
# Arrière plan 
sudo docker run -d <nom_de_l_image>

# Visualiser le conteneur
docker ps
docker ps -a

# Voir les images
docker images

# Arrêter un conteneur 
docker rm <id_du_conteneur>
````


````bash
sudo docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer-ce
````

```bash
# Build l'image
docker build -t my_image_name .

# Images
Docker images

# Lancer depuis une image
docker build --tag 'image_name'
```