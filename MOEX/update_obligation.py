from imports import *



def get_OFZ_info(dict):
    '''
    Дополнение словаря по каждой облигации
    '''
    n = 1
    kol = len(dict.keys())
    for key in dict.keys():
        secid = dict[key]['secid']
        URL = f'https://iss.moex.com/iss/securities/{secid}.json'
        # https://iss.moex.com/iss/securities/SU24020RMFS8.json
        response = requests.get(URL).json()
        for row in response['description']['data']:
            if row[1] in list_rows:
                continue
            else:
                dict[key][row[1]] = row[2]
        print(f'{n:5} из {kol:5} завершено')
        n+=1
    return dict
