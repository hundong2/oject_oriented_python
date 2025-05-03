Python `lambda` 함수 사용법
===========================

Python의 `lambda` 함수는 익명 함수(이름 없는 함수)를 정의하는 데 사용됩니다. 일반적으로 간단한 연산이나 일회성 함수 정의에 유용합니다.

함수 시그니처
--------------

.. code-block:: python

   lambda arguments: expression

- **`arguments`**: 함수에 전달할 매개변수(하나 이상 가능).
- **`expression`**: 반환할 값. 단일 표현식만 작성 가능하며, 여러 줄 코드는 사용할 수 없습니다.

특징
-----

- `lambda` 함수는 이름이 없는 익명 함수입니다.
- 간단한 연산을 수행하거나, 다른 함수의 인자로 전달할 때 유용합니다.
- 일반적인 `def` 키워드로 정의된 함수와 달리, `lambda`는 한 줄로 작성됩니다.

사용 예제
----------

1. **기본적인 `lambda` 함수 사용**

   .. code-block:: python

      # 두 숫자를 더하는 lambda 함수
      add = lambda x, y: x + y
      print(add(5, 3))  # 출력: 8

   **동작 설명**:  
   - `lambda x, y: x + y`는 두 매개변수 `x`와 `y`를 받아 그 합을 반환하는 익명 함수입니다.
   - `add` 변수에 이 함수를 할당하여 호출할 수 있습니다.

2. **리스트 정렬에서 `lambda` 사용**

   .. code-block:: python

      points = [(1, 2), (3, 1), (5, -1), (0, 0)]
      points.sort(key=lambda point: point[1])  # y 좌표 기준으로 정렬
      print(points)  # 출력: [(5, -1), (0, 0), (3, 1), (1, 2)]

   **동작 설명**:  
   - `lambda point: point[1]`는 각 튜플의 두 번째 요소(`y` 좌표)를 반환합니다.
   - `sort` 함수의 `key` 매개변수에 전달되어, 리스트가 `y` 좌표를 기준으로 정렬됩니다.

3. **`map`과 함께 `lambda` 사용**

   .. code-block:: python

      numbers = [1, 2, 3, 4, 5]
      squared = list(map(lambda x: x ** 2, numbers))
      print(squared)  # 출력: [1, 4, 9, 16, 25]

   **동작 설명**:  
   - `lambda x: x ** 2`는 각 숫자를 제곱하는 익명 함수입니다.
   - `map` 함수는 리스트의 각 요소에 이 함수를 적용하여 새로운 리스트를 생성합니다.

4. **`filter`와 함께 `lambda` 사용**

   .. code-block:: python

      even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
      print(even_numbers)  # 출력: [2, 4]

   **동작 설명**:  
   - `lambda x: x % 2 == 0`는 숫자가 짝수인지 확인하는 익명 함수입니다.
   - `filter` 함수는 리스트에서 조건을 만족하는 요소만 필터링하여 반환합니다.

5. **`reduce`와 함께 `lambda` 사용**

   .. code-block:: python

      from functools import reduce
      product = reduce(lambda x, y: x * y, numbers)
      print(product)  # 출력: 120

   **동작 설명**:  
   - `lambda x, y: x * y`는 두 숫자를 곱하는 익명 함수입니다.
   - `reduce` 함수는 리스트의 모든 요소를 순차적으로 곱하여 하나의 값을 반환합니다.

제약 사항
----------

- `lambda` 함수는 단일 표현식만 작성 가능하며, 여러 줄 코드를 사용할 수 없습니다.
- 복잡한 로직이 필요한 경우 `def` 키워드를 사용하여 일반적인 함수를 정의하는 것이 좋습니다.

장점
-----

- 간결하고 직관적인 코드 작성 가능.
- 일회성 함수 정의에 적합.

단점
-----

- 복잡한 로직에는 적합하지 않음.
- 디버깅이 어려울 수 있음.

추가 참고
----------

- `lambda` 함수는 다른 고차 함수(`map`, `filter`, `reduce`)와 함께 자주 사용됩니다.
- 간단한 연산이나 데이터 변환 작업에 유용합니다.