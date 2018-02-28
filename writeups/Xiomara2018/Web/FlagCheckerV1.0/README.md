# Flag Checker V1.0

[website](./Flag checker.html)

Upon opening the website, a dialog box asks us to "Enter the flag". When we enter an incorrect flag, we get the response "You got wrong flag". Looking at the source of the web page, we see the JavaScript file main.js. The code is obfuscated and coded in !, [, ], (, ), and +. The following is a snippet of main.js:

```
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])
```

I googled for "javascript deobfuscator brackets execlamation" and found out this was JSFuck. I found a JSFuck decoder [here](https://enkhee-osiris.github.io/Decoder-JSFuck/).

The decoded JavaScript is:
```
$flag = prompt("Enter the flag");  if($flag == "xiomara{0bfusc@tion_c@n_b3_e@sy_@s_j5fuck}") {         alert("You got right flag"); } else { alert("You got wrong flag"); }
```

The flag is xiomara{0bfusc@tion_c@n_b3_e@sy_@s_j5fuck}.