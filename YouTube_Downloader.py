# Install before running:
# pytube (pip install pytube)
# progress (pip install progress)
# To run, type python YouTube_Downloader.py
# If python is installed incorrectly, this program may run into issues.
# For testing, input "test" as the first input for a short 1 second video instead of a URL
# For manual testing, use the following 1 second youtube video =
# https://www.youtube.com/watch?v=jhFDyDgMVUI  

# Colors
import os
Color_Off='\033[0m'       # Text Reset
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
BYellow='\033[1;33m'      # Bold Yellow
BPurple='\033[1;35m'      # Bold Purple
BGreen='\033[1;32m'       # Bold Green
On_Red='\033[41m'         # Red Background
On_Green='\033[42m'       # Green Background
On_IGreen='\033[0;102m'   # High Intensity Green Background
URed='\033[4;31m'         # Red Underlined

# Variables
from pytube import YouTube      # Basis for the program to work! 
exit_token = False              # If set to true, allows user to break loop with an exit()
from datetime import timedelta  # For converting seconds to HR:MIN:SEC
from re import search           # For using RegEx to peform searches
help_token = False              # If set to true, opens a help document.
current_directory_token = False # If set to true, denotes that user has used the -d switch.

#Easter Egg Variables
rick_roll_token = False         # If set to true, opens a Rick Roll Easter Egg
emoji_token = False             # If set to true, modify the progress bar
import webbrowser               # For playing Never Gonna Give You Up
import time                     # For sleep timer
from time import sleep          # Sleep timer
from progress.bar import Bar    # For giving the dummy progress bar before opening the video

# Defines desktop path for different for an OS. 
import sys 
from sys import platform
if platform.lower() == "linux" or platform.lower() == "linux2": #Linux
    download_dir = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')   
elif platform.lower() == "darwin": # Mac OSX                
    download_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
elif platform.lower() == "win32": # Windows
    download_dir = f"{os.getenv('USERPROFILE')}\\Desktop"
else :
    download_dir = ""   # Defaults to current working directory if OS can not be detected.
    print (Red+"Warning, unable to detect OS. Files will be saved to current directory."+Color_Off)
# Main

print ("\n")
print(On_Red+"   __  __           ______      __            ____                      __                __           "+Color_Off)
print(On_Red+"   \ \/ /___  __  _/_  __/_  __/ /_  ___     / __ \____ _      ______  / /___  ____ _____/ /__  _____  "+Color_Off)
print(On_Red+"    \  / __ \/ / / // / / / / / __ \/ _ \   / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/  "+Color_Off)
print(On_Red+"    / / /_/ / /_/ // / / /_/ / /_/ /  __/  / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /      "+Color_Off)
print(On_Red+"   /_/\____/\__,_//_/  \__,_/_.___/\___/  /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/       "+Color_Off)
print(On_Red+"                                                                                                       "+Color_Off)
print(On_Red+"   Created by Derek Matthew Fong  |  github.com/derek-m-fong  |  2022  |  Version 1.0                     "+Color_Off)
print(On_Red+"                                                                                                       "+Color_Off)      
print(Color_Off)                                                                                                                                                                                                              
print ("*******************************************************************************************************")
print ("*  "+URed+"ONLY DOWNLOAD IF YOU HAVE PERMISSION. YOU ARE RESPONSIBLE FOR FOLLOWING ALL RULES AND REGULATIONS."+Color_Off+" *")
print ("*                                                                                                     *")
print ("*  To bypass user inputs, use the [-s] switch followed by what type of download you want.             *")
print ("*  "+Blue+"[youtube url] -s -[-video/-audio]" +Color_Off +" this will download the highest quality available for video/audio.*")
print ("*  Example = "+Green+"youtube.com/watch?v=dQw4w9WgXcQ -s -video"+Color_Off+"                                                *")
print ("*  You can type "+Red+"QUIT"+Color_Off+" at any time to exit the program.                                                 *")
print ("*  For more information input type [--help] at any time to bring up the help page and exit.           *")
print ("*******************************************************************************************************")
print ("\n")

