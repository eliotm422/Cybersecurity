#!/bin/bash

# Principe : écrire dans des fichiers configuration des scripts pour une kali :
# powerlevel10k
# vim

# 
#    Install the recommended font. Optional but highly recommended.
#    Install Powerlevel10k itself.
#    Restart Zsh with exec zsh.
#    Type p10k configure if the configuration wizard doesn't start automatically.

# Clavier en Fr
setxkbmap fr

# Installation de Oh My Zsh
echo " Installation de Oh My Zsh..."
export RUNZSH=no
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Installation ZSH
echo "### INSTALLATION ZSH et powerlevel10k ###"

git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
vim ~/.zshrc 
echo "Modification fichier de conf #/.zhrc."
sed -i 's/^ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc
echo "Passage à ZSH comme shell par défaut..."
chsh -s $(which zsh)
exec zsh

p10k configure

echo "### FIN CONFIG ZSH###" 

# Configuration VIM
mkdir -p ~/.vim ~/.vim/autoload ~/.vim/backup ~/.vim/colors ~/.vim/plugged


# Installation VIM
echo "### INSTALLATION VIM ###"

echo "### INSTALLATION VIMRC ###"
sudo apt-get install vim
# Couleur thème 
echo 'colorscheme ron' >> ~/.vimrc
# Syntaxe
echo 'syntax enable' >> ~/.vimrc

# Evite les erreurs avec vi 
echo 'set nocompatible' >> ~/.vimrc
echo 'filetype on' >> ~/.vimrc

# Curseur syntax
echo 'syntax on' >> ~/.vimrc

# afficahge ligne
echo 'set number' >> ~/.vimrc

# Highlight cursor line underneath the cursor horizontally.
echo 'set cursorline' >> ~/.vimrc

# Highlight cursor line underneath the cursor vertically.
echo 'set cursorcolumn' >> ~/.vimrc

# Use space characters instead of tabs.
echo 'set expandtab' >> ~/.vimrc

# " Ignore capital letters during search.
echo 'set ignorecase' >> ~/.vimrc 
