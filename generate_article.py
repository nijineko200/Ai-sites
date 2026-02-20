import os, datetime
from openai import OpenAI

# APIの初期化（api_keyのタイポ修正済み）
client = OpenAI(
    base_url="https://models.inference.ai.azure.com", 
    api_key=os.environ["GH_MODELS_TOKEN"]
)

def generate():
    messages=[{
        "role": "user", 
        "content": """Act as a senior technology journalist at 'TechPulse Global'. 
        Write a professional analysis article in English.
        
        Requirements:
        - Topic: Future tech trends, AI, or digital economy.
        - Structure: Title on the first line, then 3-4 sections with '##' subheadings.
        - Content: Deep-dive analysis, not just news. Use bullet points for key takeaways.
        - Style: Authoritative and sophisticated.
        - DO NOT mention you are an AI. 
        - DO NOT use HTML tags. Use pure Markdown only."""
    }]
    
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    content = res.choices[0].message.content
    lines = content.split('\n')
    title = lines[0].replace('#', '').strip()
    body = '\n'.join(lines[1:])
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 記事を保存するディレクトリ
    os.makedirs("src/pages/blog", exist_ok=True)
    
    # Astro用フロントマターを付けて保存
    with open(f"src/pages/blog/{date}.md", "w", encoding="utf-8") as f:
        f.write(f"---\nlayout: ../../layouts/Layout.astro\ntitle: \"{title}\"\ndate: \"{date}\"\n---\n\n{body}")

if __name__ == "__main__":
    generate()
