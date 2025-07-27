
# Python 환경 및 pip 에러 해결 가이드

macOS에서 최신 Python 및 pip 설치, Homebrew 환경에서 발생하는 pip 에러의 원인과 해결법을 정리합니다.

---

## 목차
1. [Homebrew pip 에러 원인과 해결법](#homebrew-pip-에러-원인과-해결법)
2. [문제 해결 단계별 가이드](#문제-해결-단계별-가이드)
3. [추가 자료](#추가-자료)
4. [클래스 기본 생성자(new, init)와 싱글톤 예제](#클래스-기본-생성자new-init와-싱글톤-예제)

---

## 1. Homebrew pip 에러 원인과 해결법

zsh에서 아래와 같은 에러가 발생할 수 있습니다:

```text
/opt/homebrew/bin/pip: bad interpreter: /opt/homebrew/opt/python@3.10/bin/python3.10: no such file or directory
```

### 원인
- Homebrew로 설치한 pip가 삭제되었거나 경로가 변경된 Python을 참조하고 있음
- pip가 Anaconda 등 다른 환경의 Python을 참조하여 경로가 꼬임

## 2. 문제 해결 단계별 가이드

### 1) Homebrew Python 재설치
```bash
brew install python3
brew link --overwrite python3
```

### 2) pip 심볼릭 링크 재설정
```bash
which pip
which python3
# pip가 /opt/homebrew/bin/pip에 있다면 아래 명령 실행
rm /opt/homebrew/bin/pip
ln -s $(which pip3) /opt/homebrew/bin/pip
```

### 3) pip3 사용 권장
- `pip` 대신 `pip3` 사용
- `pip3 install --upgrade pip`로 pip3 최신화

### 4) 경로 문제 확인
- `which python3`와 `which pip3`로 경로를 확인하고, 둘 다 Homebrew 경로(bin)를 가리키는지 확인

### 5) Anaconda 환경과 Homebrew 환경 분리
- Anaconda와 Homebrew Python을 혼용하지 말고, 가상환경(venv, uv, conda 등)을 명확히 구분해서 사용

### 6) 정상 동작 확인
```bash
python3 --version
pip3 --version
```

---

## 3. 추가 자료
- [Homebrew와 Python 경로 문제 공식 문서](https://docs.brew.sh/Homebrew-and-Python)
- [pip 공식 설치 가이드](https://pip.pypa.io/en/stable/installation/)
- [Anaconda 환경 관리](https://docs.anaconda.com/free/anaconda/install/)

---

## 4. 클래스 기본 생성자(new, init)와 싱글톤 예제

클래스의 기본 생성자(`__new__`, `__init__`)와 싱글톤 패턴 예제는 아래 파일에서 확인할 수 있습니다.

- [python new, init, singleton 예제](./ch03_ex05.ipynb)

# mypy 도구란?
Python 코드의 타입 체크를 자동으로 수행해주는 정적 타입 검사 도구입니다.

## 예시 파일
[mypy 공식 예제](https://github.com/python/mypy/blob/master/examples/complex.py)

## 답변
mypy는 Python 코드에 타입 힌트(예: `def foo(x: int) -> str:`)를 추가하면, 코드 실행 전에 타입 오류를 미리 찾아줍니다.  
동적 언어인 Python에서 타입 안정성을 높이고, 버그를 줄이며, 대규모 프로젝트에서 유지보수를 쉽게 해줍니다.

### 주요 특징
- 타입 힌트가 있는 코드에서 타입 오류를 빠르게 탐지
- 실행 전에 타입 오류를 알려주므로 안전한 코드 작성 가능
- 대규모 프로젝트, 협업 환경에서 코드 품질 향상에 효과적

### 사용 예시
```bash
pip install mypy
mypy your_script.py
```
타입 오류가 있으면 경고 메시지로 알려줍니다.

## 추가 자료
- [mypy 공식 홈페이지](https://mypy-lang.org/)
- [mypy 문서: Getting Started](https://mypy.readthedocs.io/en/stable/getting_started.html)