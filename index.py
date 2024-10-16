import convert
import rmdup
from convert import multiprocessing_initializer, process
from lib import archive

if __name__ == "__main__":
    convert.convert(); # <- 여기 인자값을 주는 순간 
    rmdup.rmdup(); # <- 이쪽에서 중복제거가 안됨..?
    archive('archive/user_dict.txt');

    # iarr = ['힐베르트']

    # from multiprocessing import Pool
    # with Pool(8, initializer=multiprocessing_initializer) as pool:
    #     results = pool.starmap(process, zip(iarr, (True,)))

    # o = '\n'.join(results);
    # print(o)