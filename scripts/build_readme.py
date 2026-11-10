"""profile.yml → README.md

사용법: python scripts/build_readme.py
의존성: PyYAML
"""
from pathlib import Path
from urllib.parse import quote

import yaml

ROOT = Path(__file__).resolve().parent.parent
ACCENT = "2c5364"


def badge(label: str, value: str = "", color: str = ACCENT, link: str | None = None) -> str:
    def esc(s: str) -> str:
        return quote(s.replace("-", "--").replace("_", "__").replace(" ", "_"), safe="")

    text = f"{esc(label)}-{esc(value)}" if value else esc(label)
    img = f'<img src="https://img.shields.io/badge/{text}-{color}?style=flat-square" alt="{label}"/>'
    return f'<a href="{link}">{img}</a>' if link else img


def repo_link(name: str, repo: str | None) -> str:
    return f"[{name}](https://github.com/{repo})" if repo else name


def tags(items: list[str]) -> str:
    return " ".join(f"`{t}`" for t in items)


def build(p: dict) -> str:
    out: list[str] = []
    add = out.append

    add("<!-- 이 파일은 scripts/build_readme.py가 profile.yml로 자동 생성합니다. 직접 수정하지 마세요. -->\n")

    # Header
    add('<div align="center">\n')
    add(f"# {p['name']} · {p['name_en']}\n")
    add(f"**{p['headline']}**  \n{p['subline']}\n")
    add(" ".join(badge(b["label"], b.get("value", ""), b.get("color", ACCENT), b.get("link")) for b in p.get("badges", [])))
    add("\n</div>\n")

    # About
    add("## About\n")
    add(p["intro"].strip() + "\n")
    for line in p.get("now", []):
        add(f"- {line}")
    add("")

    # Stack
    add("## Tech Stack\n")
    add("| | |\n|:--|:--|")
    for row in p["stack"]:
        icons = ",".join(row["icons"])
        add(f"| **{row['group']}** | <img src=\"https://skillicons.dev/icons?i={icons}\" height=\"36\"/> |")
    add("")

    # Featured
    f = p["featured"]
    add("## Featured\n")
    add(f"### {repo_link(f['title'], f.get('repo'))}\n")
    add(f"<sub>{f['meta']}</sub>\n")
    add(f["summary"].strip() + "\n")
    add("| 맡은 일 | 내용 |\n|:--|:--|")
    for c in f["contributions"]:
        prs = ""
        if c.get("prs") and f.get("repo"):
            prs = " " + ", ".join(f"[#{n}](https://github.com/{f['repo']}/pull/{n})" for n in c["prs"])
        add(f"| {c['area']} | {c['detail']}{prs} |")
    add("\n" + tags(f["stack"]) + "\n")

    # Other projects
    add("## Projects\n")
    add("| 프로젝트 | 내용 | 역할 | 기술 |\n|:--|:--|:--|:--|")
    for pr in p["projects"]:
        name = f"**{repo_link(pr['name'], pr.get('repo'))}**<br><sub>{pr['meta']}</sub>"
        add(f"| {name} | {pr['summary']} | {pr['role']} | {tags(pr['stack'])} |")
    add("")

    # Building
    b = p["building"]
    ms = b["milestones"]
    done = sum(1 for m in ms if m["done"])
    pct = round(done / len(ms) * 100)
    add(f"## Now Building — {b['name']}\n")
    add(b["summary"].strip() + "\n")
    add(badge("progress", f"{done}/{len(ms)} ({pct}%)") + "\n")
    for i, m in enumerate(ms):
        add(f"- [{'x' if m['done'] else ' '}] {i}. {m['step']}")
    add("")

    # Education & certs
    add("## Education & Certifications\n")
    for e in p["education"]:
        add(f"- {e}")
    for c in p.get("certifications", []):
        add(f"- {c['name']} ({c['code']})")
    add("")

    return "\n".join(out)


if __name__ == "__main__":
    data = yaml.safe_load((ROOT / "profile.yml").read_text(encoding="utf-8"))
    (ROOT / "README.md").write_text(build(data), encoding="utf-8")
    print("README.md updated")
