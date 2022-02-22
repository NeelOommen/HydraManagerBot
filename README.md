# HydraManagerBot
## A discord bot meant to 'clean-up' messages sent by the popular Hydra Discord Bot

Hydra's Manager is a bot written in python to interact with Discord's API, to 'manage' messages sent by the Hydra Discord Bot.
Hydra is a popular bot that enables server members to play music in their server's Voice channels. In doing so, it also sends 
many messages and embeds, often cluttering up a server's text channels. 

![image](https://user-images.githubusercontent.com/70756241/155105260-5d7e7040-f31f-48c9-8383-2713891c92fe.png)
![image](https://user-images.githubusercontent.com/70756241/155105314-15a6ed18-772e-4165-b656-a2431b6e0644.png)
![image](https://user-images.githubusercontent.com/70756241/155105352-9c94b945-b967-4458-91e6-b813cc868578.png)

Many servers resort to having a separate channel for bot commands,but Hydra's manager simply deletes these messages from the text channel
they were sent in, along with user commands to Hydra that begin with the '.' character.

#Hydra's Manager only checks a message's author, and if the message begins with the '.' prefix, IT DOES NOT READ ANY OTHER CONTENTS OF THE MESSAGE.

This code is meant to be run on the [replit](https://replit.com/) online IDE, and if you wish to repurpose/reuse this project:
1. Create a new repl on replit
2. Copy the contents of main and keep_online files respectively.
3. Create a bot on the [Discord Developer Page](https://discord.com/developers/applications)
4. Copy the Bot token from the Dev page and add it as an environment variable to your replit
5. Run the replit

# Note:
Replit only hosts running web servers for upto an hour after the latest recieved request, so to ensure uptime/availability,
this project makes use of the most basic web server using flask (in the keep_online file), and then a request is submitted 
periodically using a 3rd Party Service to ensure the bot stays online (in this case, I have made use of the [UpTime Robot](https://uptimerobot.com) service).

For a guide on the basics of setting up a discord bot, setting up the repl for hosting the bot, as well as ensuring its availability using UpTime Robot,
feel free to refer to the material I used, [this guide](https://www.youtube.com/watch?v=SPTfmiYiuok) by [FreeCodeCamp.org](https://www.freecodecamp.org/)

If you do decide to make use of this project yourself for further use and expansion, a reference back to this repository or attribution would be really great!
