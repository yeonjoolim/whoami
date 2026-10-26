# whoami

임연주 포트폴리오. 파이썬으로 A4 한 장 HTML을 만들고, GitHub Pages가 그 파일을 그대로 서빙한다.

메인 주소는 [https://yeonjoolim.github.io/whoami/portfolio](https://yeonjoolim.github.io/whoami/portfolio) 이다. 저장소 루트는 이 주소로 보낸다.

## 고치는 곳

문장은 `src/profile.py`만 수정한다. 사진 파일은 `assets/profile.jpg`다.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python src/build.py
```

`portfolio/index.html`과 루트 `index.html`이 다시 만들어진다. 생성된 HTML은 직접 고치지 않는다.

## 인쇄

브라우저 인쇄에서 용지는 A4, 여백은 없음, 배율은 100%로 둔다. 화면의 용지가 인쇄 한 장과 같다.
