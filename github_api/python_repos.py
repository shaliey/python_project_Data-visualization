import requests
import os

#执行API调用并存储响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"}

# 发送请求时禁用 SSL 验证
r = requests.get(url, headers=headers,verify=False)

print(f"Status code:{r.status_code}")

#将响应转换为字典
response_dict = r.json()
print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete results:{not response_dict['incomplete_results']}")

#处理结果
#print(response_dict.keys())

#探索有关仓库的信息
repo_dicts=response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Star:repository:{repo_dict['html_url']}")
    print(f"Description:{repo_dict['description']}")
    print(f"Repository:{repo_dict['html_url']}")
#研究第一个仓库
repo_dict=repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted (repo_dict.keys()):
    print(key)
print("\nSelected information about first repository:")
print(f"Name:{repo_dict['name']}")
print(f"Owner:{repo_dict['owner']['login']}")
print(f"Repository:{repo_dict['html_url']}")
print(f"Stars:{repo_dict['stargazers_count']}")
print(f"Created:{repo_dict['created_at']}")
print(f"Updated:{repo_dict['updated_at']}")
print(f"Description:{repo_dict['description']}")