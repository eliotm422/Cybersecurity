
# Installation


```bash
sudo apt-get install snort
```

# Règles

```bash
sudo vim /etc/snort/rules/local.rules

alert icmp any any -> $HOME_NET any (msg:"Tentative connexion ICMP"; sid:00001; rev:1;)
```


# Ecouter sur l'interface 


```bash
snort -A console -i eth0 -u snort -c /etc/snort/snort.conf
```