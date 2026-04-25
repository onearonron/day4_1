# Flask Hello World Setup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Windows 환경에서 `venv` 기반 Flask 최소 프로젝트를 생성하고 `http://127.0.0.1:5000/`에서 `Hello, World!`를 확인한다.

**Architecture:** 빈 작업 디렉터리에 로컬 가상환경(`.venv`)을 만들고, 해당 환경에 Flask를 설치한 뒤 단일 엔트리 파일(`app.py`)로 라우트를 제공한다. 실행은 `python app.py`로 단순화하고 브라우저에서 루트 라우트 응답을 검증한다.

**Tech Stack:** Python 3, venv, pip, Flask

---

## File Structure

- Create: `.venv/` — 로컬 Python 패키지 격리 환경
- Create: `app.py` — Flask 앱/루트 라우트/개발 서버 실행 엔트리포인트
- Modify: 없음
- Test artifact: 수동 브라우저 검증 (`http://127.0.0.1:5000/`)

### Task 1: Create Python virtual environment

**Files:**
- Create: `.venv/`

- [ ] **Step 1: Check Python availability**

Run:
```bash
python --version
```
Expected: `Python 3.x.x` 출력

- [ ] **Step 2: Create virtual environment**

Run:
```bash
python -m venv .venv
```
Expected: 프로젝트 루트에 `.venv` 디렉터리 생성

- [ ] **Step 3: Verify venv activation path (PowerShell)**

Use:
```powershell
.venv\Scripts\Activate.ps1
```
Expected: 프롬프트 앞에 `(.venv)` 표시

- [ ] **Step 4: Commit**

```bash
# 이 태스크는 환경 생성만 수행하므로 커밋 생략
```

### Task 2: Install Flask in virtual environment

**Files:**
- Create: 없음
- Modify: 없음

- [ ] **Step 1: Activate virtual environment**

Use:
```powershell
.venv\Scripts\Activate.ps1
```
Expected: `(.venv)` 표시

- [ ] **Step 2: Upgrade pip (minimal maintenance step)**

Run:
```bash
python -m pip install --upgrade pip
```
Expected: pip 업그레이드 완료 메시지

- [ ] **Step 3: Install Flask**

Run:
```bash
python -m pip install flask
```
Expected: Flask 및 의존성 설치 완료 메시지

- [ ] **Step 4: Verify Flask import**

Run:
```bash
python -c "import flask; print(flask.__version__)"
```
Expected: Flask 버전 문자열 출력

- [ ] **Step 5: Commit**

```bash
# 의존성 설치만 수행(잠금 파일 없음)으로 커밋 생략
```

### Task 3: Create `app.py` with Hello World route

**Files:**
- Create: `app.py`

- [ ] **Step 1: Write application file**

Create `app.py` with:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
```

- [ ] **Step 2: Run application**

Run:
```bash
python app.py
```
Expected: Flask 개발 서버 시작 로그 및 `Running on http://127.0.0.1:5000`

- [ ] **Step 3: Verify browser response**

Open:
```text
http://127.0.0.1:5000/
```
Expected: 페이지 본문이 정확히 `Hello, World!`

- [ ] **Step 4: Stop server after verification**

Use:
```text
Ctrl+C
```
Expected: 서버 프로세스 정상 종료

- [ ] **Step 5: Commit**

```bash
git add app.py
git commit -m "feat: add minimal Flask hello world app"
```

### Task 4: Final verification checklist

**Files:**
- Verify: `.venv/`
- Verify: `app.py`

- [ ] **Step 1: Confirm venv exists**

Run:
```bash
ls -la
```
Expected: `.venv`와 `app.py`가 목록에 존재

- [ ] **Step 2: Re-run app for final confirmation**

Run:
```bash
python app.py
```
Expected: 서버 기동 성공

- [ ] **Step 3: Re-check root route**

Open:
```text
http://127.0.0.1:5000/
```
Expected: `Hello, World!`

- [ ] **Step 4: Commit**

```bash
# 검증만 수행했으므로 추가 커밋 없음
```

## Self-Review Notes

- Spec coverage: 가상환경 생성, Flask 설치, `app.py` 생성, 로컬 URL 검증까지 모두 태스크로 매핑됨.
- Placeholder scan: TBD/TODO/모호 문구 없음.
- Consistency: 실행 포트/호스트/파일명/검증 URL이 전 태스크에서 일관됨.
