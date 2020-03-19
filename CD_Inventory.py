#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# BWorkeneh, 2020-Mar-18, completed TODOs
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        try:
            tplCdInfo = IO.ScreenIO.get_CD_info()
            PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        except Exception as e:
            print(e)
            print ('Make sure entries make sense, \n ID is int, title and artist are str' )
            print('CD not added\n')
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODO add code to handle tracks on an individual CD
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                break
            elif strChoice == 'a':
                try:
                    tInfo= IO.ScreenIO.get_track_info()
                    PC.DataProcessor.add_track(tInfo, cd)
                except Exception as e:
                    print ('\n',e)
                    print('track not added\n')
            elif strChoice == 'd':
                try:
                    IO.ScreenIO.show_tracks(cd)
                except Exception as e:
                    print (e)
            elif strChoice == 'r':
                try:
                    IO.ScreenIO.show_tracks(cd)
                    tID= int(input('Choose the track index: '))
                    cd.rmv_track(tID)
                    IO.ScreenIO.show_tracks(cd)
                except Exception as e:
                    print(e)
            else:
                print('There was an Error')
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')