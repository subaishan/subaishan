"""测试标记替换引擎"""

from src import (
    generate_icon_html,
    generate_skill_html,
    generate_github_stats_img,
    replace_tags,
)


def test_generate_icon_html_string():
    """测试字符串类型的图标生成"""
    result = generate_icon_html("python")
    assert "python" in result
    assert "img" in result
    assert "github.com" in result


def test_generate_icon_html_dict():
    """测试字典类型的图标生成"""
    result = generate_icon_html({"name": "vite", "url": "https://vitejs.dev/logo.svg"})
    assert "vite" in result
    assert "vitejs.dev" in result


def test_generate_skill_html():
    """测试技能列表生成"""
    result = generate_skill_html("languages")
    assert "python" in result
    assert "javascript" in result
    assert "\n" in result  # 多行


def test_generate_github_stats_img():
    """测试 GitHub 统计图生成"""
    result = generate_github_stats_img()
    assert "img" in result
    assert "github-readme-stats" in result


def test_replace_tags_skills():
    """测试标记替换（技能）"""
    content = "<!-- languages:start -->\nold content\n<!-- languages:end -->"
    result = replace_tags(content)
    assert "<!-- languages:start -->" in result
    assert "<!-- languages:end -->" in result
    assert "python" in result
    assert "old content" not in result


def test_replace_tags_github_stats():
    """测试标记替换（统计图）"""
    content = "<!-- github-stats:start -->\nold\n<!-- github-stats:end -->"
    result = replace_tags(content)
    assert "github-readme-stats" in result
    assert "old" not in result


def test_replace_tags_no_match():
    """测试没有匹配标记时内容不变"""
    content = "hello world"
    result = replace_tags(content)
    assert result == content
