from pytube import YouTube

link = input("introduce el enlace del video: ")
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()

print("Iniciando descarga...")
stream.download()
print("descarga finalizada")