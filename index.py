import convert
import rmdup
from konlpy.tag import Okt
import re
from convert import multiprocessing_initializer, process
from itertools import product

if __name__ == "__main__":
    # convert.convert(); # <- 여기 인자값을 주는 순간 
    # rmdup.rmdup(); # <- 이쪽에서 중복제거가 안됨..?

    iarr = ['루비 온 최순실']
    from multiprocessing import Pool
    with Pool(8, initializer=multiprocessing_initializer) as pool:
        results = pool.starmap(process, zip(iarr, (True,)))

    o = '\n'.join(results);
    print(o)