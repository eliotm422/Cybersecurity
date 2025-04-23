
# Lire les infos

````bash
# Lire les infos
file <nom>
# Lire + d'infos
minfo -i <nom>
# Hexdump
hexdump <nom>
````

# Analyse du disque

## Analyser les fichiers/dossiers supprimés

````bash
# analyse poussée du fichier 
foremost <nom>
└─$ cat output/audit.txt  
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Mon Oct 28 11:38:26 2024
Invocation: foremost usb.image 
Output directory: /media/sf_Virtual_box_partage/output
Configuration file: /etc/foremost.conf
------------------------------------------------------------------
File: usb.image
Start: Mon Oct 28 11:38:26 2024
Length: 31 MB (32505856 bytes)
 
Num      Name (bs=512)         Size      File Offset     Comment 

0:      00000168.png         240 KB           86016       (400 x 300)
Finish: Mon Oct 28 11:38:27 2024

1 FILES EXTRACTED

png:= 1
------------------------------------------------------------------

Foremost finished at Mon Oct 28 11:38:27 2024     
````

## FLS : dossiers supprimés

The **fls t**ool from Sleuth Kith Toolkit lists all files and directories in a file system and can also display file names of **recently deleted files.** In the below output the deleted file is marked with an * .

````bash
fls <nom>
# Données
└─$ fls usb.image 
r/r 3:  USB         (Volume Label Entry)
r/r * 5:        anonyme.png
v/v 1013699:    $MBR
v/v 1013700:    $FAT1
v/v 1013701:    $FAT2
V/V 1013702:    $OrphanFiles

# Infos
└─$ fdisk -lu  usb.image   
Disk usb.image: 31 MiB, 32505856 bytes, 63488 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x00000000
````



## fsstat : structures d'allocation, bloque de démarrage...

The **fsstat** command can be used to learn the the general known information, such as layout, allocation structures and boot blocks. This information is retrieved - as seen from above hexdump - from the boot sector/superblock of a file system. The following output shows the total range of the file system, metadata & content information and more.

````bash
└─$ fsstat usb.image 
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: FAT16

OEM Name: mkfs.fat
Volume ID: 0xc7ecde5b
Volume Label (Boot Sector): USB        
Volume Label (Root Directory): USB        
File System Type Label: FAT16   

Sectors before file system: 2048

File System Layout (in sectors)
Total Range: 0 - 63487
* Reserved: 0 - 3
** Boot Sector: 0
* FAT 0: 4 - 67
* FAT 1: 68 - 131
* Data Area: 132 - 63487
** Root Directory: 132 - 163
** Cluster Area: 164 - 63487

METADATA INFORMATION
--------------------------------------------
Range: 2 - 1013702
Root Directory: 2

CONTENT INFORMATION
--------------------------------------------
Sector Size: 512
Cluster Size: 2048
Total Cluster Range: 2 - 15832

FAT CONTENTS (in sectors)
--------------------------------------------
````

## Autopsy 4.14.0 : le plus complet

Autopsy provides various functionality for the analysis part, such as file listing & file content and meta data analysis, keyword search and much more. Among other it is possible to get an overview of the deleted files and to reconstruct the file, respectively to export it.

````bash
# Installation et aide
sudo apt install autopsy
└─$ autopsy -h 
Invalid flag: -h

usage: /usr/bin/autopsy [-c] [-C] [-d evid_locker] [-i device filesystem mnt] [-p port] [remoteaddr]
  -c: force a cookie in the URL
  -C: force NO cookie in the URL
  -d dir: specify the evidence locker directory
  -i device filesystem mnt: Specify info for live analysis
  -p port: specify the server port (default: 9999)
  remoteaddr: specify the host with the browser (default: localhost)

# Regarder 
http://localhost:9999/autopsy
````

# Hexedit : lire de l'hexa décimal

En faisant un hexdump, on lit notre hexadécimal de la clef usb.

On va utiliser l'outil Hexedit pour voir le fonctionnement :
````bash
└─$ hexedit -h       
usage: hexedit [-s | --sector] [-m | --maximize] [-l<n> | --linelength <n>] [--color] [-h | --help] filename

# Affichage basique
hexedit <nom> 

# Affichage prénom
hexedit <nom> | grep "ownership"
````


# Lire les .image non


````bash
sudo apt install exiv2
````

# Exifprobe

````bash
exifprobe
````
	