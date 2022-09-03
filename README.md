# discord-servicon-changer
Change your server pic in Discord when the GUI simply doesn't work.

### Storytime

Basically, the reason why i've made this script is just because i had this bug since 2 years where i simply couldnt change the server icon, and i had to change it. And i'm not the kind of guy who likes asking customer service.

### Requirements

discord.py, obtainable with the command "pip install -U discord.py"

### How to use it?

1. Create an application through the [Discord Developer Portal](https://discord.com/developers/applications).
2. Then, go to the Bot section, and then press the "Add Bot" button. Put a fancy name and a fancy image (optional).
3. Activate the "Message Content Intent" under the "Privileged Gateway Intents" section.
4. In the same folder as your .py script, create a file named ".env"
5. Click "Reset Token" and put it in the .env file as shown: "DISCORD_TOKEN=[your token]".
6. Then, go to OAuth2 -> URL Generator, select Bot, then Manage Server.
7. Open the generated URL in a new window, and add it to the server you want to change the icon.
8. Change the image.png with the image you want to add (it has to be PNG, be sure to keep the same name, aka "image.png").
9. Launch the program with "python bot.py".
10. In your Discord server, do the command "?changeicon".
11. voilà
