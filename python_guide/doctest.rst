Doctest 사용법
====================

Python의 doctest 모듈은 소스 코드의 docstring에 포함된 예제 코드가 실제로 동작하는지 테스트할 수 있게 해줍니다. 아래는 doctest의 기본 사용법과 다양한 예시를 설명합니다.

1. doctest란?
--------------------
doctest는 Python 표준 라이브러리로, 함수나 클래스의 docstring에 작성된 예제 코드(>>>로 시작하는 코드)를 실제로 실행하여 결과가 일치하는지 확인합니다.

2. 기본 사용법
--------------------
예를 들어, 아래와 같이 함수의 docstring에 예제를 작성할 수 있습니다.

.. code-block:: python

    def add(a, b):
        """
        두 수를 더합니다.
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        """
        return a + b

이제 doctest로 테스트를 실행할 수 있습니다.

.. code-block:: bash

    python -m doctest your_module.py

3. 다양한 예시
--------------------

**예제 1: 리스트 뒤집기 함수**

.. code-block:: python

    def reverse_list(lst):
        """
        리스트를 뒤집어서 반환합니다.
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list([])
        []
        """
        return lst[::-1]

**예제 2: 문자열 대문자 변환**

.. code-block:: python

    def to_upper(s):
        """
        문자열을 대문자로 변환합니다.
        >>> to_upper('hello')
        'HELLO'
        >>> to_upper('Python')
        'PYTHON'
        """
        return s.upper()

**예제 3: 예외 발생 테스트**

.. code-block:: python

    def divide(a, b):
        """
        두 수를 나눕니다.
        >>> divide(4, 2)
        2.0
        >>> divide(1, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ZeroDivisionError: division by zero
        """
        return a / b

4. 모듈 전체 테스트하기
--------------------
파일 맨 아래에 아래 코드를 추가하면, 해당 파일을 직접 실행할 때 doctest가 자동으로 동작합니다.

.. code-block:: python

    if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)

5. 여러 함수의 테스트 모음
--------------------
여러 함수의 테스트를 한 번에 모아서 실행할 수도 있습니다.

.. code-block:: python

    __test__ = {
        'add_test': """
        >>> add(1, 2)
        3
        """,
        'reverse_test': """
        >>> reverse_list([1, 2])
        [2, 1]
        """
    }

6. doctest 옵션
--------------------
- `+ELLIPSIS`: 일부 결과만 비교할 때 사용 (중간 생략 ...)
- `+IGNORE_EXCEPTION_DETAIL`: 예외 메시지의 상세 내용 무시
- `+NORMALIZE_WHITESPACE`: 공백 무시

예시:

.. code-block:: python

    def foo():
        """
        >>> foo()  # doctest: +ELLIPSIS
        'result ...'
        """
        return 'result with details'

7. 실전 예시: 카드 팩토리 함수
--------------------
아래는 ch02_ex3.py에서 사용된 카드 팩토리 함수의 doctest 예시입니다.

.. code-block:: python

    def card(rank, suit):
        """
        >>> deck = [card(rank, suit) for rank in range(1, 14) for suit in (Suit.Club, Suit.Diamond, Suit.Heart, Suit.Spade)]
        >>> len(deck)
        52
        >>> sorted(set(c.suit for c in deck))
        [<Suit.Spade: '♠'>, <Suit.Club: '♣'>, <Suit.Heart: '♥'>, <Suit.Diamond: '♦'>]
        >>> sorted(set(c.rank for c in deck))
        ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'J', 'K', 'Q']
        """
        # ...함수 구현...

8. 참고
--------------------
- 공식 문서: https://docs.python.org/ko/3/library/doctest.html
- doctest는 간단한 단위 테스트에 매우 유용하며, 예제와 테스트를 동시에 관리할 수 있습니다.

