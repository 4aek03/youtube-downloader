
from pytube import YouTube
from moviepy.editor import *


print ('ЗАГРУЗЧИК С YOUTUBE')

def download_video(url, output_path="/Users/nikita/Desktop/"):
    try:
        # Создаем объект YouTube с указанной ссылкой на видео
        yt = YouTube(url)

        # Выбираем наилучшее доступное видео-разрешение для скачивания
        video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        # Скачиваем видео
        print(f"Скачиваем видео: {yt.title}")
        video.download(output_path)

        print("Скачивание завершено!")

    except Exception as e:
        print(f"Произошла ошибка при скачивании: {str(e)}")

def download_audio(url, output_path="/Users/nikita/Desktop/"):
    try:
        # Создаем объект YouTube с указанной ссылкой на видео
        yt = YouTube(url)

        # Выбираем наилучшее доступное видео-разрешение для скачивания
        video = yt.streams.filter(only_audio=True).first()

        # Скачиваем видео
        print(f"Скачиваем аудио: {yt.title}")
        video_file = video.download(output_path, filename="temp")

        # Конвертируем видео в MP3
        audio_path = f"{output_path}/{yt.title}.mp3"
        video_clip = AudioFileClip(video_file)
        video_clip.write_audiofile(audio_path)

        # Удаляем временный видео файл
        video_clip.close()
        os.remove(video_file)

        print("Конвертация в MP3 завершена!")

    except Exception as e:
        print(f"Произошла ошибка при скачивании и конвертации: {str(e)}")


while True:
    print('mp3 -- 0/mp4 -- 1')
    prim = input(': ')


    if prim == "1":
        video = input("введите ссылку:  ")
        if __name__ == "__main__":
            video_url = video
            download_video(video_url)


    elif prim == '0':
        musik = input("введите ссылку:  ")
        if __name__ == "__main__":
            video_url = musik
            download_audio(video_url)


    else:
        print('error')
        continue

# https://www.youtube.com/watch?v=rT_Um174guo