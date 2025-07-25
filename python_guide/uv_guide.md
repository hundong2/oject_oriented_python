# Python UV 완전 가이드

## 1. UV란?

UV는 Rust로 작성된 **극도로 빠른** Python 패키지 및 프로젝트 매니저입니다.

### 주요 특징
- ⚡ **극도로 빠른 속도**: Rust 기반으로 기존 도구들보다 10-100배 빠름
- 📦 **완전한 PEP 지원**: PEP 517, 518, 508, 660 지원
- 🔧 **올인원 도구**: 패키지 관리, 가상환경, 프로젝트 관리 통합
- 🐍 **Python 버전 관리**: 여러 Python 버전 설치 및 관리

## 2. 설치 방법

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# pip로 설치
pip install uv

# pipx로 설치
pipx install uv

# Homebrew
brew install uv

# Pacman (Arch Linux)
pacman -S uv
```

## 3. 기본 사용법

### Python 버전 관리

```bash
# Python 버전 설치
uv python install 3.10 3.11 3.12

# 설치된 Python 버전 확인
uv python list

# 특정 버전으로 실행
uv run --python 3.12 -- python --version
```

### 가상환경 관리

```bash
# 가상환경 생성
uv venv

# 특정 Python 버전으로 가상환경 생성
uv venv --python 3.12

# 가상환경 활성화
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

### 프로젝트 초기화

```bash
# 새 프로젝트 생성
uv init

# 워크스페이스 없이 생성
uv init --no-workspace

# 특정 Python 버전으로 생성
uv init --python 3.12
```

## 4. 패키지 관리

### 의존성 추가/제거

```bash
# 패키지 추가
uv add requests fastapi

# 개발 의존성 추가
uv add --dev pytest black ruff

# 선택적 의존성 추가
uv add fastapi --extra standard

# 패키지 제거
uv remove requests

# 의존성 동기화
uv sync
```

### 잠금 파일 관리

```bash
# 잠금 파일 생성/업데이트
uv lock

# 의존성 트리 보기
uv tree
```

## 5. 실행 및 스크립트

```bash
# 프로젝트에서 명령어 실행
uv run python main.py
uv run pytest
uv run black .

# 일회성 스크립트 실행
uv run --no-project requests -- python -c "import requests; print('OK')"
```

## 6. 자주 사용하는 워크플로우

### 새 프로젝트 시작하기

```bash
# 1. 프로젝트 폴더 생성 및 이동
mkdir my-project && cd my-project

# 2. UV 프로젝트 초기화
uv init --python 3.12

# 3. 기본 의존성 추가
uv add requests fastapi

# 4. 개발 도구 추가
uv add --dev pytest black ruff mypy

# 5. 프로젝트 실행
uv run python main.py
```

### 기존 프로젝트 셋업

```bash
# 1. 저장소 클론
git clone <repository-url>
cd <project-name>

# 2. 의존성 동기화
uv sync

# 3. 프로젝트 실행
uv run python main.py
```

### 일상 개발 명령어

```bash
# 테스트 실행
uv run pytest

# 코드 포맷팅
uv run black .
uv run ruff check --fix .

# 타입 검사
uv run mypy .

# 개발 서버 실행 (FastAPI 예시)
uv run fastapi dev main.py
```

## 7. pyproject.toml 예시

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]>=0.115.0",
    "requests>=2.31.0",
    "pydantic>=2.0.0",
]

[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "black>=24.0.0",
    "ruff>=0.7.0",
    "mypy>=1.8.0",
]

[tool.uv]
dev-dependencies = [
    "jupyter>=1.0.0",
]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.black]
line-length = 88
target-version = ['py312']
```

## 8. IDE 통합 (PyCharm/VS Code)

### PyCharm 설정

1. `File` → `Settings` → `Project` → `Python Interpreter`
2. `Add Interpreter` → `Existing`
3. `.venv/bin/python` 경로 선택

### VS Code 설정

1. `Ctrl+Shift+P` → `Python: Select Interpreter`
2. `.venv/bin/python` 선택

## 9. 고급 사용법

### 스크립트 실행

```bash
# 인라인 스크립트
uv run --with requests -- python -c "import requests; print(requests.get('https://httpbin.org/json').json())"

# 스크립트 파일 실행
uv run --with pandas,matplotlib script.py
```

### 환경 변수 설정

```bash
# .env 파일 사용
echo "DEBUG=True" > .env
uv run --env-file .env python main.py
```

### 글로벌 도구 설치

```bash
# 글로벌 도구 설치
uv tool install black
uv tool install ruff
uv tool install mypy

# 설치된 도구 목록
uv tool list
```

## 10. 성능 비교

UV는 기존 도구들에 비해 현저히 빠른 성능을 보입니다:

- **pip**: 기준점
- **poetry**: ~2-3배 느림
- **uv**: **10-100배 빠름**

## 11. 마이그레이션 가이드

### Poetry에서 UV로

```bash
# 1. poetry.lock 제거
rm poetry.lock

# 2. pyproject.toml 변환 (수동)
# [tool.poetry.dependencies] → [project.dependencies]
# [tool.poetry.group.dev.dependencies] → [dependency-groups.dev]

# 3. UV로 동기화
uv sync
```

### pip + venv에서 UV로

```bash
# 1. requirements.txt를 pyproject.toml로 변환
uv init
uv add $(cat requirements.txt | grep -v "^#" | tr '\n' ' ')

# 2. 개발 의존성 추가
uv add --dev pytest black ruff
```

## 12. 팁과 트릭

### 자주 사용하는 별칭 설정

```bash
# ~/.bashrc 또는 ~/.zshrc에 추가
alias uvr="uv run"
alias uvs="uv sync"
alias uva="uv add"
alias uvad="uv add --dev"
alias uvt="uv run pytest"
alias uvf="uv run black . && uv run ruff check --fix ."
```

### 프로젝트 템플릿

```bash
# 빠른 FastAPI 프로젝트 생성
mkdir fastapi-project && cd fastapi-project
uv init --python 3.12
uv add fastapi --extra standard
uv add --dev pytest black ruff mypy
echo 'from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}' > main.py
uv run fastapi dev main.py
```

### 의존성 업데이트

```bash
# 모든 의존성 업데이트
uv lock --upgrade

# 특정 패키지 업데이트
uv add requests --upgrade
```

## 13. 문제 해결

### 일반적인 문제들

```bash
# 캐시 클리어
uv cache clean

# 가상환경 재생성
rm -rf .venv
uv sync

# 디버그 모드로 실행
uv --verbose run python main.py
```

## 14. 추가 리소스

- [공식 문서](https://docs.astral.sh/uv/)
- [GitHub 저장소](https://github.com/astral-sh/uv)
- [FastAPI 튜토리얼](https://fastapi.tiangolo.com/tutorial/)

---

UV는 Python 개발 워크플로우를 혁신적으로 개선하는 도구입니다. 빠른 속도와 직관적인 인터페이스로 개발 생산성을 크게 향상시킬 수 있습니다.