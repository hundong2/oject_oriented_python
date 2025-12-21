# TimSort와 각 언어별 정렬 알고리즘 개요
TimSort는 안정적이고(Stable) 입력의 정렬된 구간을 활용하는(adaptive) 병합 기반 정렬로, 부분적으로 정렬된 데이터에서 매우 빠르게 동작합니다. 각 언어의 기본 sort가 채택한 알고리즘도 함께 정리합니다.
## 예시 파일
- CPython TimSort 구현(list.sort): https://github.com/python/cpython/blob/main/Objects/listsort.c
- CPython TimSort 설계 문서: https://github.com/python/cpython/blob/main/Objects/listsort.txt
- C++ std::sort 레퍼런스: https://en.cppreference.com/w/cpp/algorithm/sort
- .NET ArraySortHelper 소스(C#): https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Collections/Generic/ArraySortHelper.cs
- C 표준 qsort(매뉴얼): https://man7.org/linux/man-pages/man3/qsort.3.html
## 답변
TimSort 핵심
- 아이디어: 입력에서 오름/내림 “runs(연속 정렬 구간)”를 탐지해 최소 길이(minrun)까지 확장 후, 스택에 저장하고 병합합니다. 부분 정렬된 데이터에서 run 길이가 길어져 병합 비용이 줄어듭니다.
- 보조 기법: 작은 구간에는 이진 삽입 정렬, 병합 시 “갈로핑(galloping)”으로 한쪽 run이 우세할 때 블록 단위로 빠르게 복사.
- 복잡도: 최악 O(n log n), 최선 O(n)(이미 거의 정렬된 경우). 안정적(키가 같으면 기존 순서 유지).

언어별 기본 sort 알고리즘
- Python
  - list.sort(), sorted(): TimSort(안정적, 적응형). 키 함수(key), 역순(reverse) 지원. 다중 키 정렬을 안정성으로 쉽게 구현 가능.
  - 구현: CPython Objects/listsort.c, 설계 설명은 listsort.txt.
- C++
  - std::sort: 보통 Introsort(퀵 정렬 + 힙 정렬 + 소형 구간 삽입 정렬). 평균 O(n log n), 최악 O(n log n). 비안정적.
  - std::stable_sort: 병합 정렬 기반(안정적), 보통 추가 메모리 필요.
  - 표준은 알고리즘을 고정하지 않지만 libstdc++/libc++가 위 방식을 일반적으로 채택.
- C
  - qsort: 알고리즘 “미지정”(구현 자유). 많은 libc가 퀵 정렬/인트로소트/병합 정렬 변형을 사용. 일반적으로 비안정적이며 평균 O(n log n).
  - 주의: 구현에 따라 동작·안정성·성능이 달라질 수 있음(BSD 계열에 별도 mergesort가 존재하기도 함).
- C#
  - Array.Sort, List<T>.Sort: .NET은 인트로소트(퀵+힙+삽입) 기반의 비안정 정렬을 사용하고, 작은 배열 최적화가 포함됨.
  - 안정 정렬이 필요하면 LINQ의 OrderBy/ThenBy를 사용(안정적).

실무 팁
- 이미(부분) 정렬된 데이터: Python의 TimSort가 특히 유리.
- 안정성 필요: Python 기본, C++는 std::stable_sort, C#는 LINQ OrderBy.
- 최악 성능 회피: 인트로소트는 퀵정렬의 최악 O(n^2)를 힙정렬로 회피해 안전한 상한 O(n log n)을 유지.

### 추가 자료
- Tim Peters의 TimSort 설명문: https://bugs.python.org/file4451/timsort.txt
- Introsort(설명): https://en.wikipedia.org/wiki/Introsort
- Java의 TimSort(참고, 객체 배열): https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#sort-java.lang.Object:A-