import datetime

def generate_markdown(sector, sources, analysis):
    date = datetime.datetime.now().strftime("%d %B %Y")

    markdown = f"""# 📊 Market Analysis Report: {sector.capitalize()} - India
*Date: {date}*

---

## 🔍 Sources Used
{sources.strip()}

---

## 🧠 AI Analysis
{analysis.strip()}

---

"""
    return markdown.strip()
