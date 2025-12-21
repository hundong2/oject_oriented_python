# Big O 표기: C++/C# 코드 예시로 이해하기
알고리즘이 입력 크기 n에 따라 얼마나 빠르게 느려지는지(시간/공간 복잡도)를 상한선으로 표현합니다.

## 예시 파일
- C++ Binary Search: https://github.com/TheAlgorithms/C-Plus-Plus/blob/master/search/binary_search.cpp
- C++ Merge Sort: https://github.com/TheAlgorithms/C-Plus-Plus/blob/master/sorting/merge_sort.cpp
- C# Binary Search: https://github.com/TheAlgorithms/C-Sharp/blob/master/Searching/BinarySearch.cs
- C# Merge Sort: https://github.com/TheAlgorithms/C-Sharp/blob/master/SortAlgorithms/MergeSort.cs

## 답변
아래는 대표 복잡도(O(1), O(n), O(log n), O(n log n), O(n^2))를 C++/C# 코드로 직관적으로 보여주는 예시입니다.

- O(1): 배열 인덱스 접근은 입력 크기와 무관하게 일정 시간
- O(n): 선형 탐색은 원소 수에 비례
- O(log n): 이진 탐색은 매 단계 절반으로 줄이며 로그에 비례
- O(n log n): 정렬(quick/merge/std::sort, List<T>.Sort)은 평균적으로 n log n
- O(n^2): 중첩 루프는 모든 쌍을 비교하면 제곱에 비례

C++ 예시
````cpp
#include <vector>
#include <algorithm>
#include <optional>

// O(1) 배열 접근
int constant_time_access(const std::vector<int>& a, size_t i) {
    return a[i];
}

// O(n) 선형 탐색
std::optional<size_t> linear_search(const std::vector<int>& a, int target) {
    for (size_t i = 0; i < a.size(); ++i) {          // n번 비교
        if (a[i] == target) return i;
    }
    return std::nullopt;
}

// O(log n) 이진 탐색 (정렬된 배열 가정)
std::optional<size_t> binary_search_idx(const std::vector<int>& a, int target) {
    size_t lo = 0, hi = a.size();
    while (lo < hi) {                                // 약 log2(n) 반복
        size_t mid = (lo + hi) / 2;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    if (lo < a.size() && a[lo] == target) return lo;
    return std::nullopt;
}

// O(n log n) 정렬
void sort_nlogn(std::vector<int>& a) {
    std::sort(a.begin(), a.end());                   // 평균 O(n log n)
}

// O(n^2) 중첩 루프(모든 쌍 비교)
size_t count_pairs_less(const std::vector<int>& a) {
    size_t cnt = 0;
    for (size_t i = 0; i < a.size(); ++i) {
        for (size_t j = i + 1; j < a.size(); ++j) {  // ~ n(n-1)/2
            if (a[i] < a[j]) ++cnt;
        }
    }
    return cnt;
}
````

C# 예시
````csharp
using System;
using System.Collections.Generic;

// O(1) 배열 접근
int ConstantTimeAccess(int[] a, int i) => a[i];

// O(n) 선형 탐색
int? LinearSearch(int[] a, int target) {
    for (int i = 0; i < a.Length; i++) {             // n번 비교
        if (a[i] == target) return i;
    }
    return null;
}

// O(log n) 이진 탐색 (정렬된 배열 가정)
int? BinarySearchIdx(int[] a, int target) {
    int lo = 0, hi = a.Length - 1;
    while (lo <= hi) {                                // 약 log2(n) 반복
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return null;
}

// O(n log n) 정렬
void SortNLogN(List<int> list) {
    list.Sort();                                      // 평균 O(n log n)
}

// O(n^2) 중첩 루프
int CountPairsLess(int[] a) {
    int cnt = 0;
    for (int i = 0; i < a.Length; i++) {
        for (int j = i + 1; j < a.Length; j++) {      // ~ n(n-1)/2
            if (a[i] < a[j]) cnt++;
        }
    }
    return cnt;
}
````

실무 팁
- 빅오는 “성장률”을 보는 상한선입니다. 상수/저차항은 숨깁니다.
- 같은 빅오라도 상수 계수 차이로 실제 성능이 달라질 수 있습니다.
- 데이터가 작을 때는 단순 알고리즘이 더 빠를 수 있습니다.

# 일반적인 함수 호출의 빅오 차수 

- s[i] 값읽기 할당 : O(1)
- s.append(value) : O(1)
- s.insert(i, value) : O(n) 
- s.remove(value) : O(n)
- s.reverse() : O(n)
- s.sort() : O(nlogn)
- value in s : O(n) 
- len(s) : O(1) 

## dictionary, set, frozenset

- m[key] read, assign : O(1)
- m.add(value) : O(1)  
- value in m : O(1) 
- len(m) : O(1)

## 한눈에 분석하는 빅오

- 코드가 데이터에 전혀 접근하지 않으면 O(1)
- 루프문에서 데이터에 접근하면 O(n)
- 두 중첩된 루프문에서 데이터를 순회하면 O(n^2)
- 함수 호출은 한단계로 세지 않고 함수 내부 코드의 총 단계 수를 센다. 
- 코드가 데이터를 반복적으로 반으로나누는 분할 정복 단계로 구성되어 있다면 O(logN)
- 코드가 데이터에서 아이템당 한번씩 이루어지는 분할 정복 단계로 구성되어 ㅣ있다면 O(N log N )
- 코드가 N개의 데이터에서 가능한 모든 값의 조합을 고려한다면, O(2^N )
- 코드가 데이터에 이쓴ㄴ 모든 값의 가능한 순열 O(N!)
- 코드가 데이터를 정렬하는 작업을 수반 O(n log n )

### 추가 자료
- [Big O Cheatsheet](https://www.bigocheatsheet.com/)
- [cppreference: std::sort](https://en.cppreference.com/w/cpp/algorithm/sort)
- [Microsoft .NET: List<T>.Sort](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1.sort)
- [TheAlgorithms C++](https://github.com/TheAlgorithms/C-Plus-Plus)
- [TheAlgorithms C#](https://github.com/TheAlgorithms/C-Sharp)