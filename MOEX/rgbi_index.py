from imports import *



def get_RGBI_info():
    '''
    Получение словаря с индексом RGBI
    '''
    dict = {}
    URL = f'http://iss.moex.com/iss/statistics/engines/stock/markets/index/analytics/RGBI.json?iss.meta=off&limit=200'
    response = requests.get(URL).json()
    number_index = 1
    for row in response['analytics']['data']:
        ticker = row[2]
        dict[number_index] = {"Название индекса" : row[0],
                              "тикер" : row[2],
                              "Короткое имя" : row[3],
                              "secid" : row[4],
                              "Доля в индексе" : row[5],
                              "Торговая сессия" : row[6]}
        number_index +=1
    return dict
