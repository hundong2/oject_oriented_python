# 파이썬의 cls 깊이 탐구와 내부 동작 확인
cls는 클래스 메서드(@classmethod)에서 “그 메서드가 속한 클래스 객체”를 가리키는 첫 번째 인자입니다. 접근 시 디스크립터(__get__)가 발동되어 해당 클래스가 자동으로 바인딩됩니다.

## 예시 파일
- Python 공식 문서: classmethod https://docs.python.org/ko/3/library/functions.html#classmethod
- CPython 소스: classmethod/staticmethod 디스크립터 구현(Objects/funcobject.c) https://github.com/python/cpython/blob/main/Objects/funcobject.c
- 바이트코드 디스어셈블러 dis https://docs.python.org/ko/3/library/dis.html
- 디스크립터 프로토콜(고급) https://docs.python.org/ko/3/howto/descriptor.html

## 답변
핵심 개념
- @classmethod로 감싼 함수는 “디스크립터”입니다. 클래스 속성으로 접근될 때 classmethod.__get__(func, obj, type)가 호출되어 “바운드 메서드(bound method)”를 반환합니다.
- 그 바운드 메서드의 __self__는 클래스 자신이며, 호출 시 cls 인자가 자동으로 전달됩니다.
- @staticmethod는 바인딩을 하지 않아 __self__가 없고, 일반 함수처럼 동작합니다. 인스턴스 메서드는 인스턴스에 바인딩되어 __self__가 인스턴스입니다.

클래스/정적/인스턴스 메서드 바인딩 비교와 내부 속성 확인
````python
class Example:
    def regular(self):
        return ("regular", self)

    @classmethod
    def cm(cls):
        return ("classmethod", cls)

    @staticmethod
    def sm():
        return ("staticmethod", None)

# 바운드 메서드 확인
print(Example.cm)           # <bound method Example.cm of <class '__main__.Example'>>
print(type(Example.cm))     # <class 'method'>
print(Example.cm.__self__)  # <class '__main__.Example'>  ← cls로 바인딩됨
print(Example.cm.__func__)  # 실제 함수 객체

print(Example.sm)           # <function Example.sm at 0x...>  ← 바인딩 없음
print(hasattr(Example.sm, "__self__"))  # False

obj = Example()
print(obj.regular)          # <bound method Example.regular of <__main__.Example object at ...>>
print(obj.regular.__self__) # 인스턴스로 바인딩
````

디스크립터가 cls를 바인딩하는 원리(직관적 재현)
````python
class BindToClassDescriptor:
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, owner):
        # 클래스 속성으로 접근될 때 owner가 전달됨
        def bound(*args, **kwargs):
            return self.func(owner, *args, **kwargs)  # cls로 owner 주입
        return bound

class Demo:
    @BindToClassDescriptor
    def show_cls(cls):
        return cls.__name__

print(Demo.show_cls())  # 'Demo'
````

바이트코드로 호출 시퀀스 확인(dis)
````python
import dis

class E:
    @classmethod
    def cm(cls):
        return cls.__name__

    @staticmethod
    def sm():
        return "SM"

def call_cls():
    return E.cm()      # cls 자동 전달

def call_static():
    return E.sm()      # 바인딩 없이 호출

dis.dis(call_cls)
# LOAD_ATTR/LOAD_METHOD → CALL_METHOD(버전에 따라 상이)
dis.dis(call_static)
````

상속·다형성과 cls의 실전 용도(대안 생성자)
````python
class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def from_tuple(cls, t):
        # cls를 사용하면 서브클래스에서 호출해도 올바른 타입으로 반환
        return cls(*t)

class Vector3D(Vector2D):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self.z = z

v2 = Vector2D.from_tuple((1, 2))
v3 = Vector3D.from_tuple((3, 4))   # cls=Vector3D → Vector3D 인스턴스 생성
print(type(v2), type(v3))          # <class '__main__.Vector2D'> <class '__main__.Vector3D'>
````

정리
- cls는 “클래스 객체”로 바인딩된 첫 인자이며, 디스크립터(__get__) 메커니즘으로 자동 주입됩니다.
- @classmethod는 상속/다형성 친화적 대안 생성자, 팩토리, 클래스 수준 작업에 적합합니다.
- 내부 동작은 CPython의 classmethod_descr_get에서 확인할 수 있고, 호출 사이트는 dis로 살펴볼 수 있습니다.

### 추가 자료
- CPython classmethod 구현(Objects/funcobject.c, classmethod_descr_get) https://github.com/python/cpython/blob/main/Objects/funcobject.c
- 메서드 바인딩/디스크립터 이해(HowTo Descriptor) https://docs.python.org/ko/3/howto/descriptor.html
- 바이트코드 명령 목록(dis) https://docs.python.org/ko/3/library/dis.html
- datamodel: 바운드 메서드와 속성 접근 https://docs.python.org/ko/3/reference/datamodel.html#invoking-descriptors
