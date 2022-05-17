from imports import *



from MOEX.get_boards import get_boards
from MOEX.get_columns_board import get_dict_columns
from MOEX.get_marketdata_board import get_marketdata_board
from MOEX.rgbi_index import get_RGBI_info



from create_files.create_xlsx import do_excel



if __name__ == '__main__':
    dict_boards_T_plus, dict_boards_all = get_boards()
    dict_RGBI = get_RGBI_info()
    dict_all = {}
    for board in dict_boards_T_plus.keys():
        dict_columns = get_dict_columns(board)
        dict_RGBI, dict_all = get_marketdata_board(dict_columns, dict_RGBI, dict_all, dict_boards_T_plus[board]['board'])
    do_excel(dict_RGBI, dict_all)
    print('Формирование файлов завершено')
