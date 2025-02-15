@echo off
cd Tools
color c
goto main

:: Tool made by AK
:: Discord: https://discord.gg/umVQB6exMR
:: Discord User: https://discord.gg/umVQB6exMR

:main
title AK 
cls

:: -------------------------------------------------------------------------------

echo.          
echo.          
echo.              ____  _                          __   ______            __
echo.             / __ \(_)_____________  _________/ /  /_  __/___  ____  / /
echo.            / / / / / ___/ ___/ __ \/ ___/ __  /    / / / __ \/ __ \/ / 
echo.           / /_/ / (__  ) /__/ /_/ / /  / /_/ /    / / / /_/ / /_/ / /  
echo.          /_____/_/____/\___/\____/_/   \____/    /_/  \____/\____/_/
echo.          
echo.          
echo.         [1] Webhook Deleter    [6] Bot Spammer
echo.         [2] Webhook Spammer    [7] Nuker (SOON)
echo.         [3] Webhook Tester     [8] Bot Online
echo.         [4] Bot Message Sender 
echo.         [5] Credits            
echo.

:: -------------------------------------------------------------------------------
   
set /p tool=.    =======^> 
if /I %tool% EQU 1 goto tool_1
if /I %tool% EQU 2 goto tool_2
if /I %tool% EQU 3 goto tool_3
if /I %tool% EQU 4 goto tool_4
if /I %tool% EQU 5 goto tool_5
if /I %tool% EQU 6 goto tool_6
if /I %tool% EQU 7 goto tool_7
if /I %tool% EQU 8 goto tool_8
if /I %tool% EQU 9 goto tool_9
if /I %tool% EQU 10 goto tool_10

:tool_1
cls
title Webhook Deleter
python Web_Deleter.py  
pause
goto main

:tool_2
cls
title Webhook Spammer
python Web_spam.py   :
pause
goto main


:tool_3
cls
title Webhook Tester
python Webhook_Tester.py 
pause
goto main


:tool_4
cls
title Bot Message Sender
python Bot_Message_Sender.py 
pause
goto main


:tool_5
cls
title Credits
echo.         ______              ___ __      
echo.        / ____/_______  ____/ (_) /______
echo.       / /   / ___/ _ \/ __  / / __/ ___/
echo.      / /___/ /  /  __/ /_/ / / /_(__  ) 
echo.      \____/_/   \___/\__,_/_/\__/____/ 
echo.      
echo.      
echo.  Discord: https://discord.gg/umVQB6exMR
echo.  Discord User: 505.PY
echo.           
pause
goto main
:tool_6
cls
title Bot Spammer
python Bot_Spammer.py 
pause
goto main

:tool_7
title ERROR
echo coming soon..
pause
goto main

:tool_8
cls
title Bot Online
python Bot_Online.py
pause
goto main

:tool_9
title ERROR
echo coming soon..
pause
goto main

:tool_10
title ERROR
echo coming soon..
pause
goto main

title ERROR
echo Invalid option
pause
goto main