while True :
    split_token = False         # Determines if a switch was used and how to proceed if so.
    loop_breaker = False        # To break out of first While loop and go to the second While loop
    restart_token = False       # Allows loop to restart if the -s switch is used wrong 
    link = input("Input your "+On_Red+" YouTube "+Color_Off+" URL to start="+"\n"+Blue)
    print (Color_Off) # All user inputs are colored blue, this makes sure it is reset.
    if link.lower() == "quit" :
        exit_token = True
        break
    if link.lower() == "--help" : 
        help_token = True   
        break
    if link.lower() == "rickroll" : # Easter Egg
        rick_roll_token = True
        break
    if link.lower() == "rickroll -emoji" : # Additional Easter Egg
        rick_roll_token = True
        emoji_token = True
        break
    if link.lower() == "test" : # Downloads a small 1 second video for testing in the default location (usually the Desktop)
        link = "https://www.youtube.com/watch?v=jhFDyDgMVUI&ab_channel=WaitOneSecondHere"
        yt_var = YouTube(link)
        stream=yt_var.streams.get_lowest_resolution()
        stream.download(download_dir)
        print (URed+"TEST COMPLETED. CHECK",download_dir,"FOR A VIDEO CALLED = One Second Video.mp4"+Color_Off+"\n")
        exit()
    if len(link.split()) > 1 : 
        link = link.split() # Split is required to ensure there is no issues with URL names and switches
        split_token = True  # To denote that link has been split or not
        if search("youtube.com", link[0]) : # Search required to make sure first index is a valid URL.
            pass
        elif search("youtu.be", link[0]) :  # Youtube's shortened URL path. 
            pass
        else : 
            print (URed+"WARNING, SWITCHES MUST COME AFTER THE YOUTUBE LINK 👎.")
            print ("ONLY YOUTUBE.COM AND YOUTU.BE SUPPORTED AT THIS TIME.")
            print ("OR MAYBE TRY PUTTING IN A DIFFERENT INPUT ALL TOGETHER"+Color_Off)
            exit()
    if "-D" in link and "-d" in link :
        print (URed+"USE ONLY ONE DIRECTORY SWITCH 👎."+Color_Off)
        exit()
    if "-d" in link :
        print (Green+"Setting current directory as the path to save files..." + Color_Off)
        sleep (.5)
        current_directory_token = True # For if statement to give better feedback of where files are saved
        download_dir = ""  # i.e current directory.       
    if "-D" in link : 
        print (On_Red+"NOTE! This switch is designed for advanced users. [--help] for more info. You can press QUIT to exit."+Color_Off+"\n")
        usr_input = input("What path do you want to save your video in?="+"\n"+Blue)
        download_dir = usr_input 
        if usr_input.lower() == "quit" :
            exit()
        if usr_input.lower() == "--help" :
            help_token = True 
            break
        print (Color_Off) # All user inputs are colored blue, this makes sure it is reset.
    if "-s" in link :
        if "-video" in link and "-audio" in link :
            print (URed+"Only select ONE choice of -video or -audio 👎."+Color_Off)
            exit()
        if "-video" in link :
            try :
                if split_token == True :
                    yt_var = YouTube(link[0]) # defined as [0] to ensure only URL's are processed, not switches if present
                if split_token == False :
                    yt_var = YouTube(link) # used when there are no switches present
                print ("Downloading..."+"\n")
                stream=yt_var.streams.get_highest_resolution()
                stream.download(download_dir)
                if current_directory_token == True : 
                    print ("Video downloaded! You can find it in your current directory."+"\n")
                    print ("😊"+"\n")
                    exit_token = True
                    break
                if current_directory_token == False :
                    print ("Video downloaded! You can find it in",Red+ download_dir +Color_Off+"\n")
                    print ("😊"+"\n")
                    exit_token = True
                    break
            except: 
                print (URed+"There was an error downloading your YouTube video!")
                print ("You can type --help to get more information on this."+Color_Off+"\n")
                print ("☹️"+"\n")
                exit_token = True
                break
        if "-audio" in link :
            try : 
                if split_token == True :
                    yt_var = YouTube(link[0]) # defined as [0] to ensure only URL's are processed, not switches if present
                if split_token == False :
                    yt_var = YouTube(link) # used when there are no switches present
                print ("Downloading..."+"\n")
                stream=yt_var.streams.get_audio_only()
                stream.download(download_dir)
                if current_directory_token == True :
                    print ("Audio downloaded! You can find it in this current directory."+"\n")
                    print ("😊"+"\n")
                    exit_token = True
                    break
                if current_directory_token == False : 
                    print ("Audio downloaded! You can find it in",Red+ download_dir +Color_Off+"\n")
                    print ("😊"+"\n")
                    exit_token = True
                    break
            except : 
                print (URed+"There was an error downloading your YouTube video!")
                print ("You can type --help to get more information on this."+Color_Off+"\n")
                print ("☹️"+"\n")
                exit_token = True
                break
        else:
            print (URed+"Specify if you want -video or -audio with the -s switch."+Color_Off+"\n")
            restart_token = True 
    if restart_token == False and help_token == False: # loop as long as [-s] is not used. This contains the error loop too.
        try :
            while True : 
                print ("\n")
                print ("Processing data...")
                if split_token == True :
                    yt_var = YouTube(link[0]) # defined as [0] to ensure only URL's are processed, not switches if present
                if split_token == False :
                    yt_var = YouTube(link) # used when there are no switches present
                print ("\n")
                print("Title  of video =", yt_var.title)
                print ("Number of views =", f'{yt_var.views:,}')
                sec = yt_var.length
                td = timedelta(seconds=sec)
                print("Length of video =", td) 
                print ("\n")
                usr_input= input("Is this the correct video? ( "+Green+"YES"+Color_Off+" / "+Red+"NO"+Color_Off+" / "+On_Red+" QUIT "+Color_Off+" )"+"\n"+Blue)
                print (Color_Off) # All user inputs are colored blue, this makes sure it is reset.
                if usr_input.lower() == "yes":
                    loop_breaker = True
                    break
                if usr_input.lower() == "quit":
                    exit_token = True
                    break
                if usr_input.lower() == "no" :
                    break
                if usr_input.lower() == "--help" :
                    help_token = True
                    break
                else : 
                    print (URed+"TRY A DIFFERENT INPUT"+"\n"+Color_Off) 
        except :
            print (URed+"PROGRAM ERROR! PLEASE TRY A DIFFERENT LINK OR DIFFERENT SYNTAX!"+"\n"+Color_Off)
            print ("You can type "+On_Red+" QUIT "+Color_Off+" to exit the program"+Red+" at any time."+Color_Off+"\n")
    if loop_breaker == True :
        break
    if exit_token == True :
        break
    if help_token == True :
        break

