#!/usr/bin/env python3
"""
GitHub Profile README 生成器
读取 README.md 和 README.zh.md，替换标记为生成的 HTML 内容
"""

from pathlib import Path

from src import replace_tags

BASE_DIR = Path(__file__).parent


def generate_readme(file_path: Path) -> None:
    """生成单个 README 文件"""
    content = file_path.read_text(encoding="utf-8")
    new_content = replace_tags(content)

    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"✅ 已更新: {file_path.name}")
    else:
        print(f"⏭️  无需更新: {file_path.name}")


def main() -> None:
    readme_en = BASE_DIR / "README.md"
    readme_zh = BASE_DIR / "README.zh.md"

    if readme_en.exists():
        generate_readme(readme_en)
    else:
        print("⚠️  README.md 不存在，请先创建")

    if readme_zh.exists():
        generate_readme(readme_zh)
    else:
        print("⚠️  README.zh.md 不存在，请先创建")


if __name__ == "__main__":
    main()
