import requests
# 康洵硕的 AI 人格 - 真正联网版import requests
name="康洵硕"
def main():
    # 自我介绍
    print("=" * 50)
    print("我是康洵硕的 AI 人格，很高兴为你服务！")
    print("我可以联网查询信息，输入 exit 退出对话")
    print("=" * 50)
    
    while True:
        user_input = input("你：")
        if user_input.strip().lower() == "exit":
            print("再见！")
            break
        
        # 真正联网请求（调用免费 API 处理问题）
        try:
            response = requests.get(
                "https://api.xygeng.cn/one",
                params={"msg": user_input},
                timeout=10
            )
            data = response.json()
            if data.get("code") == 200:
                print(f"AI：{data['data']}")
            else:
                print("AI：我暂时无法回答这个问题")
        except Exception as e:
            print(f"AI：(离线) 我现在连不上网，只能复读：{user_input}")
# ======================
# 康洵硕的 AI 人格 - 修复版
# 规则：必须联网搜索，禁止自动发句子，必须调用函数
# ======================

import requests

# ----------------------
# 1. 核心函数与参数
# ----------------------
def search_network(query, scope="全网", limit=10):
    """
    联网搜索函数
    参数:
        query: 搜索关键词
        scope: 搜索范围 (全网/百科/新闻/图片)
        limit: 返回结果数量
    """
    print(f"[调用函数] search_network")
    print(f"[参数] query={query}, scope={scope}, limit={limit}")
    
    # 这里是实际联网搜索的示例（你可以换成自己的搜索接口）
    try:
        # 示例：用 DuckDuckGo 搜索（不需要 API Key）
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        if data.get("Abstract"):
            return f"[搜索结果] {data['Abstract']}"
        else:
            return f"[搜索结果] 未找到关于「{query}」的详细信息"
    except Exception as e:
        return f"[搜索失败] 无法连接网络：{str(e)}"

# ----------------------
# 2. 强制规则：禁止乱发句子
# --------

if __name__ == "__main__":
    main()


 


