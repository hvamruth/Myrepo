import os
import pygame
#used to create video games#
import tkinter as tkr
#used to develope GUI#
import askdirectory
tkinter.filedialog

music_player = tkr.Tk()
music_player.title("Listenit")
music_player.geometry("450x350")

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
returns list of files song

play_list =
tkr.Listbox(music_player,
            font = "helvatica 12 regular",
            bg = "orange",
            selectmode=tkr.SINGLE)

for item in song_list:
    pos = 0
    play_list.insert(pos,item)
    pos += 1

    pygame.init()
    pygame.mixer.init()


    
            
