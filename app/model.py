import httpx

TOGETHER_API_KEY = "5f50c3fe9ca2042e98baa2064ef8c8b8831c5df28261ef62862cfa9f6660963e"
TOGETHER_URL = "https://api.together.xyz/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

async def analyze_with_ai(sector: str, content: str):
    prompt = f"""
You are an expert trade analyst. Based on this Indian {sector} sector news, write a markdown report with:

- 📌 Headline Summary
- 📈 Key Trends
- 💼 Trade Opportunities
- 📝 One-line Summary

News:
{content}
"""

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(TOGETHER_URL, headers=headers, json=payload)

        print("📡 TogetherAI response:", response.status_code)
        print(response.text)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        return f"⚠️ TogetherAI Error {response.status_code}: {response.text}"



