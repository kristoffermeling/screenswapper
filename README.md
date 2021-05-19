# screenswapper

The program checks the current running processes, and compares it to the programs.txt list, if the process is running, the multi-monitor setup will change to only use one screen. when the process terminates the screen configuration reverts back to multi monitor setup.

to run hidden from startup, place the ScreenSwapperBackgroundLauncher in the startup folder, and edit the path to the target .cmd file.
1.open the windows run and type "shell:startup" to open startup folder.
2.edit the path in both ScreenSwapperBackgroundLauncher and the ScreenSwapper.cmd
3. the program should now run silently in the background on startup.

