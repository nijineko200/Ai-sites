import os, datetime
from openai import OpenAI

# GitHub Models経由でGPT-4o-miniを叩く（安定ルート）
client = OpenAI(base_url="https://models.inference.ai.azure.com", api_key=os.environ["GH_MODELS_TOKEN"])

def generate():
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Write a tech news article about 2026. First line: Title."}]
    )
    text = res.choices[0].message.content
    title = text.split('\n')[0].replace('#', '').strip()
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 記事をフォルダに保存
    os.makedirs("src/content/blog", exist_ok=True)
    with open(f"src/content/blog/{date}.md", "w", encoding="utf-8") as f:
        f.write(f"---\nlayout: ../../layouts/Layout.astro\ntitle: \"{title}\"\ndate: \"{date}\"\n---\n\n{text}")

if __name__ == "__main__":
    generate()
