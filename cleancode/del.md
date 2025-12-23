# Python의 del 문과 내부 동작(바이트코드 관점)
del은 “이름 바인딩‧속성‧컨테이너 항목”을 제거하는 문입니다. CPython에서는 해당 삭제를 바이트코드로 실행하고, 참조 카운트를 줄여 필요 시 메모리를 회수합니다.
## 예시 파일
- The del statement: https://docs.python.org/ko/3/reference/simple_stmts.html#the-del-statement
- dis 모듈(바이트코드 확인): https://docs.python.org/ko/3/library/dis.html
- 바이트코드 명령 목록: https://docs.python.org/ko/3/library/dis.html#bytecode-instructions
- C API(PyObject_DelAttrString 등): https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttrString
## 답변
핵심 요약
- del name: 현재 스코프의 이름 바인딩을 제거합니다. 이후 name을 참조하면 NameError.
- del obj.attr: 객체의 속성을 제거합니다. 일반 객체는 __delattr__로 처리, property면 deleter가 호출됩니다.
- del container[index] / del container[key]: 항목 삭제(예: 리스트/딕셔너리). 내부적으로 __delitem__ 또는 전용 연산이 수행됩니다.
- 메모리: del 자체는 “이름/참조를 하나 제거”합니다. 해당 객체의 참조 카운트가 0이 되면 CPython이 즉시 메모리를 회수하고, 필요 시 __del__(finalizer)이 호출됩니다. 순환 참조는 GC가 추가로 처리합니다.

노트북 예시 코드와 연결
- ch17.ipynb의 del obj.someParameter는 인스턴스 딕셔너리에서 'someParameter' 키를 제거합니다. 속성이 존재하지 않으면 AttributeError.

del의 내부 동작을 바이트코드로 확인
````python
import dis

class C:
    def __init__(self):
        self.x = 10

def del_name():
    a = 42
    del a            # 로컬 이름 삭제
    return 0

def del_attr(c: C):
    del c.x          # 속성 삭제
    return 0

def del_subscr(lst):
    del lst[0]       # 구독 항목 삭제(리스트 첫 요소)
    return lst

dis.dis(del_name)
# 예시(버전에 따라 다를 수 있음):
# LOAD_CONST 42; STORE_FAST a
# DELETE_FAST a            ← 로컬 이름 삭제 바이트코드
# LOAD_CONST 0; RETURN_VALUE

dis.dis(del_attr)
# LOAD_FAST c; DELETE_ATTR x  ← 속성 삭제 바이트코드
# LOAD_CONST 0; RETURN_VALUE

dis.dis(del_subscr)
# LOAD_FAST lst; LOAD_CONST 0; DELETE_SUBSCR  ← 구독 삭제 바이트코드
# LOAD_FAST lst; RETURN_VALUE
````

property의 deleter 동작 확인
````python
class P:
    def __init__(self):
        self._v = 123

    @property
    def v(self):
        return self._v

    @v.deleter
    def v(self):
        print("deleter called")
        del self._v

p = P()
del p.v         # property의 deleter가 호출됨
# 출력: deleter called
````

참조 카운트/GC와 메모리 회수
````python
import sys

class Tr:
    def __del__(self):
        print("__del__ called")

obj = Tr()
print(sys.getrefcount(obj))  # 참조 수 관찰(주의: getrefcount가 임시 참조를 하나 추가)
a = obj
b = obj
del a; del b; del obj        # 마지막 참조 삭제 시 __del__ 호출 및 메모리 회수
````

어셈블리 관점
- CPython은 바이트코드 인터프리터입니다. del은 DELETE_FAST/DELETE_ATTR/DELETE_SUBSCR 등 바이트코드로 실행되며, C 레벨에서 딕셔너리 엔트리 제거, 참조 카운트 감소(Py_DECREF)가 수행됩니다.
- 네이티브 CPU 어셈블리에 직접 매핑되지 않고, “인터프리터 루프 → C API 호출”로 처리됩니다.

### 추가 자료
- 데이터 모델: 속성 접근/삭제(__getattr__/__delattr__): https://docs.python.org/ko/3/reference/datamodel.html#customizing-attribute-access
- 가비지 컬렉션(gc 모듈): https://docs.python.org/ko/3/library/gc.html
- 디스크립터/프로퍼티 동작: https://docs.python.org/ko/3/howto/descriptor.html
