
import datetime
import multiprocessing
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line.strip())
    return all_data

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов 3.91 секунд
    # start_time = datetime.datetime.now()
    # for filename in filenames:
    #     data = read_info(filename)
    # end_time = datetime.datetime.now()
    # print(f'Линейный вызов: {end_time - start_time} секунд')

    # Многопроцессный вызов 7,52 секунды
    start_time = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        all_files = []
        results = pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    print(f'Многопроцессный вызов: {end_time - start_time} секунд')
