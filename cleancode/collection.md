# collections 모듈 자주 쓰는 유형 요약과 주요 타입 예제
Python의 collections 모듈은 기본 컨테이너를 확장·보완하는 유용한 자료구조를 제공합니다. 자주 쓰는 유형을 요약하고 OrderedDict, ChainMap, Counter, UserDict를 예제로 설명합니다.
## 예시 파일
[collections 모듈 공식 문서](https://docs.python.org/ko/3/library/collections.html)
## 답변
자주 쓰는 유형:
- deque: 양쪽에서 O(1)로 추가/삭제 가능한 큐
- namedtuple: 필드 이름을 가진 가벼운 튜플
- defaultdict: 기본값을 자동 생성하는 dict
- OrderedDict: 키 순서를 관리하는 dict(순서 보존 + 추가 기능)
- ChainMap: 여러 매핑을 논리적으로 체인
- Counter: 해시 가능한 객체의 빈도 카운터
- UserDict: dict의 래퍼로 사용자 정의 dict 구현에 유리

예제:

````python
# OrderedDict: 순서와 재정렬, move_to_end 등
from collections import OrderedDict

od = OrderedDict()
od['b'] = 2
od['a'] = 1
od['c'] = 3
print(list(od.items()))          # [('b', 2), ('a', 1), ('c', 3)]

od.move_to_end('b')              # 키를 끝으로 이동
print(list(od.items()))          # [('a', 1), ('c', 3), ('b', 2)]

# 주의: Python 3.7+ 일반 dict도 삽입 순서를 보존하지만,
# OrderedDict는 move_to_end, equality의 순서 고려 등 추가 기능을 제공합니다.
````

````python
# ChainMap: 여러 dict을 겹쳐서 조회/갱신
from collections import ChainMap

defaults = {'host': 'localhost', 'port': 8000}
env = {'port': 8080}
cli = {'debug': True}

cfg = ChainMap(cli, env, defaults)
print(cfg['host'])   # 'localhost' (defaults에서)
print(cfg['port'])   # 8080 (env가 defaults를 덮음)
print(cfg['debug'])  # True (cli에서)

# 업데이트는 첫 번째 맵에 반영됨
cfg['port'] = 9000
print(cli['port'])   # 9000
````

````python
# Counter: 빈도 계산, most_common, 산술 연산
from collections import Counter

cnt = Counter(['cat', 'dog', 'cat', 'rabbit', 'dog', 'cat'])
print(cnt)                     # Counter({'cat': 3, 'dog': 2, 'rabbit': 1})
print(cnt['cat'])              # 3
print(cnt.most_common(2))      # [('cat', 3), ('dog', 2)]

# 문자열도 가능
c2 = Counter("abracadabra")
print(c2['a'])                 # 5

# 카운터 간 연산
c3 = Counter(a=2, b=1) + Counter(a=1, b=3)
print(c3)                      # Counter({'a': 3, 'b': 4})
````

````python
# UserDict: dict을 래핑해 동작을 커스터마이즈
from collections import UserDict

class LowerKeyDict(UserDict):
    def __setitem__(self, key, value):
        # 키를 소문자로 강제
        super().__setitem__(str(key).lower(), value)

d = LowerKeyDict()
d['Name'] = 'Zophie'
print(d['name'])       # 'Zophie'
print(d.data)          # 실제 내부 dict에 접근 가능: {'name': 'Zophie'}
````

참고 추가 예제:
````python
# deque: 큐/스택, 회전, 양끝 추가·삭제
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
dq.rotate(1)
print(dq)   # deque([4, 0, 1, 2, 3])

# namedtuple: 가벼운 레코드 타입
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)   # 10 20

# defaultdict: 기본값 자동 생성
from collections import defaultdict
dd = defaultdict(list)
dd['tags'].append('python')
print(dd['tags'])   # ['python']
print(dd['missing'])# [] (자동으로 빈 리스트 생성)
````

### 추가 자료
- [collections — Container datatypes](https://docs.python.org/ko/3/library/collections.html)
- [Counter 레시피와 팁](https://docs.python.org/ko/3/library/collections.html#counter-objects)