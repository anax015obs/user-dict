from convert import multiprocessing_initializer, process, tokenize
from rmdup import rmdup
from verify import verify
from archive import archive


if __name__ == "__main__":
    # title에서 고유명사, 일반명사 추출
    # tokenize(); # <- 여기 인자값을 주는 순간 
    
    # 명사의 부분집합 제거
    # rmdup(); # <- 이쪽에서 중복제거가 안됨..?

    # es가 합성할 수 없는 명사만 추출
    # es 필요
    verify();

    # 추가 명사와 병합 후 저장
    archive('archive/user_dict.txt');

