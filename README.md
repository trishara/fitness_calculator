# Trishara's Fitness Calculator


Description
-----------
This calculator was made to compile all of my body composition data on the Samsung Health App (https://www.samsung.com/global/galaxy/apps/samsung-health/) so I can track trends on my weight loss journey.
<p align="center">
<img src="https://user-images.githubusercontent.com/98492683/151250949-cd872a71-910e-4647-b46f-faf5653c0653.jpg" /></p>

How to Use
----------
1. Find the ```load_existing_file()``` function in main.py.
2. Change the path to where you want your save files to be:  
```files = os.listdir(r"C:\Users\...\....\fitness_calculator")```

3. When you run the program, choose from three options:

<p align="center">
<img src="https://user-images.githubusercontent.com/98492683/151253450-25877de7-b98c-43e1-a7e3-ba5b74817a09.PNG" />
</p>

4. You will prompted to enter your daily weight, body fat %, skeletal muscle, and how many weeks of data you have. This should be the final output:
<p align="center">
<img src="https://user-images.githubusercontent.com/98492683/151282499-62d962d5-d3f7-49d8-ae9f-2ff74e7324f3.PNG" />
</p>


Optional: Turn the script into an executable
--------------------------------------------
<p align="center"><img src="https://user-images.githubusercontent.com/98492683/151406412-ec79787e-131e-4e57-b5d0-721bcd326507.png" /></p>
  
1. First, change the path for your save files to your desktop as described previously. 
2. In the ```print_summary()``` function, add this line of code as the very last line of the function (make sure it is outside the main if-statement). This keeps the program running so the console window doesn't close out immediately after printing your results.

```k = input(f"\n{Fore.LIGHTWHITE_EX}Press [{Fore.RESET}{Fore.LIGHTMAGENTA_EX}EXIT{Fore.RESET}{Fore.LIGHTWHITE_EX}] to close this window.{Fore.RESET}")```

4. Install the auto-py-to-eve module. ```pip install auto-py-to-exe```
5. Run the command ```auto-py-to-exe```
6. Choose script location (make sure the path includes the script).
7. Choose "One File".
8. Click icon and choose the icon I uploaded to this repository's folder.
9. Create the executable. Drag the application to your desktop, the same location where you designated where you want your save files to be. If you don't do this, the application will not be able to properly load and save your data!


FAQ
----
[Q] : Why is there a negative value in the average weight lost/average body fat % lost/average skeletal muscle gained?

[A] : If there is a negative value for either average weight lost or average body fat % lost, it means there was actually a gain instead. The reverse is true for average skeletal muscle gained - a negative value means muscle was lost.


Disclamer
---------
This program was created for personal use but I thought I would share it in case anyone else with fitness watches and/or fitness apps wanted to use it to make sense of their data rather than doing all calculations by hand (that's why I coded this... it gets really tedious!) With that being said, please use at your own risk as I have not carefully sanitized the input during the creation of the save file (just periods, slashes, and escapes) to prevent possible code injection and other possible exploits. In the future I might take the time to fix this, but as of right now that's not something I'm looking to do.
