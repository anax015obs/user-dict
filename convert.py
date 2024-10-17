
from kiwipiepy import Kiwi
import time, os
import re

def multiprocessing_initializer():
    global kiwi
    kiwi = Kiwi()
    kiwi.load_user_dictionary('archive/kiwi_user_dict.txt')

def preprocess(i: str):
    iarr = i.replace('-', ' ').replace('–', ' ').replace(':', ' ').replace('\n', ' ').split(' ');
    onlykoregex = re.compile(r'\d|[a-zA-Z]');

    map = dict();
    for i in iarr:
        if onlykoregex.search(i): continue;
        if len(i) < 3: continue;    
        map[i] = 1;


    return list(map.keys());


def process(i: str, debug=False):
    tokens = kiwi.tokenize(i);
    if debug: print(tokens);
    
    word_list = []
    for i in tokens:
        if i.tag in ['NNP', 'NNG']:
            form = i.form.replace(' ', '');
            word_list.append(form);

    return word_list;

def tokenize():
    start = int(time.time())
    
    if os.path.exists('korean_noun_result.txt'):
        os.remove('korean_noun_result.txt');
    
    if os.path.exists('korean_noun_failed.txt'):
        os.remove('korean_noun_failed.txt');

    i = open('korean_noun.txt', 'r', encoding='utf-8').read();
    rawlist = preprocess(i);
    
    from multiprocessing import Pool
    with Pool(8, initializer=multiprocessing_initializer) as pool:
        tokens = pool.starmap(process, zip(rawlist))
    
    result = ''
    failed = ''
    for i in tokens:
        if len(i) > 2: failed += ' '.join(i) + '\n';
        result += '\n'.join(i) + '\n';

    f1 = open('korean_noun_failed.txt', 'w', encoding='utf-8');
    f1.write(failed);

    f2 = open('korean_noun_result.txt', 'w', encoding='utf-8');
    f2.write(result);

    print("***tokenizing run time(sec) :", int(time.time()) - start)