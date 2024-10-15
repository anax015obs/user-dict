
from konlpy.tag import Okt
import pandas as pd 
import time, os
import re
from itertools import product

def multiprocessing_initializer():
    global okt
    okt = Okt()

def process(i: str, debug=False) -> str:
    okt_pos = okt.pos(i, norm=False, stem=False);
    if debug: print(okt_pos);
    
    
    word_list = []
    for idx, word in enumerate(okt_pos):
        oktlen = len(okt_pos);
        if word[1] == 'Noun' or (word[1] == 'Suffix' and oktlen > 1 and idx == oktlen - 1 and okt_pos[idx-1][1] == 'Noun') or (word[1] == 'Josa' and oktlen > 2 and idx != oktlen - 1 and idx != 0 and okt_pos[idx-1][1] == 'Noun' and okt_pos[idx+1][1] == 'Noun'):
            if word[1] == 'Noun': word_list.append(word[0]);
            elif word[1] == 'Suffix': word_list.append(okt_pos[idx-1][0] + word[0]);
            else: word_list.append(okt_pos[idx-1][0] + word[0] + okt_pos[idx+1][0]);
    

    return '\n'.join(word_list);



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
    iarr = i.replace('-', ' ').replace('–', ' ').replace(':', ' ').split(' ');

    onlykoregex = re.compile(r'\d|[a-zA-Z]');

    map = dict();
    for i in iarr:
        if onlykoregex.search(i): continue;
        if len(i) == 1: continue;    
        map[i] = 1;


    iarr = list(map.keys());
    
    from multiprocessing import Pool
    with Pool(8, initializer=multiprocessing_initializer) as pool:
        results = pool.starmap(process, zip(iarr))
    
    o = '\n'.join(results);
    
    # write file
    f = open('korean_noun_result.txt', 'w', encoding='utf-8');
    f.write(o);
    print("***run time(sec) :", int(time.time()) - start)