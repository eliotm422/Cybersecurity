.Sup
[[Sup de Vinci/cours/OSINT]]

# Installation et utilisation
```bash
sudo apt-get install exiftool

exiftool /media/sf_Virtual_box_partage/photo.png
```
* Commande de base 
```
exiftool .jpg
```

* La localisation 
```bash
exiftool -geotag=/media/sf_Virtual_box_partage/photo.png 

```

* Le type et la sortie 
````Bash 
$ exiftool   -args UTF-16 /media/sf_Virtual_box_partage/photo.png 
$ exiftool   -b UTF-16 /media/sf_Virtual_box_partage/photo.png 

```