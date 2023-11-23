import requests
import plotly.express as px

# #执行API调用并存储响应
# url = "https://api.github.com/search/repositories"
# url += "?q=language:python+sort:stars+stars:>10000"

# headers = {"Accept":"application/vnd.github.v3+json"}

# # 发送请求时禁用 SSL 验证
# r = requests.get(url, headers=headers,verify=False)

# print(f"Status code:{r.status_code}")

# #将响应转换为字典
# response_dict = r.json()
# #print(f"Total repositories:{response_dict['total_count']}")
# print(f"Complete results:{not response_dict['incomplete_results']}")

# #处理结果
# #print(response_dict.keys())

# #探索有关仓库的信息
# repo_dicts=response_dict['items']
# #print(f"Repositories returned:{len(repo_dicts)}")
# stars,hover_texts,repo_links=[],[],[]


# #print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     repo_name=repo_dict['name']
#     repo_url=repo_dict['html_url']
#     repo_link=f"<a href='{repo_url}'>{repo_name}</a>"
#     repo_links.append(repo_link)
#     stars.append(repo_dict['stargazers_count'])
    
#     #创建悬停文本
#     owner=repo_dict['owner']['login']
#     description=repo_dict['description']
#     hover_text=f"{owner}<br/>{description}"
#     hover_texts.append(hover_text)
# #可视化
# title="Most-Starred Python Projects on Github"
# labels={'x':'Repository','y':'Stars'}
# fig=px.bar(x=repo_links,y=stars,title=title,labels=labels,hover_name=hover_texts)
# fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
# fig.update_traces(marker_color='SteelBlue',marker_opacity=0.6)
# fig.show()


def get_github_data():
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}

    # 发送请求时禁用 SSL 验证
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def visualize_github_data(github_data):
    if not github_data:
        print("Failed to fetch GitHub data.")
        return

    repo_dicts = github_data.get('items', [])
    if not repo_dicts:
        print("No repository data found.")
        return

    stars, hover_texts, repo_links = [], [], []

    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

        # 创建悬停文本
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        hover_text = f"{owner}<br/>{description}"
        hover_texts.append(hover_text)

    # 可视化
    title = "Most-Starred Python Projects on Github"
    labels = {'x': 'Repository', 'y': 'Stars'}
    fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
    fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
    fig.show()

github_data = get_github_data()
visualize_github_data(github_data)
