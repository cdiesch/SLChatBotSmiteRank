import sys
import clr
import os
import json

rank_prog = os.path.join(os.path.abspath(os.path.split(__file__)[0]), 'get-rank.py')

clr.AddReference('IronPython.SQLite.dll')
clr.AddReference('IronPython.Modules.dll')

ScriptName = 'SmiteRank'
Website = 'http://wwww.twitch.tv/TheKingSalamander'
Description = 'Gets the smite rank of the streamer.'
Creator = 'Chris Diesch'
Version = '1.0.1'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari'
                     '/537.11'}

# Settings tags
ign_tag = 'smiteIGN'
platform_tag = 'platform'
mode_tag = 'gameMode'
format_tag = 'responseStr'
cmd_tag = 'command'

# Response format keys
ign_key = '$ign'
mode_key = '$mode'
div_key = '$division'
tp_key = '$tp'
elo_key = '$elo'
url_key = '$sg_page'
user_tag = '$username'
win_tag = '$wins'
loss_tag = '$losses'
wr_tag = '$winrate'
matches_tag = '$matches'

# The default settings
settings = {ign_tag: 'KingSalamander',
            platform_tag: 'PC',
            mode_tag: 'Ranked: Conquest',
            format_tag: '@$username $ign\'s Rank in $mode: $division ($tp TP) Smite Guru elo: $elo '
                        '(more info $sg_page)',
            cmd_tag: '!rank'}

# the path to the settings file
settings_path = os.path.join(os.path.join(os.path.dirname(__file__), 'settings'))
settings_file = os.path.join(settings_path, 'SmiteRank_settings.json')


# Init definition
def Init():
    # load the settings from the settings file if it exists
    global settings
    try:
        if not os.path.exists(settings_path):
            os.makedirs(settings_path)
        if os.path.exists(settings_file):
            with open(settings_file) as reader:
                new_settings = json.load(reader)
                if len(new_settings) != 0:
                    settings = new_settings
        # The command MUST start with '!'
        if not settings[cmd_tag].startswith('!'):
            settings[cmd_tag] = '!%s' % settings[cmd_tag]
    except Exception as ex:
        sys.stderr.write('Unable to load settings from file!\n'
                         'Exception: %s' % str(ex))


# Execute definition
def Execute(data):
    # Is this a chat message and is it the !rank command?
    if data.IsChatMessage() and data.GetParam(0).lower() == settings[cmd_tag]:
        message = ''
        cmd = r'C:\Python27\python.exe "%s" "%s" "%s" --platform "%s"' % \
              (rank_prog,
               settings[ign_tag],
               settings[mode_tag],
               settings[platform_tag])
        with os.popen(cmd) as out:
            message += out.read().replace(os.linesep, '')
        info = json.loads(message)

        message = settings[format_tag]. \
            replace(user_tag, data.User). \
            replace(ign_key, settings[ign_tag]).\
            replace(mode_key, settings[mode_tag]).\
            replace(div_key, info['division']).\
            replace(tp_key, info['tp']).\
            replace(elo_key, info['elo']).\
            replace(url_key, info['url']).\
            replace(win_tag, info['win']).\
            replace(loss_tag, info['loss']).\
            replace(wr_tag, info['wr']).\
            replace(matches_tag, info['matches'])
        # print(message)
        Parent.SendTwitchMessage(message)


# ReloadSettings definition
def ReloadSettings(json_data):
    # Update the settings from stream labs chat bot UI
    global settings
    settings = json.loads(json_data)
    # The command MUST start with '!'
    if not settings[cmd_tag].startswith('!'):
        settings[cmd_tag] = '!%s' % settings[cmd_tag]
    with open(settings_file, 'w+') as writer:
        json.dump(settings, writer)


# Tick definition (does nothing)
def Tick():
    return
