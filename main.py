import json
import pandas as pd
from IPython.display import display
import os


def collect_all_wt(link_to_json_raw, path_to_export_raw, excel_name):
    link_to_json = link_to_json_raw.replace(os.sep, '/')
    path_to_export = path_to_export_raw.replace(os.sep, '/')
    text_wtb = ('wtb', 'WTB', '#wtb', '#WTB', 'Wtb', 'WTb', 'WtB', 'wtB', 'wtB')
    text_wts = ('wts', 'WTS', '#wts', '#WTS', 'Wts', 'WTs', 'WtS', 'wtS', 'wtS')
    data = []

    for root, dirs, files in os.walk(link_to_json):
        for filename in files:

            with open(link_to_json+'/'+filename, "r", encoding='utf-8') as read_file:
                developer = json.load(read_file)

            for item in developer['messages']:
                date = item['date']
                from_user = item.get("from_id")
                list_hashtag = []
                wtbwts = ''
                list_iter = []
                if type(item['text']) == list:
                    for mes in item['text']:
                        if type(mes) == dict:
                            list_hashtag.append(mes['text'])
                        else:
                            list_hashtag.append(mes)

                    if ''.join(list_hashtag).startswith(text_wtb):
                        wtbwts = 'wtb'
                    elif ''.join(list_hashtag).startswith(text_wts):
                        wtbwts = 'wts'
                        #  print(mes)

                    list_hashtag = ' '.join(list_hashtag)

                else:
                    list_hashtag = item['text']
                    if ''.join(list_hashtag).startswith(text_wtb):
                        wtbwts = 'wtb'
                    elif ''.join(list_hashtag).startswith(text_wts):
                        wtbwts = 'wts'

                    list_hashtag = ''.join(list_hashtag)

                if len(list_hashtag) < 70:
                    list_iter.append(date)
                    list_iter.append(list_hashtag)
                    list_iter.append(wtbwts)
                    list_iter.append(from_user)
                    data.append(list_iter)

    columns = ['date', 'mes', 'wt', 'from']

    df = pd.DataFrame(data, columns=columns)

    df.to_excel(path_to_export+'/' + excel_name + '.xlsx')
    display(df)


link_to_json_raw = input('ссылка на папку с файлами: ')
path_to_export_raw = input('куда вывести: ')
excel_name = input('название выходного экселя: ')



collect_all_wt(link_to_json_raw,path_to_export_raw, excel_name)