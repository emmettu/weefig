"""
weefig.py
Emmett Underhill
emmettu@gmail.com
0.1
GPL3
A script that lets you print massive obnoxious letters.

Uses the python pyfiglet module [pip install pyfiglet]
Usage: /fig [-f|-c] [font|color] <text>

Notes:
    -/fig -f term <text> will simply echo back text.
    therefore, you can use /fig -f term -c <color> to
    colorize your messages without making them gigantic
    -/fig -c rainbow will turn your text into a rainbow
    -google search figlet fonts and try them out.
"""

SCRIPT_NAME    = "weefig"
SCRIPT_AUTHOR  = "eunderhi, istewart"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "Prints figlet text"
SCRIPT_COMMAND = "fig"

try:
    import weechat
except ImportError:
    print('This script must be run under WeeChat.')
    print('Get WeeChat now at: http://www.weechat.org/')
    import_ok = False

try:
    import re
    import collections
    from pyfiglet import Figlet, FigletFont
except ImportError, message:
    print('Missing package(s) for %s: %s' % (SCRIPT_NAME, message))
    import_ok = False

import_ok = True

COLORS = ["\x0305","\x0304","\x0307","\x0303","\x0302","\x0313","\x0306","","\x0301","\x0300"]
THEMES = {
        "black"       :[[8]],
        "white"       :[[9]],
        "red"         :[[0]],
        "orange"      :[[1]],
        "yellow"      :[[2]],
        "green"       :[[3]],
        "blue"        :[[4]],
        "indigo"      :[[5]],
        "violet"      :[[6]],
        "hrainbow"     :[[0],[1],[2],[3],[4],[5],[6]],
        "vrainbow"     :[[0,1,2,3,4,5,6]],
        "royal"       :[[2,6]],
        "tiger"       :[8,1],
        "zebra"       :[8,9],
        "canada"      :[0,9],
        "america"     :[4,9,0],
        "switzerland" :[0,9],
        "germany"     :[8,0,2],
        "chess"       :[
                        [9,8],
                        [8,9]
                       ],
        "revchess"    :[
                        [8,9],
                        [9,8]
                       ],
        ""            :[[7]]
        }

def weefig_command_cb(data, buffer, args):
    font = "standard"
    color = ""
    text = ""
    args = args.split()

    i=0
    while i < len(args):
        if args[i] == "-f":
            font = args[i+1]
            i+=2
        elif args[i] == "-c":
            color = args[i+1]
            i+=2
        elif args[i] == "--font-list":
            weechat.prnt("","\n".join(FigletFont.getFonts()))
            i+=1
        else:
            text = " ".join(args[i:])
            break
    text = set_text_font(text, font)
    print_color_text(text, color)
    return weechat.WEECHAT_RC_OK

def set_text_font(text, font):
    try:
        figlet = Figlet(font=font)
    except:
        print('weefig: no such font: %s' % (font))
        return ""
    return figlet.renderText(text)

def print_color_text(text, color):
    text = text.split("\n")
    background = ""
    if "," in color:
        color, background = color.split(",")
    try:
        color = THEMES[color]
        background = THEMES[background]
    except:
        print('weefig: illegal color combination: %s,%s' % (color, background))
        return

    for i in range(len(text) - 1):
        line = ""
        if text[i][0] == "/":
            text[i] = "/" + text[i]
        for j in range(len(text[i])):
            foreground_code = COLORS[color[i%len(color)][j%len(color[j%len(color)])]]
            background_code = COLORS[background[i%len(background)][j%len(background[j%len(background)])]][-2:]
            if background_code != "":
                foreground_code += ","
            line += foreground_code + background_code + text[i][j]
        weechat.command("",line)


if __name__ == '__main__' and import_ok:
    if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION,
                        SCRIPT_LICENSE, SCRIPT_DESC, "", ""):

        weechat.hook_command(SCRIPT_COMMAND, SCRIPT_DESC,
                             '[-f font][-c color] <fig text>',
                             'that\'s it',
                             '%(commands)',
                             'weefig_command_cb', '')
