# SLChatBotSmiteRank

   These are scripts for the [Streamlabs Chatbot](https://streamlabs.com/chatbot) which can load ranked information for the streamer as well as anyone else using chat commands (!rank & !player by default).
   
NOTE: For these scripts to work the profile being requested cannot be hidden!

## Setup

### Requirements:
   - To set up this script you Must have [Python 2.7](https://www.python.org/download/releases/2.7/) installed (required for     streamlabs chatbot).
   - The Streamlabs Chatbot must be set up. The documentation for the chatbot can be found [here](https://cdn.streamlabs.com/chatbot/Documentation.pdf)
   
### Instructions
   1) Download the Desired script folder (it will download as FOLDER_NAME.zip)
   2) In Streamlabs chatbot select the scripts menu.
   3) Select the import script button.
   4) Navigate to and select the downloaded zip file.
   5) Enable the script with the checkbox in the streamlabs chatbot UI.
   6) Adjust the settings for your stream.
   7) Enjoy!
 
# SmiteRank
   This is the script which loads the streamer's ranked information.
   
## Settings
  This script has several options which can be adjusted in the Streamlabs chatbot UI, they are as follows:
  
### Smite Name:
  The smite in game name you wish to load the stats for.
  
### Game Mode:
 The game mode you wish to load stats for (Ranked: Conquest, Ranked: Duel, Ranked Joust (3v3) are currently supported).
 
### Platform:
 The platform you play smite on (PC, Xbox, or Playstation).
 
### Command:
 The command you wish the script to execute on (!rank by default).
 
### Response:
 The format of the response you wish to have, options for the response are listed below.
 
#### Response Options:
   1) $ign - The IGN (in game name) of the smite account stats have been loaded for.
   2) $mode - The game mode stats have been loaded for.
   3) $division - The current ranked division.
   4) $tp - The current Tribute Point value.
   5) $elo - The current smite guru elo value.
   6) $sg_page - The smite guru page for the given smite account.
   7) $username - The name of the chat user who called this command.
   8) $wins - The number of wins.
   9) $losses - The number of losses.
   10) $matches - The total number of matches played.
   11) $winrate - The winrate.
   
# PlayerRank
   This is the script which can load anybody's ranked information.
   
## Settings
  This script has several options which can be adjusted in the Streamlabs chatbot UI, they are as follows:
  
### Game Mode:
 The game mode you wish to load stats for (Ranked: Conquest, Ranked: Duel, Ranked Joust (3v3) are currently supported).
 
### Platform:
 The platform to load profiles from (PC, Xbox, or Playstation). Currently this will be the only supported platform, but this will be changed to be the default platform and support other platforms by including them in the command (ex: !player KingSalamander PC).
 
### Command:
 The command you wish the script to execute on (!player by default).
 
### Response
 The format of the response you wish to have, options for the response are listed below.
 
#### Response Options:
   1) $ign - The IGN (in game name) of the smite account stats have been loaded for.
   2) $mode - The game mode stats have been loaded for.
   3) $division - The current ranked division.
   4) $tp - The current Tribute Point value.
   5) $elo - The current smite guru elo value.
   6) $sg_page - The smite guru page for the given smite account.
   7) $username - The name of the chat user who called this command.
   8) $wins - The number of wins.
   9) $losses - The number of losses.
   10) $matches - The total number of matches played.
   11) $winrate - The winrate.
       
