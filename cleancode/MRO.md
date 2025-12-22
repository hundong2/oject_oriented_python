# MRO(C3) 알고리즘과 메서드 결정 순서
Python의 MRO(Method Resolution Order)는 C3 선형화를 사용해 다중 상속에서 속성/메서드 탐색 순서를 결정합니다. 국소 우선순위 보장, 단조성, 일관성을 만족합니다.
## 예시 파일
- The Python 2.3 Method Resolution Order (C3) 설명: https://www.python.org/download/releases/2.3/mro/
- 데이터 모델(속성 조회와 MRO): https://docs.python.org/ko/3/reference/datamodel.html#customizing-class-creation
- super() 함수: https://docs.python.org/ko/3/library/functions.html#super
- inspect.getmro: https://docs.python.org/ko/3/library/inspect.html#inspect.getmro
- CPython 구현(typeobject.c, MRO 관련): https://github.com/python/cpython/blob/main/Objects/typeobject.c
## 답변
핵심 개념
- 목적: 다중 상속에서 “어떤 클래스의 메서드를 먼저 볼지”를 결정하는 선형 순서(MRO)를 만든다.
- C3 선형화 성질:
  - Local precedence order: 클래스 정의에서 왼쪽 부모가 오른쪽 부모보다 우선.
  - Monotonicity: 서브클래스의 MRO는 슈퍼클래스 MRO의 상대적 순서를 깨지 않는다.
  - Consistent linearization: 모든 부모 리스트와 부모들의 MRO를 하나로 “merge”하여 충돌이 없도록 만든다. 불가능하면 TypeError.

C3 선형화 요약 공식
- L(C) = [C] + merge(L(P1), L(P2), …, [P1, P2, …])
  - L(X): 클래스 X의 MRO
  - merge: 각 리스트의 “헤드 후보”들 중 어떤 리스트의 “꼬리”에도 나타나지 않는 헤드를 선택해 결과에 추가하고, 선택된 헤드를 모든 리스트에서 제거하며 반복. 후보가 없으면 일관된 MRO가 불가능해 오류.

예제 1) 다이아몬드 상속에서의 MRO와 호출
````python
class A:
    def who(self): print("A")
class B(A):
    def who(self):
        print("B"); super().who()
class C(A):
    def who(self):
        print("C"); super().who()
class D(B, C):
    pass

print(D.mro())        # [D, B, C, A, object]
D().who()
# 출력:
# B
# C
# A
````
- C3 계산 스케치: L(A)=[A, object], L(B)=[B, A, object], L(C)=[C, A, object]
  - L(D) = [D] + merge([B, A, object], [C, A, object], [B, C])
  - 헤드 B(꼬리들에 B 없음) → [D, B] …
  - 다음 C → [D, B, C] …
  - 다음 A → [D, B, C, A] …
  - 마지막 object → [D, B, C, A, object]

예제 2) 일관성 없는 상속은 오류
````python
class X: pass
class Y: pass
class A(X, Y): pass     # A는 X를 Y보다 우선
class B(Y, X): pass     # B는 Y를 X보다 우선(역순)

try:
    class Z(A, B):      # 모순: Z는 A와 B의 우선순위를 동시에 만족 불가
        pass
except TypeError as e:
    print("MRO error:", e)
# MRO error: Cannot create a consistent method resolution order (MRO) for bases A, B
````

예제 3) MRO 확인과 메서드 결정 순서 추적
````python
import inspect

class A:  pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print("__mro__:", D.__mro__)
print("inspect.getmro:", inspect.getmro(D))

# 속성 탐색 시퀀스(메서드도 동일 규칙)
for cls in D.__mro__:
    print("lookup in:", cls.__name__)
````

예제 4) super()는 “현재 MRO에서의 다음 클래스”를 따른다
````python
class Mixin1:
    def f(self):
        print("Mixin1"); super().f()

class Mixin2:
    def f(self):
        print("Mixin2"); super().f()

class Base:
    def f(self):
        print("Base")

class Foo(Mixin1, Mixin2, Base):
    pass

print(Foo.mro())  # [Foo, Mixin1, Mixin2, Base, object]
Foo().f()
# 출력:
# Mixin1
# Mixin2
# Base
````
- 각 f는 super().f()로 “MRO의 다음”을 호출. 다중 상속에서도 안전하게 협력적(cooperative) 호출이 된다.

포인트
- 왼쪽 부모가 먼저: class D(B, C)면 B가 C보다 먼저 탐색된다.
- super()는 “부모 이름”이 아니라 “MRO에서 다음”을 호출한다.
- 모순되는 우선순위가 있으면 Python이 클래스를 만들 때 즉시 TypeError로 막는다.

### 추가 자료
- MRO 직관적 설명(블로그, Michele Simionato): https://www.python.org/download/releases/2.3/mro/
- super() 가이드: https://realpython.com/python-super/
- Fluent Python 2/e(챕터: 상속과 MRO) 발췌: https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/ (도서)