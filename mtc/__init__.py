import os
import click

try:
    import configparser

    def read_string(string):
        parser = configparser.ConfigParser()
        parser.read_string(string)
        return parser

except ImportError:
    import ConfigParser
    import io

    def read_string(string):
        parser = ConfigParser.ConfigParser()
        parser.readfp(io.BytesIO(string))
        return parser


TMUX = os.environ.get('TMUX')
ESC_BEGIN = '\033Ptmux;\033\033]' if TMUX else '\033]'
ESC_END = '\a\033\\' if TMUX else '\a'

COLOR_NAME_CODES = dict(
    foregroundcolour='10;',
    backgroundcolour='11;',
    cursorcolour='12;',
    black='4;0;',
    red='4;1;',
    green='4;2;',
    yellow='4;3;',
    blue='4;4;',
    magenta='4;5;',
    cyan='4;6;',
    white='4;7;',
    boldblack='4;8;',
    boldred='4;9;',
    boldgreen='4;10;',
    boldyellow='4;11;',
    boldblue='4;12;',
    boldmagenta='4;13;',
    boldcyan='4;14;',
    boldwhite='4;15;',
)


def set_color(name, val):
    print('{begin}{color_name}{val}{end}'.format(
        begin=ESC_BEGIN,
        color_name=COLOR_NAME_CODES[name.lower()],
        val=val,
        end=ESC_END))

themes = '''
[onedark]
ForegroundColour=171,178,191
BackgroundColour=30,33,39
CursorColour=97,175,239
BoldBlack=92,99,112
Black=92,99,112
BoldRed=224,108,117
Red=224,108,117
BoldGreen=152,195,121
Green=152,195,121
BoldYellow=209,154,102
Yellow=209,154,102
BoldBlue=97,175,239
Blue=97,175,239
BoldMagenta=198,120,221
Magenta=198,120,221
BoldCyan=86,182,194
Cyan=86,182,194
BoldWhite=171,178,191
White=171,178,191

[material-dark]
BackgroundColour=35,35,34
ForegroundColour=229,229,229
CursorColour=229,229,229
Black=33,33,33
BoldBlack=66,66,66
Red=183,20,31
BoldRed=232,59,63
Green=69,123,36
BoldGreen=122,186,58
Yellow=246,152,30
BoldYellow=255,234,46
Blue=19,78,178
BoldBlue=84,164,243
Magenta=86,0,136
BoldMagenta=170,77,188
Cyan=14,113,124
BoldCyan=38,187,209
White=239,239,239
BoldWhite=217,217,217

[material-light]
BackgroundColour=234,234,234
ForegroundColour=46,46,45
CursorColour=46,46,45
Black=33,33,33
BoldBlack=66,66,66
Red=183,20,31
BoldRed=232,59,63
Green=69,123,36
BoldGreen=122,186,58
Yellow=252,123,8
BoldYellow=253,142,9
Blue=19,78,178
BoldBlue=84,164,243
Magenta=86,0,136
BoldMagenta=170,77,188
Cyan=14,113,124
BoldCyan=38,187,209
White=239,239,239
BoldWhite=217,217,217
'''


def set_theme(theme):
    parser = read_string(themes)
    for k, v in parser.items(theme):
        set_color(k, v)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('theme')
def set(theme):
    set_theme(theme)


if __name__ == '__main__':
    cli()
