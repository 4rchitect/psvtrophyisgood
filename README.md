# psvtrophyisgood

psvtrophyisgood Trophy Folder editor For PSVITA!  

using this tool you can edit NPWR folder data, this allows you to unlock, lock, and change the timestamp  
of any trophy in any set.  

# Importing trophys into PSVTIG:  
In order to import trophys into psvtig you need 2 things.  
1. the trophy conf folder, you can find this at ur0:user/00/trophy/conf.  
2. the decrypted trophy data folder, goto ur0:user/00/trophy/data,   
hover over the folder you want and press triangle > open decrypted in vitashell.  

then in PSVTIG click import trophy, and select the conf folder first, and then select the data folder.  
if everything is OK it should import into the program. from there you can edit it.  

# Exporting trophys from PSVTIG:  
So you made some edits to the trophy set, and now you want to put it back onto   
the vita to sync. well first on the main screen select the trophy you want and goto export set  
then just select where you want it, and you'll now have a data/NPWR and a conf/NPWR folder  

copy the data folder somewhere on your vita (just not ur0:/user/00/trophy/data),  
then select both TRPTRANS and TRPTITLE in vitashell and goto copy  
repeat the steps for getting the decrypted files in vitashell again  
once your in the "open decrypted" thing press triangle and paste.   

your folders are now encrypted again so the vita will read them!  

if the trophy app doesnt update, delete ur0:user/00/trophy/data/sce_trop and ur0:user/00/trophy/db  
open the app again it should say restoring, the progress of the set will NOT be correct, do not worry  
let it sync and it will update to the correct progress,  

# Credits
Massive thanks to JustinTrophyGod, for helping me find the majority of bugs during developlment (so I can fix them!)  
Massive thanks to @motoharu @theFlow and @dots_tb for trophy decryption/encryption  
Thanks to AnalogMan for helping me with timezones.  
and thanks to the following beta testers:
frosty, wosley, shadow, levi, Justin, and joslin (aka JustinTrophyGod)  


No commercial use / trophy service use. unless its a free trophy service thanks :D 
