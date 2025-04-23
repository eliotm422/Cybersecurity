.defense
[[Useful Windows Event logs]] [[Working with IDS IPS]]

**

# Introduction


  

Bienvenue dans le module de déobfuscation JavaScript !

La déobfuscation de code est une compétence importante à acquérir si nous voulons exceller dans l'analyse de code et l'ingénierie inverse. Lors des exercices d'équipe rouge/bleue, nous rencontrons souvent du code obfusqué qui cherche à cacher certaines fonctionnalités, comme des logiciels malveillants qui utilisent du code JavaScript obfusqué pour récupérer leur charge utile principale. Sans comprendre ce que fait ce code, nous pourrions ne pas savoir exactement ce que fait le code et donc ne pas être en mesure de mener à bien l'exercice en équipe rouge/bleue.

Dans ce module, nous commencerons par apprendre la structure générale d'une page HTML, puis nous localiserons le code JavaScript à l'intérieur. Une fois cela fait, nous apprendrons ce qu'est l'obfuscation, comment elle est réalisée et où elle est utilisée, puis nous apprendrons à déobfusquer un tel code. Une fois le code déobfusqué, nous tenterons de comprendre son utilisation générale pour reproduire sa fonctionnalité et découvrir manuellement ce qu'il fait.

Les sujets suivants seront abordés :

- Localisation du code JavaScript
    
- Introduction à l'obfuscation de code
    
- Comment déobfusquer du code JavaScript
    
- Comment décoder des messages encodés
    
- Analyse de base du code
    
- Envoi de requêtes HTTP de base
    

Résumé : Ce module traite de la déobfuscation de code JavaScript, une compétence essentielle pour l'analyse de code et l'ingénierie inverse. On apprendra à localiser le code JavaScript dans une page HTML, à comprendre ce qu'est l'obfuscation et comment la réaliser, et à déobfusquer le code pour en comprendre la fonctionnalité cachée. On découvrira également comment décoder des messages encodés et réaliser une analyse de base du code, ainsi que l'envoi de requêtes HTTP simples. Ces compétences sont utiles pour les exercices d'équipe rouge/bleue et pour comprendre le comportement des logiciels malveillants cachés derrière un code JavaScript obfusqué.

---

## What is obfuscation

L'Obfuscation de Code

Avant d'apprendre la déobfuscation, nous devons d'abord comprendre l'obfuscation de code. Sans comprendre comment le code est obfusqué, nous pourrions ne pas réussir à déobfusquer le code, surtout s'il a été obfusqué à l'aide d'un outil d'obfuscation personnalisé.

Qu'est-ce que l'obfuscation ? L'obfuscation est une technique utilisée pour rendre un script plus difficile à lire par les humains, tout en lui permettant de fonctionner de la même manière d'un point de vue technique, bien que les performances puissent être plus lentes. Cela est généralement réalisé automatiquement à l'aide d'un outil d'obfuscation, qui prend le code en entrée et tente de le réécrire d'une manière beaucoup plus difficile à lire, selon sa conception.

