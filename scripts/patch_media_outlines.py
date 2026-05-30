#!/usr/bin/env python3
"""Post-process generated media/moduleN/outline.yaml for learn_uart_spi_i2c.

Fixes:
  - Self-check expect strings (modules 2–8 use module-specific messages)
  - Removes invalid --scaffold slides (this course has no scaffold scripts)
  - Syncs manifest expect_stdout_contains after outline edits
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

COURSE = Path(__file__).resolve().parent.parent
MAX_BULLET_CHARS = 140


def _truncate_bullet(text: str, limit: int = MAX_BULLET_CHARS) -> str:
    """Shorten bullet text so slides do not overflow (verify_media limit)."""
    s = str(text).strip()
    if len(s) <= limit:
        return s
    cut = limit - 3
    chunk = s[:cut]
    if " " in chunk:
        chunk = chunk.rsplit(" ", 1)[0]
    return chunk.rstrip(".,;:") + "..."


def _truncate_slide_bullets(slide: dict[str, Any]) -> bool:
    """Return True if any bullet was shortened."""
    changed = False
    bullets = slide.get("bullets")
    if isinstance(bullets, list):
        new_bullets: list[Any] = []
        for b in bullets:
            if isinstance(b, str):
                t = _truncate_bullet(b)
                new_bullets.append(t)
                if t != b:
                    changed = True
            else:
                new_bullets.append(b)
        if changed:
            slide["bullets"] = new_bullets
    left = slide.get("left")
    if isinstance(left, list):
        new_left: list[Any] = []
        for item in left:
            if isinstance(item, str):
                t = _truncate_bullet(item)
                new_left.append(t)
                if t != item:
                    changed = True
            else:
                new_left.append(item)
        if changed:
            slide["left"] = new_left
    return changed


def _example_basename(folder: str) -> str:
    """Return short example name (e.g. spec_to_rtl) from examples/spec_to_rtl."""
    return folder.rstrip("/").split("/")[-1]


def _normalize_demo_base(name: str) -> str:
    """Strip .png and optional exNN_ prefix to get example basename."""
    base = name.replace(".png", "").split("/")[-1]
    m = re.match(r"^ex\d+_(.+)$", base)
    if m:
        base = m.group(1)
    return _example_basename(base)


def patch_outline(data: dict[str, Any], module: int) -> bool:
    """Return True if any change was made."""
    changed = False
    slides: list[dict[str, Any]] = data.get("slides") or []

    new_slides: list[dict[str, Any]] = []
    ex_num = 0
    for slide in slides:
        if (
            slide.get("type") == "code"
            and slide.get("title") == "Exercise scaffold"
            and "--scaffold" in str(slide.get("code", ""))
        ):
            changed = True
            continue
        if slide.get("type") == "demo" and slide.get("title") == f"Module {module} self-check":
            if module == 1:
                expect = "All required checks passed"
            else:
                expect = f"All required checks for Module {module} passed"
            if slide.get("expect_stdout_contains") != expect:
                slide["expect_stdout_contains"] = expect
                changed = True
        if slide.get("type") == "demo" and slide.get("title", "").startswith("Demo:"):
            ex_num += 1
            shot = str(slide.get("screenshot", ""))
            base = _normalize_demo_base(shot)
            new_shot = f"assets/screenshots/ex{ex_num:02d}_{base}.png"
            if slide.get("screenshot") != new_shot:
                slide["screenshot"] = new_shot
                changed = True
            notes = str(slide.get("notes", ""))
            if "examples/examples/" in notes:
                slide["notes"] = notes.replace("examples/examples/", "examples/")
                changed = True
        if slide.get("type") == "bullets" and str(slide.get("notes", "")).startswith("module"):
            notes = str(slide.get("notes", ""))
            if "examples/examples/" in notes:
                slide["notes"] = notes.replace("examples/examples/", "examples/")
                changed = True
        if slide.get("type") == "bullets" and _truncate_slide_bullets(slide):
            changed = True
        if slide.get("type") == "two_column" and _truncate_slide_bullets(slide):
            changed = True
        new_slides.append(slide)

    if len(new_slides) != len(slides):
        data["slides"] = new_slides
        slides = new_slides
    return changed


def rebuild_manifest_from_outline(
    manifest: dict[str, Any],
    slides: list[dict[str, Any]],
    module: int,
    course_name: str,
) -> bool:
    """Rebuild screenshot assets from outline demo slides; keep diagrams."""
    old_assets = manifest.get("assets") or []
    diagrams = [a for a in old_assets if a.get("type") == "diagram"]
    new_assets: list[dict[str, Any]] = list(diagrams)

    slide_num = 0
    for slide in slides:
        slide_num += 1
        if slide.get("type") != "demo":
            continue
        shot = slide.get("screenshot")
        if not shot:
            continue
        aid = Path(str(shot)).stem
        entry: dict[str, Any] = {
            "id": aid,
            "type": "screenshot",
            "file": str(shot),
            "capture_command": str(slide.get("command", "")),
            "cwd": ".",
            "slides": [slide_num],
        }
        if slide.get("expect_stdout_contains"):
            entry["expect_stdout_contains"] = slide["expect_stdout_contains"]
        new_assets.append(entry)

    if new_assets == old_assets:
        return False
    manifest["module"] = module
    manifest["course"] = course_name
    manifest["assets"] = new_assets
    return True


def main() -> int:
    modules = sorted(
        int(m.group(1))
        for p in (COURSE / "docs").glob("MODULE*.md")
        if (m := re.match(r"MODULE(\d+)\.md$", p.name))
    )
    if not modules:
        print("No docs/MODULE*.md found", file=sys.stderr)
        return 1

    for mod in modules:
        media = COURSE / "media" / f"module{mod}"
        outline_path = media / "outline.yaml"
        manifest_path = media / "assets" / "manifest.yaml"
        if not outline_path.is_file():
            print(f"SKIP module {mod}: no outline.yaml")
            continue

        outline = yaml.safe_load(outline_path.read_text(encoding="utf-8")) or {}
        changed = patch_outline(outline, mod)
        course_name = str(outline.get("course", "learn_uart_spi_i2c"))

        if manifest_path.is_file():
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
            if rebuild_manifest_from_outline(
                manifest, outline.get("slides") or [], mod, course_name
            ):
                changed = True
            if changed:
                manifest_path.write_text(
                    yaml.dump(manifest, sort_keys=False, allow_unicode=True),
                    encoding="utf-8",
                )

        if changed:
            outline_path.write_text(
                yaml.dump(outline, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            print(f"Patched module {mod}")
        else:
            print(f"OK module {mod} (no changes)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
