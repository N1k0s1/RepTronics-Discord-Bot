# RepTronics Discord Bot    
### Setup Instructions    
```
Step 1.
Download/clone the repo.
Make sure you have the required dependencies in requirements.txt
pip install -r /path/to/requirements.txt

Step 2.
In the ids.json file, input the following information.
"ts_users": [1136290556591485039, 978886408964026378, 648794335697043468], - These User IDs are the Users allowed to use the /ts {@user} command.  
"id": 718418845194256404, - This is the Guild ID, used to sync the command tree locally for if any changes are made as guild specific commands sync instantly.
"allowed_users": [1136290556591485039, 978886408964026378], - These are the users allowed to run commands in any channel *WIP*
"allowed_channel_id": 1263491691638292521, - The channel that users are allowed to use commands in, copy the Channel ID.
"admin": 978886408964026378 - The admin user that will recieve logs etc.

Step 3. (Skip if you already have a bot token)
Go to https://discord.com/developers/applications
Click 'New Application'
Choose a name & Accept the TOS.
Go to Bot on the sidebar.
Click on reset token.
Copy the token that comes up.

Step 4.
Input the bot token in the token.env file.

Step 5.
Run the bot!
```

# Commands *(for all members)*   
+ /gen2 - returns a menu with all the AirPod Gen 2 chips  
+ /gen3 - returns a menu with all the AirPod Gen 3 chips  
+ /pro1 - returns a menu with all the AirPod Pro 1 chips  
+ /pro2 - returns a menu with all the AirPod Pro 2 chips  
+ /maxes - returns a menu with all the Airpod Maxes chips 
+ /sellers - returns a menu with all the sellers listed   
+ /quiz - returns a link to a quiz, to help the user decide what model they want to purchase    
+ /ping - returns the bot's ping _might remove it later_ **need to make this an embed at some point, also need to make it admin only, or at least channel locked** 
_restricted commands_   
+ /sync - syncs the bot command tree **need to make this an embed at some point** 
+ /loadcog - loads a cog _currently not using any cogs at the moment as they've been unstable and unreliable_ **need to make this an embed at some point**    
+ /unloadcog - unloads a cog _currently not using any cogs at the moment as they've been unstable and unreliable_ **need to make this an embed at some point**    
+ /ts {@user} - sends the given user a embed, containing a survey on how their support experience was      
# Logging Features
The bot will log when people attempt to run admin commands, when admin commands are run, or when people attempt to run commands in the non specified channels (any channel other then #bot-commands)


![IMG_1162](https://github.com/user-attachments/assets/07233ef1-e421-42c1-a6f4-eb854b9cb5a3)
![IMG_1163](https://github.com/user-attachments/assets/3259fcd5-9458-442e-a965-7b5d890b0500)
