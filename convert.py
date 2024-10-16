
from kiwipiepy import Kiwi
import time, os
import re

def multiprocessing_initializer():
    global kiwi
    kiwi = Kiwi()
    kiwi.load_user_dictionary('archive/kiwi_user_dict.txt')



def process(i: str, debug=False) -> str:
    # tokens = okt.pos(i, norm=False, stem=False);
    tokens = kiwi.tokenize(i);
    if debug: print(tokens);
    
    
    # word_list = []
    # for idx, word in enumerate(tokens):
    #     oktlen = len(tokens);
    #     if word[1] == 'Noun':
    #         word_list.append(word[0]);        
    #     elif (word[1] in ['Suffix', 'Modifier'] and oktlen > 1 and idx == oktlen - 1 and tokens[idx-1][1] == 'Noun'):
    #         word_list.append(tokens[idx-1][0] + word[0]);
    #     elif (word[1] in ['Josa', 'Modifier'] and oktlen > 2 and idx != oktlen - 1 and idx != 0 and tokens[idx-1][1] == 'Noun' and tokens[idx+1][1] == 'Noun'):
    #         word_list.append(tokens[idx-1][0] + word[0] + tokens[idx+1][0]);
    

    word_list = []
    for i in tokens:
        if i.tag in ['NNG', 'NNP']:
            split = i.form.split(' ');
            for j in split:
                word_list.append(j);

    return '\n'.join(word_list);



def convert():
    start = int(time.time())
    
    if os.path.exists('korean_noun_result.txt'):
        os.remove('korean_noun_result.txt');

    # read file 
    f = open('korean_noun.txt', 'r', encoding='utf-8');

    # toString
    i = f.read();
    # split by space or hypen
    iarr = i.replace('-', ' ').replace('–', ' ').replace(':', ' ').replace('\n', ' ').split(' ');

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