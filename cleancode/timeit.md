# timeit.timeit 인수 설명
timeit.timeit()의 각 인수가 무엇을 의미하고 어떻게 실행되는지, 예제 코드 기준으로 설명합니다.
## 예시 파일
[Python 공식 문서: timeit](https://docs.python.org/ko/3/library/timeit.html)
## 답변
예제 코드: timeit.timeit('random.randint(1, 100)', 'import random', number=1000000)

- stmt(첫 번째 인수): 실행할 코드 조각입니다. 여기서는 'random.randint(1, 100)'을 1,000,000번 실행합니다. 문자열로 전달하면 독립된 작은 스코프에서 평가됩니다.
- setup(두 번째 인수): 실행 전에 한 번만 준비용으로 실행되는 코드입니다. 문자열 'import random'을 통해 stmt에서 사용할 random 심볼을 준비합니다. 문자열로 stmt를 쓰고 외부 이름을 참조할 때 필수입니다.
- number(키워드 인수): stmt를 반복 실행할 횟수입니다. 여기서는 1,000,000번 반복합니다. 반환값은 총 소요 시간(초)이며, 평균 시간은 total / number로 계산합니다.

추가 인수(상황에 따라 유용):
- globals: 문자열 stmt/setup이 외부 변수를 참조해야 할 때 주입할 네임스페이스 딕셔너리입니다.
  - 예: timeit.timeit('random.randint(1, 100)', number=1_000_000, globals={'random': random})
- stmt에 callable 전달: 문자열 대신 인자 없는 호출 가능 객체를 줄 수 있어 빠르고 안전합니다.
  - 예:
    ````python
    import random, timeit
    timeit.timeit(lambda: random.randint(1, 100), number=1_000_000)
    ````

동작 요약:
- setup을 먼저 한 번 실행 → stmt를 number만큼 반복 실행 → 총 경과 시간을 float(초)로 반환.
- 문자열로 전달하면 독립 스코프에서 실행되므로 필요한 모듈/변수를 setup이나 globals로 제공해야 합니다.

팁:
- 측정 값을 평균으로 보고 싶으면 avg = timeit.timeit(...)/number.
- 큰 number로 오래 걸리면 repeat를 사용해 여러 번 측정 후 최소/중간값을 참고하세요.

### 추가 자료
- [timeit.repeat 사용법](https://docs.python.org/ko/3/library/timeit.html#timeit.Timer.repeat)
- [성능 측정 모범 사례](https://docs.python.org/ko/3/library/timeit.html#examples)
