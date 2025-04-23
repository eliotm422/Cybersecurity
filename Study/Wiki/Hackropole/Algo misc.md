
# A l'envers

Pour commencer, téléchargez le fichier docker-compose.yml :
    curl https://hackropole.fr/challenges/fcsc2022-misc-a-l-envers/docker-compose.public.yml -o docker-compose.yml
    Lancez l'épreuve en exécutant dans le même dossier :
    docker compose up
    Dans un second terminal, accédez à l'épreuve via Netcat avec :
    nc localhost 4000


Les malins, c'est trop dur il faut faire un script :
Pour lire :
https://askubuntu.com/questions/873788/bash-read-lines-from-netcat-connection
Pour reverse :
https://stackoverflow.com/questions/11461625/reverse-the-order-of-characters-in-a-string

 vim reverse_nc.sh
```bash
#!/bin/bash

LOGFILE="./log.log"
if [ -f "$LOGFILE" ]; then
	rm $LOGFILE
fi

while read line
do
	echo $line >> $LOGFILE
	if [[ $line == ">>> "* ]]; then
		echo ${question:4} | rev | tee -a $LOGFILE

	fi
done 
echo "Good bye"
```

```sh
nc localhost 4000 < ./backpipe | bash ./reverse_nc.sh > ./backpipe
```

```bash
cat log.log | tail -n 1
```

chmod +x reverse_nc.sh