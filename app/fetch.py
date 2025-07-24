
import os
import httpx

NEWS_API_KEY = "6c25963545294b9493ea56900f0fc142"
NEWS_API_URL = "https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize=5&apiKey={key}"

async def get_sector_data(sector: str):
    query = f"{sector} sector India"
    url = NEWS_API_URL.format(query=query, key=NEWS_API_KEY)

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return None
        data = response.json()
        articles = data.get("articles", [])
        if not articles:
            return None

        # Format titles and URLs for markdown generation
        content = ""
        for article in articles:
            title = article.get("title", "No Title")
            url = article.get("url", "")
            content += f"- [{title}]({url})\n"
        return content