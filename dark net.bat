@echo off
chcp 65001
title DARK NET
color 4
:menu
cls

echo ██████╗░░█████╗░██████╗░██╗░░██╗  ███╗░░██╗███████╗████████╗
echo ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ████╗░██║██╔════╝╚══██╔══╝
echo ██║░░██║███████║██████╔╝█████═╝░  ██╔██╗██║█████╗░░░░░██║░░░
echo ██║░░██║██╔══██║██╔══██╗██╔═██╗░  ██║╚████║██╔══╝░░░░░██║░░░
echo ██████╔╝██║░░██║██║░░██║██║░╚██╗  ██║░╚███║███████╗░░░██║░░░
echo ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚══╝╚══════╝░░░╚═╝░░░
echo.
echo.
echo welome to the dark net
echo.
pause
color 2
echo =================================================
echo 1) here you only pay with bitcoins
echo 2) you can buy a monkey, a Slovak teacher, and so on
echo 3) We are not responsible for any damages
echo ================================================
pause
start https://fakedarknet.wordpress.com/
md adam
md virus
md kubo
md ahoj
md rezen
md paprika
set url="https://www.youtube.com/shorts/Hm5xRNFTASA"
set shortcutName="hudba.lnk"
set desktopFolder=%USERPROFILE%\Desktop

echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = oWS.ExpandEnvironmentStrings("%desktopFolder%") ^& "\" ^& %shortcutName% >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = %url% >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
exit




