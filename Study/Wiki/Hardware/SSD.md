
# Histoire


### **1. Évolution des SSD**

- **Années 1990-2000** : Les premiers SSD utilisaient la mémoire volatile (RAM) avec une batterie pour maintenir les données en cas de coupure d'alimentation. Ces modèles étaient coûteux et destinés aux environnements industriels.
- **2008-2012** : Les SSD basés sur la mémoire NAND ont commencé à remplacer les disques durs (HDD) dans les ordinateurs grand public. Les premiers modèles étaient chers, avec des capacités limitées (~64-128 Go).
- **Depuis 2020** : Les SSD NVMe avec 3D NAND dominent le marché grâce à leur vitesse, fiabilité et capacité accrue.

# 2. Les technologies

## 2.1 Types de mémoire flash NAND

La mémoire NAND est l'élément principal des SSD. Elle stocke les données sous forme de charges électriques. Les types de NAND se différencient par le nombre de bits stockés dans chaque cellule :
4 systèmes, du moins dense et couteux au plus :
* Signle level Cell
* Multiple level Cell
* Triple level Cell
* Quadruple level Cell

## 2.2 Architectures de NAND

L'architecture influe sur la densité et la performance.

### 2.21 2D NAND (NAND planaire)

- Les cellules sont disposées sur une seule couche.
- **Avantages** : Simple et peu coûteux.
- **Inconvénients** : Moins dense, limite de capacité.

### 2.22 3D NAND (NAND empilée)

- Les cellules sont empilées verticalement en couches multiples.
- **Avantages** :
    - Plus dense (jusqu’à 176 couches en 2024).
    - Performances et durabilité améliorées.
    - Réduction des coûts par Go.
- **Inconvénients** : Coûts de fabrication plus élevés au départ.
## 2.3 Les technologies d'interfaces

L'interface détermine la manière dont le SSD communique avec l'ordinateur.

### 2.31 SATA (Serial ATA)

- **Débit maximum** : ~600 Mo/s (SATA III).
- **Avantages** :
    - Compatible avec de nombreux ordinateurs.
    - Coût réduit.
- **Inconvénients** :
    - Débit limité par rapport aux interfaces modernes.
- **Utilisation** : SSD d'entrée de gamme.

### 2.32 NVMe (Non-Volatile Memory Express)

- **Description** : Utilise une interface PCIe (généralement PCIe Gen 3, 4 ou 5).
- **Débit maximum** : Jusqu'à 7 000 Mo/s pour PCIe Gen 4 (et plus avec Gen 5).
- **Avantages** :
    - Débits très élevés.
    - Latence extrêmement faible.
- **Inconvénients** :
    - Coût plus élevé.
    - Nécessite une carte mère compatible.
- **Utilisation** : Jeux, stations de travail, usages exigeants.


### 3. Formats physiques des SSD

- **2,5 pouces** : Format classique pour les SSD SATA, compatible avec les baies de disques des PC portables et fixes.
- **M.2** : Petit format semblable à une barrette de RAM, utilisé pour les SSD SATA et NVMe. Deux types de clés existent :
    - **Clé B** : Pour SATA uniquement.
    - **Clé M** : Pour NVMe (PCIe).
    - **Clé B+M** : Compatible avec SATA et NVMe.
- **U.2** : Utilisé dans les serveurs, ce format combine des performances NVMe avec une meilleure dissipation thermique.
- **Add-in Card (AIC)** : SSD au format carte PCIe, utilisé dans les stations de travail et serveurs pour des performances maximales.