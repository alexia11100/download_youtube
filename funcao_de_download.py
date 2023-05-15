#funçãos de download
import pytube
import os

def limpar_tela():
    os.system("cls")

def baixar_mp4():
    link_mp4 = input("Cole seu URL: ")
    youtube_mp4 = pytube.YouTube(link_mp4)
    youtube_mp4.streams.get_by_resolution("720p").download("meus_videos")
    print("Video baixado.")

def baixar_mp3():
    link_mp3 = input("Cole seu URL: ")
    youtube_mp3 = pytube.YouTube(link_mp3)
    youtube_mp3.streams.get_audio_only().download("meus_audios")
    print("Audio baixado.")