if exit_token == True :
    print ("Good-bye")
    exit()

while True and help_token == False and rick_roll_token == False: # Only actives if they haven't used --help or rickroll
    back_token = False      # Allows you to go to the previous loop without exiting the program.
    exit_token = False      # Allows you to break out of the loop without triggering try errors. 
    usr_input = input("What type of download do you want? ( "+Green+"VIDEO"+Color_Off+" / "+Purple+"AUDIO"+Color_Off+" / "+On_Red+" QUIT "+Color_Off+" )"+"\n"+Blue)
    print (Color_Off) # All user inputs are colored blue, this makes sure it is reset.
    if usr_input.lower() == "quit" :
        exit()
    if usr_input.lower() == "--help" :
        help_token = True
        break
    if usr_input.lower() == "video":
        while True and help_token == False:
            back_token = False
            usr_input = input("What quality of video do you want? ( "+Green+"HIGHEST"+Color_Off+" / "+Purple+"LOWEST"+Color_Off+" / "+Blue+"OTHER"+Color_Off+" / "+On_Red+" QUIT "+Color_Off+" )"+"\n"+Blue)
            print (Color_Off) # All user inputs are colored blue, this makes sure it is reset.
            if usr_input.lower() == "quit":
                exit()
            if usr_input.lower() == "--help" :
                help_token = True
                break
            if usr_input.lower() == "highest":
                try :
                    print ("Downloading..."+"\n")
                    stream=yt_var.streams.get_highest_resolution()
                    stream.download(download_dir)
                    if current_directory_token == True : 
                        print ("Video downloaded! You can find it in the current directory."+"\n")
                        print ("😊"+"\n")
                        exit_token = True
                        break
                    if current_directory_token == False : 
                        print ("Video downloaded! You can find it in",Red+ download_dir +Color_Off+"\n")
                        print ("😊"+"\n")
                        exit_token = True
                        break
                except: 
                    print (URed+"There was an error downloading your YouTube video!")
                    print ("You can type --help to get more information on this."+Color_Off+"\n")
                    print ("☹️"+"\n")
                    exit_token = True
                    break
            if usr_input.lower() == "lowest":
                try :
                    print ("Downloading..."+"\n")
                    stream=yt_var.streams.get_lowest_resolution()
                    stream.download(download_dir)
                    if current_directory_token == True :
                        print ("Video downloaded! You can find it in the current directory"+"\n")
                        print ("😊"+"\n")
                        exit_token = True
                        break
                    if current_directory_token == False :
                        print ("Video downloaded! You can find it in",Red+ download_dir +Color_Off+"\n")
                        print ("😊"+"\n")
                        exit_token = True
                        break
                except: 
                    print (URed+"There was an error downloading your YouTube video!")
                    print ("You can type --help to get more information on this."+Color_Off+"\n")
                    print ("☹️"+"\n")
                    exit_token = True
                    break
            if usr_input.lower() == "other":
                print ("Let me process that for you..."+"\n")
                str_data = str(yt_var.streams.filter(only_video=True))
                arr = (str_data.split(", "))
                i=1 # Number assigned to download options (tied to itag and itag_dict)
                itag_dict={}
                mp4_token = False # Tracks if mp4 data has been saved or not. 
                print (Cyan+"webm is more compressed and lower quality, but is better for performance on websites.")
                print ("mp4 is a higher quality format and can be used in more systems."+"\n"+Color_Off)
                print (On_Red+" NOTE: THIS ONLY DOWNLOADS THE VIDEO: THERE WILL BE NO AUDIO EMBEDDED. "+Color_Off+"\n")
                print (" SELECT "+On_Red+" BACK "+Color_Off+" TO CHOOSE HIGHEST OR LOWEST IF THIS IS NEEDED. "+"\n")
                for data in arr: 
                    split_data=(data.split())
                    sorted_data = split_data[1:5+1]
                    itag_data_type = (sorted_data[0].split("=\"")[1])[:-1]
                    video_data_type = ((sorted_data[1].split("/"))[1])[:-1]
                    resolution_data_type = (sorted_data[2].split("=\"")[1])[:-1]
                    fps_data_type = (sorted_data[3].split("=\"")[1])[:-1]
                    vcodec_data_type = (sorted_data[4].split("=\"")[1])[:-1]
                    itag_dict[str(i)]=itag_data_type
                    if "mp4" in data and mp4_token == False: # Finds first intance of mp4 and saves it.
                        highest_itag = i
                        mp4_token = True
                    if "webm" in data : # Finds last intance of webm and saves it.
                        lowest_itag = i
                    if len(resolution_data_type) > 4 : # Formatting for 3 or 4 char in string (ex: 360p vs 1080p)   
                        if i < 10 : # Formatting for user input data if only 1 char long (1-9)
                            if "mp4" in data :
                                print (str(i)," --",Red+"Video type=",video_data_type," "+Blue+"Resoltion=",resolution_data_type,Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)
                            if "webm" in data :
                                print (str(i)," --",Red+"Video type=",video_data_type,Blue+"Resoltion=",resolution_data_type,Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)                      
                        if i >= 10 : # Formatting for user input data if 2 char long (10+) 
                            if "mp4" in data :
                                print (str(i),"--",Red+"Video type=",video_data_type," "+Blue+"Resoltion=",resolution_data_type,Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)
                            if "webm" in data :
                                print (str(i),"--",Red+"Video type=",video_data_type,Blue+"Resoltion=",resolution_data_type,Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)
                    if len(resolution_data_type) <= 4 : # Formatting for 3 or 4 char in string (ex: 360p vs 1080p)
                        if i < 10 : # Formatting for user input data if only 1 char long (1-9)
                            if "mp4" in data :
                                print (str(i)," --",Red+"Video type=",video_data_type," "+Blue+"Resoltion=",resolution_data_type," "+Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)
                            if "webm" in data :
                                print (str(i)," --",Red+"Video type=",video_data_type,Blue+"Resoltion=",resolution_data_type," "+Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)
                        if i >= 10 : # Formatting for user input data if 2 char long (10+) 
                            if "mp4" in data :
                                print (str(i),"--",Red+"Video type=",video_data_type," "+Blue+"Resoltion=",resolution_data_type," "+Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)
                            if "webm" in data :
                                print (str(i),"--",Red+"Video type=",video_data_type,Blue+"Resoltion=",resolution_data_type," "+Green+"FPS=",fps_data_type,Purple+"codec=",vcodec_data_type+Color_Off)
                    i+=1
                while True and help_token == False:
                    print ("\n")       
                    if len(arr) < 10 : # Formatting if answer is only 1 char long
                        print ("For the highest quality video select = "+On_Green,str(highest_itag),Color_Off)
                        print ("For the lowest  quality video select = "+On_Red,str(lowest_itag),Color_Off+"\n")
                    if len(arr) >= 10 : # Formatting if answer is 2 char long
                        print ("For the highest quality video select = "+On_Green," "+str(highest_itag),Color_Off)
                        print ("For the lowest  quality video select = "+On_Red,str(lowest_itag),Color_Off+"\n")
                    usr_input = input("Please select which video you want to download ( "+Green+"1-"+str(len(arr))+Color_Off+" /"+Purple+" BACK"+Color_Off+" / "+On_Red+" QUIT "+Color_Off+" )"+"\n"+Blue)
                    print (Color_Off) # All user inputs are colored blue, this makes sure it is reset.)
                    if usr_input.lower() == "quit" :
                        exit_token = True
                        break
                    if usr_input.lower() == "back" :
                        back_token = True
                        break
                    if usr_input.lower() == "--help" :
                        help_token = True
                        break
                    if usr_input.isnumeric() == True and int(usr_input) in range(i) and int(usr_input) > 0: # Checks to usr_input is a valid number
                        try :
                            print ("Downloading..."+"\n")
                            stream=yt_var.streams.get_by_itag(itag_dict[usr_input])
                            stream.download(download_dir)
                            if current_directory_token == True :
                                print ("Video downloaded! You can find it in the current directory."+"\n")
                                print ("😊"+"\n")
                                exit_token = True
                                break
                            if current_directory_token == False :
                                print ("Video downloaded! You can find it in",Red+ download_dir +Color_Off+"\n")
                                print ("😊"+"\n")
                                exit_token = True
                                break
                        except: 
                            print (URed+"There was an error downloading your YouTube video!")
                            print ("You can type --help to get more information on this."+Color_Off+"\n")
                            print ("☹️"+"\n")
                            exit_token = True
                            break
                    else :
                        print (URed+"Please only input a number in the range of 1 - "+str(i-1)+Color_Off+"\n")        
                if exit_token == True :
                    break
            if back_token == False and exit_token == False:  # Error only if they input a wrong string in the first loop, ignores users going backwards or exiting
                print (URed+"TRY A DIFFERENT INPUT"+"\n"+Color_Off)
            if exit_token == True:
                break
    if exit_token == True :
        break
    if usr_input.lower() == "audio":
        try:
            print ("Downloading..."+"\n")
            stream=yt_var.streams.get_audio_only()
            stream.download(download_dir)
            if current_directory_token == True :
                print ("Audio downloaded! You can find it in the current directory."+"\n")
                print ("😊"+"\n")
                exit_token == True
                break
            if current_directory_token == False :
                print ("Audio downloaded! You can find it in",Red+ download_dir +Color_Off+"\n")
                print ("😊"+"\n")
                exit_token == True
                break
        except : 
            print (URed+"There was an error downloading your YouTube video!")
            print ("You can type --help to get more information on this."+Color_Off+"\n")
            print ("☹️"+"\n")
            exit_token == True
            break
    if exit_token == True:
        break
    if back_token == False: 
        print (URed+"TRY A DIFFERENT INPUT"+"\n"+Color_Off)

