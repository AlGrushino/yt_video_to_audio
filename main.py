import pytube


def url_youtube():
    url_yt = pytube.YouTube(input('Введите сслыку на видео: '))
    return url_yt


def address():
    address = input('Введите путь к папке, куда будет сохранено аудио: ')
    return address


def main():
    audio = url_youtube().streams.filter(only_audio=True, file_extension='mp4')[0]
    audio.download(address())
    print('done, congrats!!!!!\n'
          'u r greate programmer!!!!')


if __name__ == '__main__':
    main()



