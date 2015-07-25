```
                     _____      
 _      _____  ___  / __(_)___ _
| | /| / / _ \/ _ \/ /_/ / __ `/
| |/ |/ /  __/  __/ __/ / /_/ / 
|__/|__/\___/\___/_/ /_/\__, /  
                       /____/
Adds figlet capabilities to weechat.
```
#Installation:

-pip install pyfiglet (if you do not already have the pyfiglet library)

-clone this repository to any directory

-copy weefig.py to ~/.weechat/python

-in weechat run 
```
/python load weefig.py
```
#Usage:
```
/fig [-f <font> -c <foreground theme,background theme>] text
```
An example being 
```
/fig -f larry3d -c white,rainbow Hello World
```
This would print Hello World in the larry3d font with white text and a rainbow background.

Additionally, the -f and -c options can be left out if you have no desire to deviate from the standard color or font.
```
/fig Hello World
```
Would print Hello World in the standard font and the standard color for your client.

Another point of note is that using the "term" font will echo back your text unaltered, therefore, if you just want to color your text you can use:
```
/fig -f term -c <color> <text>
```

Please visit http://www.figlet.org/examples.html to learn more about the available fonts.

#Acknowledgements:

This script uses pyfiglet, so I would like to thank both the developers of figlet, and its python port pyfiglet.
