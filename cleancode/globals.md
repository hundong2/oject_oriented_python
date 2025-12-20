# globals() 함수 설명
현재 모듈(파일)의 전역 심볼 테이블을 나타내는 딕셔너리를 반환합니다. 반환된 딕셔너리를 통해 전역 변수/함수/클래스를 조회하거나 동적으로 바인딩할 수 있습니다.
## 예시 파일
[Python 공식 문서: globals](https://docs.python.org/ko/3/library/functions.html#globals)
## 답변
- 반환값: 현재 모듈의 전역 네임스페이스 딕셔너리(일반적으로 해당 모듈의 __dict__와 동일 객체).
- 용도:
  - 전역 이름 조회/설정(globals()['name']).
  - eval/exec에 전역 네임스페이스 주입.
  - timeit에서 문자열 stmt가 참조할 심볼을 제공(globals=...).
- 함수 내부에서도 globals()는 항상 “모듈의 전역 딕셔너리”를 돌려줍니다. 특정 전역 이름을 재바인딩하려면 global 선언 또는 globals()['name'] = value를 사용합니다.
- Jupyter 노트북에서는 __name__, __builtins__, In/Out 등 노트북 환경의 전역 심볼도 포함됩니다.

예제:
````python
# 기본 조회/설정
x = 10
print(globals()['x'])   # 10

globals()['y'] = 42     # 전역에 y 추가
print(y)                # 42

# 함수 내부에서 전역 재바인딩
def set_answer():
    globals()['answer'] = 123  # global 선언 없이도 가능
set_answer()
print(answer)           # 123

# eval/exec와 함께 사용
code = "result = a + b"
a, b = 5, 7
exec(code, globals())
print(result)           # 12

# timeit에서 globals 전달
import timeit, random
print(timeit.timeit("random.randint(1, 100)", number=1_000_000, globals=globals()))
````

주의:
- 과도한 동적 바인딩(globals 변경)은 가독성과 유지보수를 해칩니다. 가능하면 명시적 import/변수 전달을 선호하세요.
- locals()는 현재 스코프의 로컬 딕셔너리를 반환하며, 함수 로컬에서 변경이 즉시 반영되지 않을 수 있습니다.

### 추가 자료
- [locals() 문서](https://docs.python.org/ko/3/library/functions.html#locals)
- [timeit 모듈](https://docs.python.org/ko/3/library/timeit.html)
- [eval/exec 사용법](https://docs.python.org/ko/3/library/functions.html#eval)
