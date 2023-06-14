import tkinter as tk
import pytube
from pytube import exceptions
import os


root = tk.Tk()
root.title('AudioTube')
root.geometry('300x250')


def url_youtube():
    url = entry_link.get()
    exceptions_dict = {
        'RegexMatchError': f'Ссылка не работает',
        'LiveStreamError': f'Можно скачать звук только с завершённых стримов',
        'MembersOnly': f'Видео доступно только для платных подписчиков'
    }
    try:
        audio = pytube.YouTube(url).streams.filter(
            only_audio=True,
            file_extension='mp4'
        )[0]
    except pytube.exceptions.RegexMatchError:
        label_url['text'] = exceptions_dict['RegexMatchError']
    except pytube.exceptions.LiveStreamError:
        label_url['text'] = exceptions_dict['LiveStreamError']
    except pytube.exceptions.MembersOnly:
        label_url['text'] = exceptions_dict['MembersOnly']
    else:
        label_url['text'] = f'Ссылка работает'
        return audio


def address():
    path = entry_path.get()
    if os.path.exists(path):
        if os.path.isdir(path):
            label_path['text'] = 'Путь существует'
            return path
        else:
            label_path['text'] = f'Путь не является директорией'
    else:
        label_path['text'] = f'Директории по указанному пути не существует'


def main():
    try:
        url_youtube().download(address())
        label_url['text'] = 'Скачано'
    except AttributeError:
        label_path['text'] = 'Что-то пошло не так'


text_link = tk.Label(text='Введите ссылку на видео:')  # надпись в самом верху
text_link.pack(anchor='center', padx=6, pady=6)
entry_link = tk.Entry(root)  # поле для ввода
entry_link.pack(anchor='center', padx=6, pady=6)


text_path = tk.Label(text='Введите путь до каталога:')
text_path.pack(anchor='center', padx=6, pady=6)
entry_path = tk.Entry(root)
entry_path.pack(anchor='center', padx=6, pady=6)


btn_download = tk.Button(text='Скачать', command=main)  # кнопка с командой
btn_download.pack(anchor='center', padx=6, pady=6)

label_url = tk.Label()
label_url.pack(anchor='center', padx=6, pady=6)
label_path = tk.Label()
label_path.pack(anchor='center', padx=6, pady=6)

root.mainloop()
