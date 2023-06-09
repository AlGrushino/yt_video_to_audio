import pytube
import os


def url_youtube():
    url_yt = pytube.YouTube(input('Введите сслыку на видео: '))
    return url_yt


def address():
    address = input('Введите путь к папке, куда будет сохранено аудио: ')
    return address


def main():
    try:
        audio = url_youtube().streams.filter(only_audio=True, file_extension='mp4')[0]
    except pytube.exceptions.RegexMatchError:
        print('ссылка не работает')
    else:
        dir = address()
        if os.path.exists(dir):
            if os.path.isdir(dir):
                audio.download(dir)
                print('done, congrats!!!!!\n'
                      'u r great programmer!!!!')
            else:
                print('указанный путь не является директорией')
        else:
            print('директории не существует')


if __name__ == '__main__':
    main()



