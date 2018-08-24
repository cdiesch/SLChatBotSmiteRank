# SLChatBotSmiteRank

   This is a [Streamlabs Chatbot](https://streamlabs.com/chatbot) script which loads the [SMITE](https://streamlabs.com/chatbot) ranked information for the streamer.

## Setup
### Requirements:
   - To set up this script you Must have [Python 2.7](https://www.python.org/download/releases/2.7/) installed (required for     streamlabs chatbot).
   - The python.exe file MUST be under C:\Python27.
   - The Streamlabs Chatbot must be set up. The documentation for the chatbot can be found [here](https://cdn.streamlabs.com/chatbot/Documentation.pdf)
### Instructions
   1) Download the SmiteRank folder (it will download as SmiteRank.zip)
   2) In Streamlabs chatbot select the scripts menu.
   3) Select the import script button.
   4) Navigate to and select the downloaded SmiteRank.zip file.
 
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
   12) $percentile - The percentile of the player.
       
