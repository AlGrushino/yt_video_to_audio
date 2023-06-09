import pytube
from pytube import exceptions
import os


def url_youtube():
    url = input('Введите сслыку на видео:')
    exceptions_dict = {
        'RegexMatchError': f'Ссылка {url} не работает',
        'LiveStreamError': f'Можно скачать звук только с завершённых стримов',
        'MembersOnly': f'Видео доступно только для платных подписчиков'
    }
    try:
        url_yt = pytube.YouTube(url)
        audio = url_yt.streams.filter(
            only_audio=True,
            file_extension='mp4'
        )[0]
    except pytube.exceptions.RegexMatchError:
        print(exceptions_dict['RegexMatchError'])
    except pytube.exceptions.LiveStreamError:
        print(exceptions_dict['LiveStreamError'])
    except pytube.exceptions.MembersOnly:
        print(exceptions_dict['MembersOnly'])
    else:
        print(f'Ссылка {url} работает')
        return audio


def address():
    path = input('Введите путь к директории, куда будет сохранено аудио:')
    if os.path.exists(path):
        if os.path.isdir(path):
            return path
        else:
            print(f'{path} не является директорией')
    else:
        print(f'Директории {path} не существует')


def main():
    try:
        url_youtube().download(address())
    except AttributeError:
        print('Что-то пошло не так')


if __name__ == '__main__':
    main()
