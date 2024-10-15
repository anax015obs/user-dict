
from konlpy.tag import Okt
import pandas as pd 
import time, os
import re

def multiprocessing_initializer():
    global okt
    okt = Okt()

def process(i: str) -> str:
    okt_pos = okt.pos(i, norm=False, stem=False);
    word_list = []
    for idx, word in enumerate(okt_pos):
        # if word[1] not in ['Josa', 'Punctuation', 'Suffix', 'Adjective', 'Verb' ] or (word[1] == 'Josa' and idx != len(okt_pos) - 1): 
        #     word_list.append(word[0])
        if word[1] in ['Foreign']: continue;
        # 조사, 구두점 제거. 조사가 마지막에 붙어있을 경우 제거하지 않음
        if word[1] not in ['Josa', 'Punctuation', 'Suffix', 'Adjective', 'Verb' ] or (word[1] == 'Josa' and idx != len(okt_pos) - 1): 
            word_list.append(word[0])
    return ''.join(word_list);



def convert():
    start = int(time.time())

    pq = pd.read_parquet('korean_noun.parquet');

    if os.path.exists('korean_noun.txt'):
        os.remove('korean_noun.txt');

    if os.path.exists('korean_noun_result.txt'):
        os.remove('korean_noun_result.txt');


    pq.to_csv('korean_noun.txt', sep='\t', index=False);

    # read file 
    f = open('korean_noun.txt', 'r', encoding='utf-8');

    # toString
    i = f.read();
    # split by space or hypen
    iarr = i.replace('-', ' ').replace('–', ' ').split(' ');

    onlykoregex = re.compile(r'\d|[a-zA-Z]');

    map = dict();
    for i in iarr:
        if onlykoregex.search(i): continue;
        if len(i) == 1: continue;    
        map[i] = 1;


    iarr = list(map.keys());
    
    from multiprocessing import Pool
    with Pool(8, initializer=multiprocessing_initializer) as pool:
        results = pool.map(process, iarr)
    
    o = '\n'.join(results);
    
    # write file
    f = open('korean_noun_result.txt', 'w', encoding='utf-8');
    f.write(o);
    print("***run time(sec) :", int(time.time()) - start)