# RepTronics Discord Bot    
### Setup Instructions    
```
Step 1. Make sure you have the required dependencies in requirements.txt.
pip install -r /path/to/requirements.txt

Step 2.
In the info.json file, input the following information.
Guild ID, Admin Members (User ID), User/Users to be messages with relevant logs. (USER ID), Allowed Channel ID's, Users allowed to use the /ts command (USER ID)
Then, input the bot token in the token.env file
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
The bot will log when people attempt to run admin commands, or run commands in the non specified channels (any channel other then #bot-commands)