if exit_token == True :
    print ("Good-bye")
    exit ()

if help_token == True :
    print (BPurple+"***********************************************************************************************"+Color_Off)
    print (BPurple+"*                                                                                             *"+Color_Off)
    print (BPurple+"*         ██╗  ██╗███████╗██╗     ██████╗         ██████╗  █████╗  ██████╗ ███████╗           *"+Color_Off)
    print (BPurple+"*         ██║  ██║██╔════╝██║     ██╔══██╗        ██╔══██╗██╔══██╗██╔════╝ ██╔════╝           *"+Color_Off)
    print (BPurple+"*         ███████║█████╗  ██║     ██████╔╝        ██████╔╝███████║██║  ███╗█████╗             *"+Color_Off)
    print (BPurple+"*         ██╔══██║██╔══╝  ██║     ██╔═══╝         ██╔═══╝ ██╔══██║██║   ██║██╔══╝             *"+Color_Off)
    print (BPurple+"*         ██║  ██║███████╗███████╗██║             ██║     ██║  ██║╚██████╔╝███████╗           *"+Color_Off)
    print (BPurple+"*         ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝             ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝           *"+Color_Off)
    print (BPurple+"*                                                                                             *"+Color_Off)
    print (BPurple+"***********************************************************************************************"+Color_Off)
    print ("\n")          

    print (On_IGreen+"This program was developed by Derek Matthew Fong during his time at Full Stack Academy in 2022."+Color_Off)
    print (On_IGreen+"      github.com/AltOption     |     linkedin.com/in/derekmfong     |      derekmfong.com      "+Color_Off+"\n")

    print ("For help on getting Pytube to run, please visit https://github.com/pytube/pytube")
    print ("To install pytube try pip install pytube, or Google how to use pytube.")
    print ("Pytube is a standalone program that can run on the commandline. This program leverages")
    print ("Pytube as the basis of the program to give more visual feedback when downloading.")
    print ("If you need more specific or refined results in your download, run pytube from the CLI."+"\n")

    print ("The following switches can be used during the inital operation of Youtube_Downloader =")
    print ("[-s],[-video],[-audio],[-d],[-D],[--help],[test],[rickroll]"+"\n")

    print (Yellow+"[test]"+Color_Off+" = used for testing purposes"+"\n")

    print ("Used as a standalone input during the start of the program, it will download a one second, low")
    print ("quality youtube video to your Desktop (actual path noted during download process). Use this")
    print ("option to test to make sure the program works or to familiarize yourself with the inputs."+"\n")

    print (Blue+"<youtube link> [-s] [-video] or [-audio]"+Color_Off+"= Downloads the highest quality video or audio."+"\n")

    print ("By default, this will be saved to the Desktop. In some cases (see below), that path will be the")
    print ("current working directory instead. You may get an error if the video already exists in this location."+"\n")
  
    print (Cyan+"<youtube link> [-d] "+Color_Off+"= Saves the video to the current working directory."+"\n")

    print ("It is possible for this to run into errors if you are in a folder that you can't write files to.")
    print ("Additionally, you will have processing errors if the video is already in your directory. By default,")
    print ("files are saved to the Desktop. If the OS can not be detected, files will be saved in the current")
    print ("directory. Please ensure that you have the correct privledge to write in the current directory.")
    print ("Problems can arise when using the [-D] switch if the input is not exact. Because of this, it is")
    print ("recommended that you enter the directory you want to save files in and then use the [-d] switch")
    print ("instead of potentially saving the file in the wrong folder."+"\n")
 

    print (Purple+"<youtube link> [-D]"+Color_Off+" = Saves the youtube video to a defined path."+"\n")

    print ("Note that the path shouldn't be defined during the initial input. [-D] will trigger")
    print ("A special prompt which will then ask for the desired path. Note that this path is NOT")
    print ("checked by the system so if your path is called /Desktop and you input /desktop")
    print ("You will now make a new folder called desktop (with a lowercase d) intead.")
    print ("Note that you must use the full path, as ~ or similar shortcuts (ex: tabbing) won't work.")
    print ("If this folder has not been created, this will create the folder for the user during download."+"\n")

    print (BYellow+"Other potential inputs you may run into can be found if you have selected VIDEO then OTHER:"+Color_Off+"\n")
   
    print ("If a user has NOT used the [-s] switch and has chosen to download a video, they are given")
    print ("The option to either enter HIGHEST, LOWESET, or OTHER. HIGHEST and LOWEST download videos")
    print ("automatically set to their respective qualities, but OTHER will *ONLY* download the video.")
    print ("In other words, HIGHEST/LOWEST downloads video mixed with audio, while OTHER is ONLY video.")
    print ("To note, audio can be quickly downloaded with the [-s] [-audio] switches after the link."+"\n")

    print ("In the OTHER option, two of the main differences between the videos will be MP4 and webm.")
    print ("MP4 is much higher quality, and it is the defaulted option when trying the HIGHEST switch.")
    print ("webm is a more compressed format that is good for sending small files or lowering rendering")
    print ("time on a website. Note that this option will not import audio. By default, the LOWEST")
    print ("option during the quality prompt will mix audio and video together in an MP4 format."+"\n")

    print ("If you get an error downloading your video, ensure that the video is not already in that location.")
    print ("Errors can be caused by a number of factors, including wrong permissions to the file path,")
    print ("disruptions during the download process, errors in YouTube's API, or errors with pytube.")
    print ("If you enter a URL shortener or use something other than youtube.com/$ or youtu.be/$ you will")
    print ("also get an automatic error because the program looks for those specific terms."+"\n")

    print ("If additional refinement is needed, you can always run this program via the CLI version.")
    print ("pytube --help will give you more information how to use this program in that way."+"\n")

    print (BGreen+"[rickroll]"+Color_Off+" = Test it out! You can try adding"+BGreen+" [-emoji] "+Color_Off+"to it too."+"\n")

    print ("Typing "+On_Green+" --help "+Color_Off+" at any time will bring this page up.")

    print ("Typing "+On_Red+" QUIT "+Color_Off+" at any time will exit the program." +"\n")

    print ("Please follow all local rules and regulations before downloading videos.")

