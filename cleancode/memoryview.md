# 파이썬 memoryview 설명
버퍼 프로토콜(PEP 3118)을 구현한 객체(bytes-like)를 “복사 없이” 참조해 부분 읽기/쓰기, 슬라이싱, 형 변환을 제공하는 뷰 타입입니다. 바이너리 데이터를 효율적으로 다룰 때 유용합니다.

## 예시 파일
[Python 공식 문서: memoryview objects](https://docs.python.org/ko/3/library/stdtypes.html#memoryview-objects)

## 답변
- 핵심 개념
  - zero-copy: 원본 버퍼를 공유하므로 빠르고 메모리 절약.
  - 대상: bytes, bytearray, array, mmap, NumPy 배열 등 버퍼 제공 객체.
  - 읽기/쓰기: 원본이 가변(bytearray, array 등)이고 뷰가 read-write면 수정이 원본에 즉시 반영.
- 주요 속성/메서드
  - readonly, itemsize, format(PEP 3118 포맷), ndim, shape, strides, nbytes
  - cast(fmt), tobytes(), tolist(), toreadonly(), release()

예제 1) bytearray에 대한 zero-copy 수정
````python
data = bytearray(b"ABCDEF")
mv = memoryview(data)
mv[1:4] = b"xyz"   # B → x, C → y, D → z 로 치환
print(data)        # bytearray(b'AxyzEF')  ← 원본이 바로 변경
````

예제 2) bytes는 읽기 전용(쓰기 불가)
````python
b = b"hello"
mv = memoryview(b)        # mv.readonly == True
try:
    mv[0] = 72
except TypeError as e:
    print("읽기 전용:", e)
````

예제 3) 슬라이싱은 여전히 뷰(복사 없음)
````python
buf = bytearray(range(10))     # 0..9
mv = memoryview(buf)
sub = mv[2:7]                  # 2..6 뷰
sub[-1] = 99                   # 인덱스 6을 99로
print(list(buf))               # [0,1,2,3,4,5,99,7,8,9]
````

예제 4) 형 변환(cast)로 동일 버퍼를 다른 원소 타입으로 보기
````python
from array import array

a = array('H', [0x1234, 0xABCD])  # unsigned short(2바이트) 2개
mv = memoryview(a)
mv_bytes = mv.cast('B')           # 바이트 단위 뷰로 재해석
print(list(mv_bytes))             # 엔디안에 따라 바이트 나열

# 바이트 단위 수정 → 원래 16비트 값이 함께 바뀜
mv_bytes[0] = 0xFF
print(a.tolist())
````

예제 5) 연속성·차원 정보 활용(간단 점검)
````python
import array
a = array.array('b', range(6))    # 1바이트 정수 6개
mv = memoryview(a)
print(mv.ndim, mv.shape, mv.strides, mv.itemsize)  # 1 (6,) (1,) 1
print(mv.readonly)                                 # False
````

언제 쓰나
- 대용량 바이너리 처리(파일 IO, 네트워크 버퍼)에서 불필요한 복사를 피하고 성능 향상.
- 일부 구간만 뷰로 잘라 가공(슬라이싱), 포맷을 바꿔 해석(cast)할 때.
- 외부 라이브러리(NumPy, PIL 등)와 버퍼를 공유해 상호운용.

주의
- 뷰가 살아있는 동안 원본 객체가 해제되면 안 됩니다. 필요 시 mv.release()로 명시 해제.
- bytes처럼 읽기 전용 소스는 쓰기가 불가.
- 엔디안/정렬을 고려해 cast를 사용하세요.

### 추가 자료
- [PEP 3118 — Python buffer protocol](https://peps.python.org/pep-3118/)
- [버퍼 프로토콜(C API) 개요](https://docs.python.org/ko/3/c-api/buffer.html)
