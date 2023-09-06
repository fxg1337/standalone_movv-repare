from tkinter import *
import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip

from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import messagebox

import shutil

from pytube import *
import subprocess, sys, os
from os.path import join as pjoin
from subprocess import PIPE, run


class Fxg(Tk):
    def __init__(test):
        super(Fxg, test).__init__() # Set up class and Tk
        
    
        test.title("GUI") # Set GUI name
        test.minsize(100, 50) # Set GUI size
        
        test.BStart() # display start button
        test.BQuit() # Display Quite button
        test.SStart()# Display signa start button 

    def BStart(test): # create start button 
        test.Bstart = ttk.Button(test, text = "Batch repair", command = test.fixmoovb )
        test.Bstart.grid(column = 1, row = 2)
        ToolTip(test.Bstart, msg='Start batch repair')
        
    def SStart(test): # create start button 
        test.Bstart = ttk.Button(test, text = "Singel Repair", command = test.fixmoovs )
        test.Bstart.grid(column = 2, row = 2)
        ToolTip(test.Bstart, msg='Singal repair Button')
        

    def BQuit(test):  # create quite button
        test.Bquit = ttk.Button(test, text = "Quit", command = test.AQuit)
        test.Bquit.grid(column = 3, row = 2)
        ToolTip(test.Bquit, msg='Quit Button')
        

    def AQuit(test): # set the quit action 
        test.destroy()
        test.quit()
        

    def fixmoovb(test):
        os.system('cls')
        sufx = ".mp4"
        folder_selected = filedialog.askdirectory() #dmaged files location
        
        # Copy untrunk file to folder
        #------------------------------
        
        # set destnation for untrunk files
        dest1 = folder_selected + r"/untrunc.exe"
        dest2 = folder_selected + r"/AVCODEC-57.DLL"
        dest3 = folder_selected + r"/AVFORMAT-57.DLL"
        dest4 = folder_selected + r"/AVUTIL-55.DLL"
        dest5 = folder_selected + r"/LIBGCC_S_SEH-1.DLL"
        dest6 = folder_selected + r"/LIBSTDC++-6.DLL"
        dest7 = folder_selected + r"/LIBWINPTHREAD-1.DLL"
        dest8 = folder_selected + r"/SWRESAMPLE-2.DLL"

        # set the source path for the untrunk files
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\untrunc.exe"
        src_path2 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVCODEC-57.DLL"
        src_path3 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVFORMAT-57.DLL"
        src_path4 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVUTIL-55.DLL"
        src_path5 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBGCC_S_SEH-1.DLL"
        src_path6 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBSTDC++-6.DLL"
        src_path7 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBWINPTHREAD-1.DLL"
        src_path8 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\SWRESAMPLE-2.DLL"

        # copy the files
        shutil.copy(src_path1, dest1)
        shutil.copy(src_path2, dest2)
        shutil.copy(src_path3, dest3)
        shutil.copy(src_path4, dest4)
        shutil.copy(src_path5, dest5)
        shutil.copy(src_path6, dest6)
        shutil.copy(src_path7, dest7)
        shutil.copy(src_path8, dest8)
        #--------------------------------
        
        NameOfRef = filedialog.askopenfilename() # selcte ref file 
        test.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        test.progress.grid( column = 1, row = 9)
        test.update_idletasks()
        test.progress['value'] += 30
    
        
        os.chdir(folder_selected)
        test.progress['value'] += 30
        for item in os.listdir(folder_selected):
            
            if item.endswith(sufx):
            
                test.progress['value'] += 30
                repair = "untrunc.exe " + NameOfRef + " " + item
            
                test.progress['value'] += 50
                subprocess.call(repair, shell=True)
            


        os.remove("untrunc.exe")
        os.remove("AVCODEC-57.DLL")
        os.remove("AVUTIL-55.DLL")
        os.remove("AVFORMAT-57.DLL")
        os.remove("LIBGCC_S_SEH-1.DLL")
        os.remove("LIBSTDC++-6.DLL")
        os.remove("LIBWINPTHREAD-1.DLL")
        os.remove("SWRESAMPLE-2.DLL")

        RemoveRef = NameOfRef + "_fixed.mp4"
    
        dirnameref, filenameref = os.path.split(NameOfRef)
       
        for i in os.listdir(folder_selected):
           
            if i == filenameref:
                os.remove(RemoveRef)
            elif i == NameOfRef:
                os.remove(NameOfRef)

            else:
                test.progress.destroy()
     

    
    def fixmoovs(test):
        os.system('cls')
        file_selected = filedialog.askopenfilename() # selct dmaged file 
        
        # Copy untrunk file to folder
        #------------------------------
        
        # set destnation for untrunk files
        dest1 = folder_selected + r"/untrunc.exe"
        dest2 = folder_selected + r"/AVCODEC-57.DLL"
        dest3 = folder_selected + r"/AVFORMAT-57.DLL"
        dest4 = folder_selected + r"/AVUTIL-55.DLL"
        dest5 = folder_selected + r"/LIBGCC_S_SEH-1.DLL"
        dest6 = folder_selected + r"/LIBSTDC++-6.DLL"
        dest7 = folder_selected + r"/LIBWINPTHREAD-1.DLL"
        dest8 = folder_selected + r"/SWRESAMPLE-2.DLL"

        # set the source path for the untrunk files
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\untrunc.exe"
        src_path2 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVCODEC-57.DLL"
        src_path3 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVFORMAT-57.DLL"
        src_path4 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVUTIL-55.DLL"
        src_path5 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBGCC_S_SEH-1.DLL"
        src_path6 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBSTDC++-6.DLL"
        src_path7 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBWINPTHREAD-1.DLL"
        src_path8 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\SWRESAMPLE-2.DLL"

        # copy the files
        shutil.copy(src_path1, dest1)
        shutil.copy(src_path2, dest2)
        shutil.copy(src_path3, dest3)
        shutil.copy(src_path4, dest4)
        shutil.copy(src_path5, dest5)
        shutil.copy(src_path6, dest6)
        shutil.copy(src_path7, dest7)
        shutil.copy(src_path8, dest8)
        #--------------------------------
        
        NameOfRef = filedialog.askopenfilename() # selcte ref file 
        test.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        test.progress.grid( column = 1, row = 9)
        test.update_idletasks()
        test.progress['value'] += 30

        
        repair = "untrunc.exe " + NameOfRef + " " + file_selected
        

        os.remove("untrunc.exe")
        os.remove("AVCODEC-57.DLL")
        os.remove("AVUTIL-55.DLL")
        os.remove("AVFORMAT-57.DLL")
        os.remove("LIBGCC_S_SEH-1.DLL")
        os.remove("LIBSTDC++-6.DLL")
        os.remove("LIBWINPTHREAD-1.DLL")
        os.remove("SWRESAMPLE-2.DLL")
        RemoveRef = NameOfRef + "_fixed.mp4"
        os.remove(RemoveRef)
        self.progress.destroy()
    

fxg = Fxg()
fxg.mainloop()