# Lets users pick emoji for progress bar
if emoji_token == True :
    emoji_input = input ("Enter an emoji of choice="+"\n")
    emoji = emoji_input
else :
    emoji = "💀"

if rick_roll_token == True :

    print("⣿⣿⣿⠿⡿⠀⠀⠈⠙⣿⣿⡿⠁⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⡇⢸⣟⣿⣿⣿⣿⣿⣿⣟⣵⣦⡀⠏⣿⡄⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺")
    print("⣿⣿⣇⣤⡇⠀⠀⠀⣴⣿⠿⠃⠀⣭⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⢸⣿⡟⣇⣾⡗⠀⠀⠀⠨⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸")
    print("⣿⣿⡏⡏⡅⠀⢀⣴⣿⣿⣿⣿⠶⢿⣽⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠋⠉⠉⠉⠉⠉⠉⠙⠛⠋⠳⣼⣽⣇⢿⡇⣿⡆⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣷⣅⣷⠀⣼⣿⣿⣿⡿⣿⣯⣽⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣾⣿⣿⣧⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⢿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣿⡿⣿⡄⣻⣧⠠⠴⡇⢸⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠸⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⣧⠹⣿⣿⡄⠀⠀⡇⢸⡛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠸⠂⠘⣇⡀⠙⢿⡗⠀⠀⡷⢸⢱⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⡿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠇⢀⣤⡶⠶⢿⡿⠿⠿⢦⡀⠸⣾⣿⣿⡿⠿⠷⢶⣤⣄⠀⢻⣧⠀⡾⠁⠀⠀⡇⢸⢄⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠")
    print("⣿⣿⡟⠇⠿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀⡟⠀⣡⣴⣶⣶⣧⠈⠁⠀⠀⠈⠙⠿⠾⠷⠶⣦⣄⣹⡆⠀⣿⣾⠇⠀⠀⠀⡟⢸⢀⠟⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠿")
    print("⣿⣿⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠁⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡇⠀⣧⣟⣀⡀⠀⠀⣷⣀⣘⣧⣤⣤⣶⣶⣶⣿⣿⣿⣿⣿⡉⠉⠀⠀⠀")
    print("⣿⣿⡇⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠐⣆⡀⠀⠀⠀⠀⠀⠀⠇⠀⣿⠙⢿⣽⣟⠋⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠚⠉⠀")
    print("⣿⣿⡇⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠙⣷⠀⠀⠀⠀⠀⠀⠀⣠⡶⣶⣦⣷⣭⣿⡄⠀⠀⠀⠀⠀⡎⠀⢿⣇⢸⣷⡿⠶⢶⡶⢾⠛⠋⠙⠋⠉⣨⣿⣦⣽⢧⡀⠀⠀⠀⠀⠀")
    print("⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⣼⠏⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠋⠉⠁⠀⠙⠀⠀⠀⠀⠀⢿⠀⣨⠿⣿⠁⠀⣀⡞⠀⠘⣆⣠⠞⢀⣴⣿⣿⣿⣿⣿⣝⣇⠀⠀⠀⠀")
    print("⣿⣿⡇⠋⠀⠀⣀⣀⣤⠤⠄⠀⠀⠀⠀⣿⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡁⢀⡿⠀⠀⠈⢷⠀⢀⡟⠀⢀⣾⣿⣿⣿⠟⠻⣿⣿⣿⠳⣄⣀⢀")
    print("⣿⣿⠇⣼⣿⣿⡿⣿⡻⣲⢶⠄⠀⠀⠀⣿⣿⣆⡠⠀⠀⠀⠀⠀⣴⣿⣿⣭⣭⣭⣿⣷⡦⠀⠀⠀⠀⠀⢠⢿⣿⣿⣦⣥⣄⡀⢸⣀⣤⣀⣴⣿⣿⣿⡟⠃⠀⠀⠈⠻⣿⣷⣈⠉⠉")
    print("⣿⣿⠰⡇⠐⠈⠀⠋⣩⡽⣿⠀⠠⣄⠰⣿⣟⣿⠟⢧⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⢠⡾⡏⠀⠟⣿⣿⣿⣿⠛⢻⣿⣿⣿⡿⢻⠏⠀⠀⠀⠀⠀⠈⣿⣿⣿⣆⠀")
    print("⣿⣿⢸⠇⠀⢴⣾⣿⣖⡯⣿⡇⠀⢮⠉⣿⣎⣋⣠⣾⡁⠀⠀⠀⠀⠀⠻⢤⣤⠞⡁⠀⠀⠀⠀⠀⢠⠿⣼⢿⡛⡄⢸⣿⣿⡿⠀⣿⣿⣿⣿⣿⣷⣶⠴⢶⣄⣀⣤⠌⠿⠛⠛⢻⡄")
    print("⣿⡿⢸⠀⠀⠉⣻⣿⢵⣻⣿⠀⠀⣟⠷⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠲⣶⣶⡞⠃⠀⠀⠀⠀⠀⠀⠀⢻⡊⢳⣶⡛⠿⠿⣷⡤⣾⣿⣿⣿⠏⠉⠉⠠⣤⡌⠉⠀⠀⠀⠀⠀⠀⠱")
    print("⣿⡇⣿⠀⠰⣿⣿⣿⡽⣾⣿⠀⠰⢯⣠⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢸⣿⣿⣦⣄⠈⣧⢘⣿⣿⡇⠀⢀⣀⣤⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⠀⢈⣺⣿⣿⣯⣿⡇⠀⢘⠳⣿⣿⣿⣿⣿⠿⠍⠿⣿⠀⠘⠲⣤⣄⣀⣀⣀⣀⣠⠾⠃⠀⠀⢀⡞⠀⣾⣿⣿⣿⣿⣷⣝⣃⡿⢿⠇⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⠀⣸⣿⣿⣿⣺⢽⠇⠀⢨⣹⣿⣿⣿⣿⣯⣠⣤⣴⢛⡇⠀⠀⠈⠙⢿⣿⠟⠉⠀⠀⠀⠀⣠⠟⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣶⣶⣤⣤⣤⣀⣀⠀⠀⠀")
    print("⣿⣿⣿⠁⣽⢟⣿⡟⠋⠛⠀⠀⠓⢬⣿⣿⣿⣿⡏⠀⡼⠁⣼⡇⠀⠀⠀⠀⠀⢶⡄⠀⠀⠀⢀⡴⠃⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶")
    print("⣿⣿⣿⠁⣤⣿⣿⣷⡶⣶⣤⣄⣀⣸⣾⣿⣿⣿⡇⢸⠇⠀⣿⡇⠀⠀⠀⠀⠀⠙⠟⠀⢀⡴⠋⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⡖⠸⢿⡍⣼⣹⡟⡉⠹⡍⠁⢸⣿⣿⣿⣷⣿⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⢈⣷⠟⠁⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⡇⠁⠈⡟⠿⢻⠘⠶⠄⡇⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⡻⣦⠀⠀⠀⢀⣴⠿⠋⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")

    with Bar('Rick Rolling= ', fill=emoji, suffix='%(percent).1f%% - %(eta)ds') as bar:
        for i in range(100):
            sleep(.01)
            bar.next()
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1')  
    exit()
