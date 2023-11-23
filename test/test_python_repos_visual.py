import sys
sys.path.append('D:/python/python_project_Data visualization')
from github_api.python_repos_visual import get_github_data, visualize_github_data
import pytest

def test_get_github_data():
    github_data = get_github_data()
    assert github_data is not None

def test_visualize_github_data(monkeypatch, capsys):
    # 用于捕获对 show 方法的调用
    captured_show = []

    # 定义替代的 show 方法
    def mock_show(fig, *args, **kwargs):
        captured_show.append(fig)
        

    #使用 monkeypatch 替换 show 方法
    monkeypatch.setattr('plotly.graph_objects.Figure.show', mock_show)

    github_data = {
        'items': [
            {'name': 'Repo1', 'html_url': 'https://github.com/repo1', 'stargazers_count': 100, 'owner': {'login': 'user1'}, 'description': 'Description1'},
            {'name': 'Repo2', 'html_url': 'https://github.com/repo2', 'stargazers_count': 200, 'owner': {'login': 'user2'}, 'description': 'Description2'},
        ]
    }

    visualize_github_data(github_data)

    # 检查 show 方法是否被正确调用
    assert len(captured_show) == 1

    # 在 captured_show[0] 上检查预期的图形内容
    assert 'Most-Starred Python Projects on Github' in str(captured_show[0])
    assert 'Repo1' in str(captured_show[0])
    assert 'Repo2' in str(captured_show[0])
    assert 'user1' in str(captured_show[0])
    assert 'user2' in str(captured_show[0])
    assert 'Description1' in str(captured_show[0])
    assert 'Description2' in str(captured_show[0])