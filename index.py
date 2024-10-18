import tokenizer
import decompounder
import remover
import lib

if __name__ == "__main__":
    # title에서 고유명사, 일반명사 추출
    tokenizer.tokenize(); # <- 여기 인자값을 주는 순간 
    
    # 합성명사를 가중치에 따라 어근분해
    decompounder.decompound(); # <- 이쪽에서 중복제거가 안됨..?


    # res = decompounder.process({'테스트로겐': 1, '테스티스': 1}, {'트로': 3}, {'테스트': 1}, {}, {'테스트': 1});
    # print(res);
    # es가 합성할 수 없는 명사만 추출
    # es 필요
    # remover.removeMergable();

    # 추가 명사와 병합 후 저장
    # lib.archive('archive/user_dict.txt');


