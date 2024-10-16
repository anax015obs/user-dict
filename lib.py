import os

def archive(i: str):
    if os.path.exists(i):
        os.remove(i);

    addi = open('archive/additional.txt', 'r', encoding='utf-8');
    addistr = addi.read();  

    result = open('korean_noun_result.txt', 'r', encoding='utf-8');
    resultstr = result.read();
    
    o = open(i, 'w', encoding='utf-8');
    o.write(resultstr + '\n' + addistr);