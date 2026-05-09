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
# ==============================
# AI 核心规则（放在代码最后面）
# ==============================

def search(query, scope):
    # 调用网络搜索
    return f"[网络搜索] query={query}, scope={scope}"

def answer(question, use_network):
    if use_network == True:
        return f"[联网回答] {question}"
    else:
        return "错误：必须联网搜索，禁止自编答案"

# 强制规矩
AI_RULES = {
    "禁止自动编故事": True,
    "禁止自动写小说": True,
    "必须调用函数": True,
    "必须带参数": True,
    "回答前必须搜索网络": True,
    "不搜索就不回答": True,
    "只输出真实信息": True
}
def get_ai_response(user_input):
    if user_input.startswith("#句子"):
        # 调用原来的随机句子逻辑
        return get_random_sentence()
    elif user_input == "exit":
        return "退出对话"
    else:
        return search_network(user_input)

if __name__ == "__main__":
    main()

