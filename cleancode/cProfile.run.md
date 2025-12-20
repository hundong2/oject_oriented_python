# cProfile.run() 출력 필드 설명
cProfile.run()가 출력하는 표의 각 열이 의미하는 바와 해석 방법을 간단히 정리합니다.
## 예시 파일
[Python 공식 문서: cProfile](https://docs.python.org/ko/3/library/profile.html#module-cProfile)
## 답변
cProfile.run('addUpNumbers()') 출력 표의 열 의미:
- ncalls: 호출 횟수. 재귀가 있으면 “primitive/total” 형식으로 표시(원시 호출/총 호출).
- tottime: 해당 함수 내부에서만 소비한 시간(자식 함수 시간 제외).
- percall(왼쪽): tottime/ncalls(호출 1회당 순수 실행 시간).
- cumtime: 해당 함수 + 그가 호출한 모든 하위 함수 시간을 포함한 누적 시간.
- percall(오른쪽): cumtime/primitive_calls(원시 호출 기준 평균 누적 시간).
- filename:lineno(function): 함수의 소스 위치와 이름.

헤더/정렬:
- “n function calls in X seconds”: 총 호출 수와 전체 측정 시간(초).
- “Ordered by: …”: 정렬 기준. sort='tottime' 또는 'cumtime' 등으로 조절 가능.
  - 예: cProfile.run('addUpNumbers()', sort='cumtime')

간단 예시:
````python
import cProfile

def addUpNumbers():
    total = 0
    for i in range(1, 1_000_001):
        total += i

cProfile.run('addUpNumbers()', sort='tottime')
# 출력 열: ncalls | tottime | percall | cumtime | percall | filename:lineno(function)
````

실전 팁:
- 상세 분석/필터링은 pstats로 파일에 저장 후 다루세요:
````python
import cProfile, pstats

cProfile.run('addUpNumbers()', 'stats.out')
p = pstats.Stats('stats.out').strip_dirs().sort_stats('cumtime')
p.print_stats(20)  # 상위 20개만 출력
````

### 추가 자료
- [pstats — 프로파일 결과 분석](https://docs.python.org/ko/3/library/profile.html#module-pstats)
- [프로파일링 가이드(튜토리얼)]https://docs.python.org/ko/3/library/profile.html#instant-user-s-guide