![](https://lh7-us.googleusercontent.com/Npt2YR442x9W5g_b8bNdqMsoKsOT76F2-qz4Zj8h99b3gihsPk-xPCgdfaHyaIJ7pWPm7d3XxqKK013iuPKJDD0qNQT3cq4XV6Cx5H9X7spcHN_z8qNYmT1-LaF4enlCEHgT_jAkBzCZGSYgqkEMIVQ)Par exemple, les obfuscateurs de code transforment souvent le code en un dictionnaire de tous les mots et symboles utilisés dans le code, puis essaient de reconstruire le code d'origine pendant l'exécution en se référant à chaque mot et symbole du dictionnaire. Voici un exemple de code JavaScript simple étant obfusqué.

Utilisations Il existe de nombreuses raisons pour lesquelles les développeurs peuvent envisager d'obfusquer leur code. Une raison courante est de cacher le code d'origine et ses fonctions pour éviter qu'il soit réutilisé ou copié sans la permission du développeur, rendant ainsi la fonctionnalité d'origine du code plus difficile à inverser. Une autre raison est de fournir une couche de sécurité lors de l'authentification ou du chiffrement pour prévenir les attaques sur les vulnérabilités pouvant être trouvées dans le code.

Il convient de noter que l'authentification ou le chiffrement côté client n'est pas recommandé, car le code est plus vulnérable aux attaques de cette manière.

Cependant, l'utilisation la plus courante de l'obfuscation est à des fins malveillantes. Il est courant que les attaquants et les acteurs malveillants obfusquent leurs scripts malveillants pour empêcher les systèmes de détection et de prévention des intrusions de détecter leurs scripts. Dans la section suivante, nous apprendrons comment obfusquer un code JavaScript simple et tenterons de l'exécuter avant et après l'obfuscation pour noter toute différence.

Résumé : L'obfuscation de code est une technique qui rend le code plus difficile à lire pour les humains, tout en maintenant sa fonctionnalité technique. Cela peut être utilisé pour protéger la propriété intellectuelle, ajouter une couche de sécurité à l'authentification et au chiffrement, ou dissimuler des scripts malveillants pour éviter la détection. Cependant, l'utilisation malveillante de l'obfuscation est courante pour échapper aux systèmes de détection des intrusions. Il est important de comprendre l'obfuscation pour pouvoir déobfusquer un code et en comprendre les intentions cachées.

#   

# Basic Obfuscation

---

Code obfuscation is usually not done manually, as there are many tools for various languages that do automated code obfuscation. Many online tools can be found to do so, though many malicious actors and professional developers develop their own obfuscation tools to make it more difficult to deobfuscate.

---

## Running JavaScript code

Let us take the following line of code as an example and attempt to obfuscate it:

Code: javascript

console.log('HTB JavaScript Deobfuscation Module');

  

First, let us test running this code in cleartext, to see it work in action. We can go to [JSConsole](https://jsconsole.com/), paste the code and hit enter, and see its output:

![](https://lh7-us.googleusercontent.com/VUIXcS2u_VZd07Y11nTyaarXVA9o5jpQAcQG6P3YHoVIY-Sa5clq854dYkrfnWyXBeEG1Zgkk07whouaLk49e8h5z75kLIAvURx5mZ7wDNEz2bHM1KvUFwPQqHI3vyzKY-nyIKtbHCQ9yAaDaKOBM3U)

We see that this line of code prints HTB JavaScript Deobfuscation Module, which is done using the console.log() function.

---

## Minifying JavaScript code

A common way of reducing the readability of a snippet of JavaScript code while keeping it fully functional is JavaScript minification. Code minification means having the entire code in a single (often very long) line. Code minification is more useful for longer code, as if our code only consisted of a single line, it would not look much different when minified.

Many tools can help us minify JavaScript code, like [javascript-minifier](https://javascript-minifier.com/). We simply copy our code, and click Minify, and we get the minified output on the right:

![](https://lh7-us.googleusercontent.com/Dsc_oQuYM92_o2HROLCyzU3dJKL_SdXkpdaZ3dtiUlb6o94cGYEdV7WT-MmH6zEqyx_wwPgkjtLbcI1BuMjIFdgUfNuxVTkbETmMiLj2pNncKkhw4ajDD4yvHNkf5C8haF8waYM1N5FeRnBVEjtCTs0)

Once again, we can copy the minified code to [JSConsole](https://jsconsole.com/), and run it, and we see that it runs as expected. Usually, minified JavaScript code is saved with the extension .min.js.

Note: Code minification is not exclusive to JavaScript, and can be applied to many other languages, as can be seen on [javascript-minifier](https://javascript-minifier.com/).

---

## Packing JavaScript code

Now, let us obfuscate our line of code to make it more obscure and difficult to read. First, we will try [BeautifyTools](http://beautifytools.com/javascript-obfuscator.php) to obfuscate our code:

![](https://lh7-us.googleusercontent.com/s5X_hURY_1Pju5bXj3vBVrUACPMTw5TCoqgXpfRXFNpBmTleNiycERf_e5vg10PWtx5sefQEv2sqZuL5XSa6MLMrF487SpWa7ucEBd0iyO2YWvXZRL4Cbcz2soXq8IL-uhPpTTmmktTsnEyN7JC2aPM)

Code: javascript

eval(function(p,a,c,k,e,d){e=function(c){return c};if(!''.replace(/^/,String)){while(c--){d[c]=k[c]||c}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('5.4(\'3 2 1 0\');',6,6,'Module|Deobfuscation|JavaScript|HTB|log|console'.split('|'),0,{}))

  

We see that our code became much more obfuscated and difficult to read. We can copy this code into [https://jsconsole.com](https://jsconsole.com/), to verify that it still does its main function:

![](https://lh7-us.googleusercontent.com/o0rZUvbfr37Ko38pqnFp7DOPkzGfYxiuzwpUQ6HAtpIVaXgDCVag__mLYT_uzHzdjX_m6-WuW2pcGkRIGnBDlhLw5AKIWWjDvXQddbEnscsIsjZZpKw6rT0Dyv_5ARsAX4ok7ddwhTgI3mObcAYLPAc)

Nous constatons que nous obtenons la même sortie. Note : Le type d'obfuscation ci-dessus est connu sous le nom de "packing", ce qui est généralement reconnaissable grâce aux six arguments de fonction utilisés dans la fonction initiale "function(p,a,c,k,e,d)". Un outil d'obfuscation de type "packer" tente généralement de convertir tous les mots et symboles du code en une liste ou un dictionnaire, puis les référence à l'aide de la fonction (p,a,c,k,e,d) pour reconstruire le code d'origine lors de l'exécution. Le contenu de (p,a,c,k,e,d) peut varier d'un "packer" à un autre, mais il contient généralement un certain ordre dans lequel les mots et symboles du code d'origine ont été regroupés pour savoir comment les ordonner lors de l'exécution. Bien qu'un "packer" fasse un excellent travail pour réduire la lisibilité du code, nous pouvons toujours voir ses principales chaînes de caractères écrites en clair, ce qui peut révéler une partie de sa fonctionnalité. C'est pourquoi nous pourrions rechercher de meilleures façons d'obfusquer notre code.

Résumé : Nous avons remarqué que nous obtenons la même sortie après avoir utilisé un outil d'obfuscation de type "packer". Ce type d'obfuscation consiste à convertir les mots et symboles du code en une liste ou un dictionnaire, puis à les référencer pour reconstruire le code d'origine lors de l'exécution. Malgré cela, certaines parties du code restent lisibles en clair, ce qui peut révéler des informations sur sa fonctionnalité. Pour une meilleure sécurité, il est important de rechercher des méthodes plus avancées d'obfuscation de code.

  

# Advanced Obfuscation

---

So far, we have been able to make our code obfuscated and more difficult to read. However, the code still contains strings in cleartext, which may reveal its original functionality. In this section, we will try a couple of tools that should completely obfuscate the code and hide any remanence of its original functionality.

---

## Obfuscator

Let's visit [https://obfuscator.io](https://obfuscator.io/). Before we click obfuscate, we will change String Array Encoding to Base64, as seen below:

![](https://lh7-us.googleusercontent.com/W9J1g0e_zEO4FSK-sk0P7hLuvlJcRd8vl2uW8swXtza-JP-S6EX95VPqRMK--TraDRIL2CoeRvHKPKRhVIpLT3kVQuwrtYMNfHZtn0WSfRksCrXn_jZ2NbowfNljv-f2VGJXq2mIBygDC6r49Qmv7VI)

Now, we can paste our code and click obfuscate:

![](https://lh7-us.googleusercontent.com/3iLiyF6P9vTJeL_bh-NE5jsNPhGzbQ2WSxpWAxLteT5Wi4ziLbQVqI9Thaz8qfXeetU-l8Jq_EcR9Hg6-0JAZBfVr2pHbOyIH-V97YqVbh4_dvmmF9ymoNRdXpJzrvUQGn9dFm9fIEh7ParEJ8PvIyE)

We get the following code:

Code: javascript
***
```` bash
var _0x1ec6=['Bg9N','sfrciePHDMfty3jPChqGrgvVyMz1C2nHDgLVBIbnB2r1Bgu='];(function(_0x13249d,_0x1ec6e5){var _0x14f83b=function(_0x3f720f){while(--_0x3f720f){_0x13249d['push'](_0x13249d['shift']());}};_0x14f83b(++_0x1ec6e5);}(_0x1ec6,0xb4));var _0x14f8=function(_0x13249d,_0x1ec6e5){_0x13249d=_0x13249d-0x0;var _0x14f83b=_0x1ec6[_0x13249d];if(_0x14f8['eOTqeL']===undefined){var _0x3f720f=function(_0x32fbfd){var _0x523045='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=',_0x4f8a49=String(_0x32fbfd)['replace'](/=+$/,'');var _0x1171d4='';for(var _0x44920a=0x0,_0x2a30c5,_0x443b2f,_0xcdf142=0x0;_0x443b2f=_0x4f8a49['charAt'](_0xcdf142++);~_0x443b2f&&(_0x2a30c5=_0x44920a%0x4?_0x2a30c5*0x40+_0x443b2f:_0x443b2f,_0x44920a++%0x4)?_0x1171d4+=String['fromCharCode'](0xff&_0x2a30c5>>(-0x2*_0x44920a&0x6)):0x0){_0x443b2f=_0x523045['indexOf'](_0x443b2f);}return _0x1171d4;};_0x14f8['oZlYBE']=function(_0x8f2071){var _0x49af5e=_0x3f720f(_0x8f2071);var _0x52e65f=[];for(var _0x1ed1cf=0x0,_0x79942e=_0x49af5e['length'];_0x1ed1cf<_0x79942e;_0x1ed1cf++){_0x52e65f+='%'+('00'+_0x49af5e['charCodeAt'](_0x1ed1cf)['toString'](0x10))['slice'](-0x2);}return decodeURIComponent(_0x52e65f);},_0x14f8['qHtbNC']={},_0x14f8['eOTqeL']=!![];}var _0x20247c=_0x14f8['qHtbNC'][_0x13249d];return _0x20247c===undefined?(_0x14f83b=_0x14f8['oZlYBE'](_0x14f83b),_0x14f8['qHtbNC'][_0x13249d]=_0x14f83b):_0x14f83b=_0x20247c,_0x14f83b;};console[_0x14f8('0x0')](_0x14f8('0x1'));
***
```` 

This code is obviously more obfuscated, and we can't see any remnants of our original code. We can now try running it in [https://jsconsole.com](https://jsconsole.com/) to verify that it still performs its original function. Try playing with the obfuscation settings in [https://obfuscator.io](https://obfuscator.io/) to generate even more obfuscated code, and then try rerunning it in [https://jsconsole.com](https://jsconsole.com/) to verify it still performs its original function.

---

## More Obfuscation

Now we should have a clear idea of how code obfuscation works. There are still many variations of code obfuscation tools, each of which obfuscates the code differently. Take the following JavaScript code, for example:
***
Code: javascript
````
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(!

...SNIP...

[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+[+[]])))()

***
````
We can still run this code, and it would still perform its original function:

![](https://lh7-us.googleusercontent.com/_9T1kKAvi_FkCIA4grz-brpw8yVqF4l7eEjYoCv_y3xI_sfOX8fDNFb3SVt9kN1ksyRxDBttZ7V-ajVSr91iX7RmS5kdHOX6ag8k0Bbc2Y3t18qHRRX5hWQovuuj1gzwRPkntq4VLfC8JLUEojulp6c)

Note: The above code was snipped as the full code is too long, but the full code should successfully run.

We can try obfuscating code using the same tool in [JSF](http://www.jsfuck.com/), and then rerunning it. We will notice that the code may take some time to run, which shows how code obfuscation could affect the performance, as previously mentioned.

There are many other JavaScript obfuscators, like [JJ Encode](https://utf-8.jp/public/jjencode.html) or [AA Encode](https://utf-8.jp/public/aaencode.html). However, such obfuscators usually make code execution/compilation very slow, so it is not recommended to be used unless for an obvious reason, like bypassing web filters or restrictions.

  

# Deobfuscation

---

Now that we understand how code obfuscation works let's start our learning towards deobfuscation. Just as there are tools to obfuscate code automatically, there are tools to beautify and deobfuscate the code automatically.

---

## Beautify

We see that the current code we have is all written in a single line. This is known as Minified JavaScript code. In order to properly format the code, we need to Beautify our code. The most basic method for doing so is through our Browser Dev Tools.

For example, if we were using Firefox, we can open the browser debugger with [ CTRL+SHIFT+Z ], and then click on our script secret.js. This will show the script in its original formatting, but we can click on the '{ }' button at the bottom, which will Pretty Print the script into its proper JavaScript formatting: ![](https://lh7-us.googleusercontent.com/WvaqC2YQKTISg0DWvQNTH0OJrndc_SjHNaRmWARnU5k5w3iN941N3XbceJUiDJnn6BGCsxBlLoG3zIFcr0M_WBe3zbuQQ6FJV9xzOFLZemCda3KTZCauxnKJ58EXvKgrGoiQbOLry7cLIYzP6YlxAKo)

Furthermore, we can utilize many online tools or code editor plugins, like [Prettier](https://prettier.io/playground/) or [Beautifier](https://beautifier.io/). Let us copy the secret.js script:
````
Code: javascript
***
eval(function (p, a, c, k, e, d) { e = function (c) { return c.toString(36) }; if (!''.replace(/^/, String)) { while (c--) { d[c.toString(a)] = k[c] || c.toString(a) } k = [function (e) { return d[e] }]; e = function () { return '\\w+' }; c = 1 }; while (c--) { if (k[c]) { p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]) } } return p }('g 4(){0 5="6{7!}";0 1=8 a();0 2="/9.c";1.d("e",2,f);1.b(3)}', 17, 17, 'var|xhr|url|null|generateSerial|flag|HTB|flag|new|serial|XMLHttpRequest|send|php|open|POST|true|function'.split('|'), 0, {}))

***

We can see that both websites do a good job in formatting the code:

![](https://lh7-us.googleusercontent.com/gzbRjOtKI9FdDrrcmqXeyPUglZJF5mulfQWy6jmWAVJ2euZ6STidYDtGOTSXIM0pdWbAvTPHYP1r2c4gwIhMDYyDrcH7285c_LAmL7FXiQoshKBB628t_I_pnnCv_cKdx4iauIkGt50HrCCIlyTOISI)

![](https://lh7-us.googleusercontent.com/psv6JIP11osTuNHJDjlmb7sh3DrZNFTr3mifdRuq6cjFlgBX8X9bddcMS011st3FD98TkBZWo52VecNXKxkRg_dEVCceWPFLUzIE5s-1CzJRfkwQWi8okG6AHdozeLMwN39RpDddYjkys8OP_LTTiiY)
````

However, the code is still not very easy to read. This is because the code we are dealing with was not only minified but obfuscated as well. So, simply formatting or beautifying the code will not be enough. For that, we will require tools to deobfuscate the code.

---

## Deobfuscate

We can find many good online tools to deobfuscate JavaScript code and turn it into something we can understand. One good tool is [JSNice](http://www.jsnice.org/). Let's try copying our above-obfuscated code and run it in JSNice by clicking the Nicify JavaScript button.

Tip: We should click on the options button next to the "Nicify JavaScript" button, and de-select "Infer types" to reduce cluttering the code with comments.

Tip: Ensure you do not leave any empty lines before the script, as it may affect the deobfuscation process and give inaccurate results.

![](https://lh7-us.googleusercontent.com/u0MV2xMXxy7K3Pdqcq_Sv1_X4l_Msjrp1l0tf9p4L_Xcqn33lxOlEfJTIWvvL4K4nFdAGmkMaO0CIv5G5tkSrppvkRWIfTYaV--YUtvi0TKZKv4Ka_Eth1CnNB1da_hBzkY1SO6wLnisi7uwRzwiJqI)

We can see that this tool does a much better job in deobfuscating the JavaScript code and gave us an output we can understand:
````

Code: javascript

'use strict';

function generateSerial() {

  ...SNIP...

  var xhr = new XMLHttpRequest;

  var url = "/serial.php";

  xhr.open("POST", url, true);

  xhr.send(null);

};

````
 

As previously mentioned, the above-used method of obfuscation is packing. Another way of unpacking such code is to find the return value at the end and use console.log to print it instead of executing it.

---

## Reverse Engineering

Though these tools are doing a good job so far in clearing up the code into something we can understand, once the code becomes more obfuscated and encoded, it would become much more difficult for automated tools to clean it up. This is especially true if the code was obfuscated using a custom obfuscation tool.

We would need to manually reverse engineer the code to understand how it was obfuscated and its functionality for such cases. If you are interested in knowing more about advanced JavaScript Deobfuscation and Reverse Engineering, you can check out the [Secure Coding 101](https://academy.hackthebox.com/module/details/38) module, which should thoroughly cover this topic.

  

Using what you learned in this section, try to deobfuscate 'secret.js' in order to get the content of the flag. What is the flag?

[http://adresseip:port](about:blank)

ctrl shit z // inspecter debuger

on colle le code ici 
````

***
eval(function (p, a, c, k, e, d) { e = function (c) { return c.toString(36) }; if (!''.replace(/^/, String)) { while (c--) { d[c.toString(a)] = k[c] || c.toString(a) } k = [function (e) { return d[e] }]; e = function () { return '\\w+' }; c = 1 }; while (c--) { if (k[c]) { p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]) } } return p }('g 4(){0 5="6{7!}";0 1=8 a();0 2="/9.c";1.d("e",2,f);1.b(3)}', 17, 17, 'var|xhr|url|null|generateSerial|flag|HTB|1_4m_7h3_53r14l_g3n3r470r|new|serial|XMLHttpRequest|send|php|open|POST|true|function'.split('|'), 0, {}))

[https://beautifier.io/](https://beautifier.io/)

eval(function(p, a, c, k, e, d) {

    e = function(c) {

        return c.toString(36)

    };

    if (!''.replace(/^/, String)) {

        while (c--) {

            d[c.toString(a)] = k[c] || c.toString(a)

        }

        k = [function(e) {

            return d[e]

        }];

        e = function() {

            return '\\w+'

        };

        c = 1

    };

    while (c--) {

        if (k[c]) {

            p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c])

        }

    }

    return p

}('g 4(){0 5="6{7!}";0 1=8 a();0 2="/9.c";1.d("e",2,f);1.b(3)}', 17, 17, 'var|xhr|url|null|generateSerial|flag|HTB|1_4m_7h3_53r14l_g3n3r470r|new|serial|XMLHttpRequest|send|php|open|POST|true|function'.split('|'), 0, {}))
***
on colle le joli code ici 

[http://www.jsnice.org/](http://www.jsnice.org/)
***
'use strict';

/**

 * @return {undefined}

 */

function generateSerial() {

  /** @type {string} */

  var flag = "HTB{1_4m_7h3_53r14l_g3n3r470r!}";

  /** @type {!XMLHttpRequest} */

  var xhr = new XMLHttpRequest;

  /** @type {string} */

  var url = "/serial.php";

  xhr.open("POST", url, true);

  xhr.send(null);

}

;
````

*** 
tadam

# Code Analysis

---

Now that we have deobfuscated the code, we can start going through it:

Code: javascript
***
'use strict';

function generateSerial() {

  ...SNIP...

  var xhr = new XMLHttpRequest;

  var url = "/serial.php";

  xhr.open("POST", url, true);

  xhr.send(null);

};

***

We see that the secret.js file contains only one function, generateSerial.

---

## HTTP Requests

Let us look at each line of the generateSerial function.
***
Code: javascript

'use strict';

function generateSerial() {

  ...SNIP...

  var xhr = new XMLHttpRequest;

  var url = "/serial.php";

  xhr.open("POST", url, true);

  xhr.send(null);

};

***

#### Code Variables

The function starts by defining a variable xhr, which creates an object of XMLHttpRequest. As we may not know exactly what XMLHttpRequest does in JavaScript, let us Google XMLHttpRequest to see what it is used for.  
After we read about it, we see that it is a JavaScript function that handles web requests.

  

# HTTP Requests

---

In the previous section, we found out that the secret.js main function is sending an empty POST request to /serial.php. In this section, we will attempt to do the same using cURL to send a POST request to /serial.php. To learn more about cURL and web requests, you can check out the [Web Requests](https://academy.hackthebox.com/module/details/35) module.

---

## CURL

cURL is a powerful command-line tool used in Linux distributions, macOS, and even the latest Windows PowerShell versions. We can request any website by simply providing its URL, and we would get it in text-format, as follows:

Minimuss74@htb[/htb]$ curl http://SERVER_IP:PORT/

  

</html>

<!DOCTYPE html>

  

<head>

    <title>Secret Serial Generator</title>

    <style>

        *,

        html {

            margin: 0;

            padding: 0;

            border: 0;

...SNIP...

        <h1>Secret Serial Generator</h1>

        <p>This page generates secret serials!</p>

    </div>

</body>

  

</html>

  

This is the same HTML we went through when we checked the source code in the first section.

---

## POST Request

To send a POST request, we should add the -X POST flag to our command, and it should send a POST request:

Minimuss74@htb[/htb]$ curl -s http://SERVER_IP:PORT/ -X POST

  

Tip: We add the "-s" flag to reduce cluttering the response with unnecessary data

However, POST request usually contains POST data. To send data, we can use the "-d "param1=sample"" flag and include our data for each parameter, as follows:

Minimuss74@htb[/htb]$ curl -s http://SERVER_IP:PORT/ -X POST -d "param1=sample"

  

Now that we know how to use cURL to send basic POST requests, in the next section, we will utilize this to replicate what server.js is doing to understand its purpose better.

  

The second variable defined is the URL variable, which contains a URL to /serial.php, which should be on the same domain, as no domain was specified.

#### Code Functions

Next, we see that xhr.open is used with "POST" and URL. We can Google this function once again, and we see that it opens the HTTP request defined 'GET or POST' to the URL, and then the next line xhr.send would send the request.

So, all generateSerial is doing is simply sending a POST request to /serial.php, without including any POST data or retrieving anything in return.

The developers may have implemented this function whenever they need to generate a serial, like when clicking on a certain Generate Serial button, for example. However, since we did not see any similar HTML elements that generate serials, the developers must not have used this function yet and kept it for future use.

With the use of code deobfuscation and code analysis, we were able to uncover this function. We can now attempt to replicate its functionality to see if it is handled on the server-side when sending a POST request. If the function is enabled and handled on the server-side, we may uncover an unreleased functionality, which usually tends to have bugs and vulnerabilities within them.

Try applying what you learned in this section by sending a 'POST' request to '/serial.php'. What is the response you get?

curl [http://94.237.56.76:55156](http://94.237.56.76:55156)

on voit le code de la page

curl -s http://SERVER_IP:PORT/ -X POST

curl [http://94.237.56.76:55156](http://94.237.56.76:55156) -X POST

RIEN …

However, POST request usually contains POST data. To send data, we can use the "-d "param1=sample"" flag and include our data for each parameter, as follows:

curl -s http://SERVER_IP:PORT/ -X POST -d "param1=sample"

curl [http://94.237.56.76:55156](http://94.237.56.76:55156) -X POST -d "param1=sample"

rien… On cherche sur la page serial.php

curl http://94.237.56.76:55156/serial.php -X POST -d "param1=sample"

N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz

ok

curl http://94.237.56.76:55156/serial.php -X POST -d "param1=Coucou"

MARCHE aussi

# Decoding

---

After doing the exercise in the previous section, we got a strange block of text that seems to be encoded:

Minimuss74@htb[/htb]$ curl http:/SERVER_IP:PORT/serial.php -X POST -d "param1=sample"

  

ZG8gdGhlIGV4ZXJjaXNlLCBkb24ndCBjb3B5IGFuZCBwYXN0ZSA7KQo=

  

This is another important aspect of obfuscation that we referred to in More Obfuscation in the Advanced Obfuscation section. Many techniques can further obfuscate the code and make it less readable by humans and less detectable by systems. For that reason, you will very often find obfuscated code containing encoded text blocks that get decoded upon execution. We will cover 3 of the most commonly used text encoding methods:

- base64
    
- hex
    
- rot13
    

---

## Base64

base64 encoding is usually used to reduce the use of special characters, as any characters encoded in base64 would be represented in alpha-numeric characters, in addition to + and / only. Regardless of the input, even if it is in binary format, the resulting base64 encoded string would only use them.

#### Spotting Base64

base64 encoded strings are easily spotted since they only contain alpha-numeric characters. However, the most distinctive feature of base64 is its padding using = characters. The length of base64 encoded strings has to be in a multiple of 4. If the resulting output is only 3 characters long, for example, an extra = is added as padding, and so on.

#### Base64 Encode

To encode any text into base64 in Linux, we can echo it and pipe it with '|' to base64:

Base64 Encode

Minimuss74@htb[/htb]$ echo https://www.hackthebox.eu/ | base64

  

aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K

  

#### Base64 Decode

If we want to decode any base64 encoded string, we can use base64 -d, as follows:

Base64 Decode

Minimuss74@htb[/htb]$ echo aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K | base64 -d

  

https://www.hackthebox.eu/

  

---

## Hex

Another common encoding method is hex encoding, which encodes each character into its hex order in the ASCII table. For example, a is 61 in hex, b is 62, c is 63, and so on. You can find the full ASCII table in Linux using the man ascii command.

#### Spotting Hex

Any string encoded in hex would be comprised of hex characters only, which are 16 characters only: 0-9 and a-f. That makes spotting hex encoded strings just as easy as spotting base64 encoded strings.

#### Hex Encode

To encode any string into hex in Linux, we can use the xxd -p command:

Hex Encode

Minimuss74@htb[/htb]$ echo https://www.hackthebox.eu/ | xxd -p

  

68747470733a2f2f7777772e6861636b746865626f782e65752f0a

  

#### Hex Decode

To decode a hex encoded string, we can use the xxd -p -r command:

Hex Decode

Minimuss74@htb[/htb]$ echo 68747470733a2f2f7777772e6861636b746865626f782e65752f0a | xxd -p -r

  

https://www.hackthebox.eu/

  

---

## Caesar/Rot13

Another common -and very old- encoding technique is a Caesar cipher, which shifts each letter by a fixed number. For example, shifting by 1 character makes a become b, and b becomes c, and so on. Many variations of the Caesar cipher use a different number of shifts, the most common of which is rot13, which shifts each character 13 times forward.

#### Spotting Caesar/Rot13

Even though this encoding method makes any text looks random, it is still possible to spot it because each character is mapped to a specific character. For example, in rot13, http://www becomes uggc://jjj, which still holds some resemblances and may be recognized as such.

#### Rot13 Encode

There isn't a specific command in Linux to do rot13 encoding. However, it is fairly easy to create our own command to do the character shifting:

Rot13 Encode

Minimuss74@htb[/htb]$ echo https://www.hackthebox.eu/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'

  

uggcf://jjj.unpxgurobk.rh/

  

#### Rot13 Decode

We can use the same previous command to decode rot13 as well:

Rot13 Decode

Minimuss74@htb[/htb]$ echo uggcf://jjj.unpxgurobk.rh/ | tr 'A-Za-z' 'N-ZA-Mn-za-m'

  

https://www.hackthebox.eu/

  

Another option to encode/decode rot13 would be using an online tool, like [rot13](https://rot13.com/).

---

## Other Types of Encoding

There are hundreds of other encoding methods we can find online. Even though these are the most common, sometimes we will come across other encoding methods, which may require some experience to identify and decode.

If you face any similar types of encoding, first try to determine the type of encoding, and then look for online tools to decode it.

Some tools can help us automatically determine the type of encoding, like [Cipher Identifier](https://www.boxentriq.com/code-breaking/cipher-identifier). Try the encoded strings above with [Cipher Identifier](https://www.boxentriq.com/code-breaking/cipher-identifier), to see if it can correctly identify the encoding method.

Other than encoding, many obfuscation tools utilize encryption, which is encoding a string using a key, which may make the obfuscated code very difficult to reverse engineer and deobfuscate, especially if the decryption key is not stored within the script itself.

  

Using what you learned in this section, determine the type of encoding used in the string you got at previous exercise, and decode it. To get the flag, you can send a 'POST' request to 'serial.php', and set the data as "serial=YOUR_DECODED_OUTPUT".

On rappelle : 

Minimuss74@htb[/htb]$ curl http:/SERVER_IP:PORT/serial.php -X POST -d "param1=sample"

  

N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz

Minimuss74@htb[/htb]$ echo https://www.hackthebox.eu/ | base64

  

aHR0cHM6Ly93d3cuaGFja3RoZWJveC5ldS8K

### on encode en base 64

Pour décoder en base64: 

echo N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz | base64 -d

7h15_15_a_s3cr37_m3554g3

### encode en hex

Minimuss74@htb[/htb]$ echo https://www.hackthebox.eu/ | xxd -p

  

68747470733a2f2f7777772e6861636b746865626f782e65752f0a

  

Minimuss74@htb[/htb]$ echo N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz | xxd -p -r

  

rien…

###   

### Ceaser encoding 

Minimuss74@htb[/htb]$ echo N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz | tr 'A-Za-z' 'N-ZA-Mn-za-m'

  

A2tkAI8kAI9uK3ZmL3VmA19gZmH1ATpm

maintenant on essaie avec les deux clefs

base64 : 

7h15_15_a_s3cr37_m3554g3

rot13 Ceaser : 

A2tkAI8kAI9uK3ZmL3VmA19gZmH1ATpm

  

curl http://94.237.56.76:55156/serial.php -X POST -d "serial=7h15_15_a_s3cr37_m3554g3"

HTB{ju57_4n07h3r_r4nd0m_53r14l}

OUI

curl http://94.237.56.76:55156/serial.php -X POST -d "serial=A2tkAI8kAI9uK3ZmL3VmA19gZmH1ATpm"

N2gxNV8xNV9hX3MzY3IzN19tMzU1NGcz

  

  

# Skills Assessment

Target: 94.237.56.76:37626

 Try to study the HTML code of the webpage, and identify used JavaScript code within it. What is the name of the JavaScript file being used?

[http://94.237.56.76:37626](http://94.237.56.76:37626)

inspect / debugger 

api.min.js

  

 Submit

+ 1  Once you find the JavaScript code, try to run it to see if it does any interesting functions. Did you get something in return?

  

eval(function (p, a, c, k, e, d) { e = function (c) { return c.toString(36) }; if (!''.replace(/^/, String)) { while (c--) { d[c.toString(a)] = k[c] || c.toString(a) } k = [function (e) { return d[e] }]; e = function () { return '\\w+' }; c = 1 }; while (c--) { if (k[c]) { p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]) } } return p }('t 5(){6 7=\'1{n\'+\'8\'+\'9\'+\'a\'+\'b\'+\'c!\'+\'}\',0=d e(),2=\'/4\'+\'.g\';0[\'f\'](\'i\',2,!![]),0[\'k\'](l)}m[\'o\'](\'1{j\'+\'p\'+\'q\'+\'r\'+\'s\'+\'h\'+\'3}\');', 30, 30, 'xhr|HTB|_0x437f8b|k3y|keys|apiKeys|var|flag|3v3r_|run_0|bfu5c|473d_|c0d3|new|XMLHttpRequest|open|php|n_15_|POST||send|null|console||log|4v45c|r1p7_|3num3|r4710|function'.split('|'), 0, {}))

[https://beautifier.io/](https://beautifier.io/)

eval(function(p, a, c, k, e, d) {

    e = function(c) {

        return c.toString(36)

    };

    if (!''.replace(/^/, String)) {

        while (c--) {

            d[c.toString(a)] = k[c] || c.toString(a)

        }

        k = [function(e) {

            return d[e]

        }];

        e = function() {

            return '\\w+'

        };

        c = 1

    };

    while (c--) {

        if (k[c]) {

            p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c])

        }

    }

    return p

}('t 5(){6 7=\'1{n\'+\'8\'+\'9\'+\'a\'+\'b\'+\'c!\'+\'}\',0=d e(),2=\'/4\'+\'.g\';0[\'f\'](\'i\',2,!![]),0[\'k\'](l)}m[\'o\'](\'1{j\'+\'p\'+\'q\'+\'r\'+\'s\'+\'h\'+\'3}\');', 30, 30, 'xhr|HTB|_0x437f8b|k3y|keys|apiKeys|var|flag|3v3r_|run_0|bfu5c|473d_|c0d3|new|XMLHttpRequest|open|php|n_15_|POST||send|null|console||log|4v45c|r1p7_|3num3|r4710|function'.split('|'), 0, {}))

[http://jsconsole.com](http://jsconsole.com)

copier le code coller entrer

HTB{j4v45cr1p7_3num3r4710n_15_k3y}

  

 Submit

 Hint

+ 1  As you may have noticed, the JavaScript code is obfuscated. Try applying the skills you learned in this module to deobfuscate the code, and retrieve the 'flag' variable.

[http://www.jsnice.org/](http://www.jsnice.org/)

'use strict';

/**

 * @return {undefined}

 */

function apiKeys() {

  /** @type {string} */

  var flag = "HTB{n" + "3v3r_" + "run_0" + "bfu5c" + "473d_" + "c0d3!" + "}";

  /** @type {!XMLHttpRequest} */

  var xhr = new XMLHttpRequest;

  /** @type {string} */

  var url = "/keys" + ".php";

  xhr["open"]("POST", url, !![]);

  xhr["send"](null);

}

console["log"]("HTB{j" + "4v45c" + "r1p7_" + "3num3" + "r4710" + "n_15_" + "k3y}");

on copie le code du var flag dans la console 

et on envoie 

[http://jsconsole.com](http://jsconsole.com)

'use strict';

/**

 * @return {undefined}

 */

function apiKeys() {

  /** @type {string} */

  var flag = "HTB{n" + "3v3r_" + "run_0" + "bfu5c" + "473d_" + "c0d3!" + "}";

  /** @type {!XMLHttpRequest} */

  var xhr = new XMLHttpRequest;

  /** @type {string} */

  var url = "/keys" + ".php";

  xhr["open"]("POST", url, !![]);

  xhr["send"](null);

}

console["log"]("HTB{n" + "3v3r_" + "run_0" + "bfu5c" + "473d_" + "c0d3!" + "}");

  

HTB{n3v3r_run_0bfu5c473d_c0d3!}

  

  

  

 Submit

 Hint

+ 1  Try to Analyze the deobfuscated JavaScript code, and understand its main functionality. Once you do, try to replicate what it's doing to get a secret key. What is the key?

 */

function apiKeys() {

  /** @type {string} */

  var flag = "HTB{n" + "3v3r_" + "run_0" + "bfu5c" + "473d_" + "c0d3!" + "}";

  /** @type {!XMLHttpRequest} */

  var xhr = new XMLHttpRequest;

  /** @type {string} */

  var url = "/keys" + ".php";

  xhr["open"]("POST", url, !![]);

  xhr["send"](null);

url : [http://94.237.56.76:37626](http://94.237.56.76:37626)/keys.php

curl http:/SERVER_IP:PORT/serial.php -X POST -d "param1=sample"

curl [http://94.237.56.76:37626](http://94.237.56.76:37626)/keys.php POST -d "param1=sample"

error il n’aime pas le POST…

on fait plus simple 

curl http://94.237.56.76:37626/keys.php -X POST                

4150495f70336e5f37333537316e365f31355f66756e

voilà notre clef, on va la décoder 

echo 4150495f70336e5f37333537316e365f31355f66756e | base64 -d

�^t��_�M���_߽�ߝ��^�߮_�]����

non

echo 4150495f70336e5f37333537316e365f31355f66756e  | xxd -p -r

API_p3n_73571n6_15_fun

peut être

echo 4150495f70336e5f37333537316e365f31355f66756e | tr 'A-Za-z' 'N-ZA-Mn-za-m'

4150495s70336r5s37333537316r365s31355s66756r

non

curl [http://94.237.56.76:37626](http://94.237.56.76:37626)/keys.php -X POST -d "serial=API_p3n_73571n6_15_fun"

4150495f70336e5f37333537316e365f31355f66756e

tadam

  

  

  

  

 Submit

+ 2  Once you have the secret key, try to decide it's encoding method, and decode it. Then send a 'POST' request to the same previous page with the decoded key as "key=DECODED_KEY". What is the flag you got?

curl [http://94.237.56.76:37626](http://94.237.56.76:37626)/keys.php -X POST -d "key=API_p3n_73571n6_15_fun"

HTB{r34dy_70_h4ck_my_w4y_1n_2_HTB}

# conclusion

Voici un résumé de ce que nous avons appris :

Tout d'abord, nous avons extrait le code source HTML de la page web et localisé le code JavaScript. Ensuite, nous avons appris différentes méthodes pour obfusquer le code JavaScript. Après cela, nous avons appris comment rendre lisible et désobfusquer le code JavaScript minifié et obfusqué. Ensuite, nous avons examiné le code désobfusqué et analysé sa fonction principale. Ensuite, nous avons appris à faire des requêtes HTTP et avons réussi à reproduire la fonction principale du code JavaScript obfusqué. Enfin, nous avons découvert diverses méthodes pour encoder et décoder des chaînes de caractères

  

  


**