#!/usr/bin/env python3
"""profile.py를 읽어 GitHub Pages용 정적 HTML을 만든다."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(__file__).resolve().parent


def load_profile() -> dict:
    spec = importlib.util.spec_from_file_location("profile", SRC / "profile.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("src/profile.py를 읽지 못했습니다.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.PROFILE


def main() -> None:
    env = Environment(
        loader=FileSystemLoader(SRC / "templates"),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    profile = load_profile()

    portfolio = ROOT / "portfolio" / "index.html"
    portfolio.parent.mkdir(parents=True, exist_ok=True)
    portfolio.write_text(
        env.get_template("portfolio.html.j2").render(**profile),
        encoding="utf-8",
    )

    index = ROOT / "index.html"
    index.write_text(
        env.get_template("index.html.j2").render(site_url=profile["site_url"]),
        encoding="utf-8",
    )
    print(f"wrote {portfolio.relative_to(ROOT)}")
    print(f"wrote {index.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
