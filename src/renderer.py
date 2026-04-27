"""
标记替换引擎
负责将 README 中的标记替换为生成的 HTML 内容
"""

import re
from typing import Any

# ==========================================
# 你的数据配置（修改这里）
# ==========================================

GITHUB_USERNAME = "subaishan"

# 技能图标列表
# 字符串 = 使用 GitHub 官方图标库
# 字典 = 使用自定义图片链接
SKILLS: dict[str, list[Any]] = {
    "languages": [
        "python",
        "c",
        "html",
        "css",
    ],
    "tools": [
        ""
        "qt",
        "django",
        "flask",
        "git",
        "docker",
        "visual-studio-code",
        "linux",
    ],
    "interested": [
        "llm",
        "vue",
    ],
}


# ==========================================
# 图标生成
# ==========================================

def generate_icon_html(icon: Any) -> str:
    """生成单个技能图标 HTML"""
    if isinstance(icon, str):
        url = f"https://raw.githubusercontent.com/github/explore/main/topics/{icon}/{icon}.png"
        alt = icon
    else:
        url = icon["url"]
        alt = icon["name"]
    return f'<code><img height="20" src="{url}" alt="{alt}" /></code>'


def generate_skill_html(skill_key: str) -> str:
    """生成某个分类的技能图标列表 HTML"""
    icons = SKILLS.get(skill_key, [])
    items = [generate_icon_html(icon) for icon in icons]
    return "\n".join(items)


# ==========================================
# GitHub 统计图
# ==========================================

def generate_github_stats_img() -> str:
    """生成 GitHub 统计图 HTML"""
    params = {
        "username": GITHUB_USERNAME,
        "show_icons": "true",
        "icon_color": "0078e7",
        "title_color": "0078e7",
        "include_all_commits": "true",
    }
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"https://github-readme-stats.vercel.app/api?{query}"
    print(f"Generated GitHub stats URL: {url}")
    return f'<img align="right" width="450" src="{url}" />'


# ==========================================
# 标记替换
# ==========================================

# 定义所有生成器，包括 github-stats 和 skills
GENERATORS: dict[str, Any] = {
    "github-stats": lambda: generate_github_stats_img(),
}

print(f"Initial generators: {list(GENERATORS.keys())}")

# 动态添加 skills 相关的标记
for key in SKILLS:
    GENERATORS[key] = lambda k=key: generate_skill_html(k)


def replace_tags(content: str) -> str:
    """
    替换内容中的所有标记
    标记格式: <!-- name:start --> ... <!-- name:end -->
    """
    def replacer(match: re.Match) -> str:
        print(f"Found tag: {match.group(1)}")
        print(f"Generators available: {list(GENERATORS.keys())}")
        tag_name = match.group(1)
        if tag_name in GENERATORS:
            return f"<!-- {tag_name}:start -->\n{GENERATORS[tag_name]()}\n<!-- {tag_name}:end -->"
        return match.group(0)

    pattern = r"<!--\s*([\w-]+):start\s*-->.*?<!--\s*\1:end\s*-->"
    return re.sub(pattern, replacer, content, flags=re.DOTALL)
