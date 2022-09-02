"""
Created on Fri Aug 26 20:22:40 2022

@author: Vitor
"""

from pytube import YouTube,streams
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

def pastas():
    pasta = filedialog.askdirectory() ## escolhe destinatário
    return pasta

def videos():
    video = YouTube(Pegarlink())
    pasta=pastas()
    baixarvideo = video.streams.get_highest_resolution()
    baixarvideo.download(pasta)
    
def audios():
    video = YouTube(Pegarlink()) # Chama a função de Pegar Link
    pasta=pastas()
    
    baixaraudio = video.streams.get_audio_only() # Pega somente o audio do vídeo
    arquivo_saida=baixaraudio.download(pasta) # baixa o arquivo dentro da pasta em mp4
    base, ext = os.path.splitext(arquivo_saida) 
    nome_novo= base + '.mp3' # formata o arquivo para mp3
    os.rename(arquivo_saida, nome_novo)

def Pegarlink():
    url = link.get()
    return url

root = tk.Tk()
root.geometry("196x120") # Define o Tamanho da tela
root.title("Baixando coisa do YouTube")


txt = Label(root,text="Coloque o Link abaixo")

txt.pack()

link = tk.Entry(root) # Caixa de Texto
link.pack()

mp3botao = tk.Button(text="MP3",command= audios) # Botão MP3
mp3botao.pack()
mp4botao = tk.Button(text="MP4",command= videos) # Botão MP4
mp4botao.pack()    
  
root.mainloop()

