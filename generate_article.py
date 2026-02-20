import os, datetime
from openai import OpenAI

client = OpenAI(base_url="https://models.inference.ai.azure.com", api_key=os.environ["GH_MODELS_TOKEN"])
def generate():
    messages=[{
        "role": "user", 
        "content": """Act as a professional technology journalist at 'TechPulse Global'. 
        Write a deep-dive analysis article in English.
        - Topic: Future tech trends or AI's impact on business/society.
        - Format: First line must be the Title.
        - Tone: Serious, analytical, and authoritative.
        - DO NOT use AI-like phrases. DO NOT mention you are an AI.
        - Length: Minimum 500 words with several subheadings."""
    }]
    
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    text = res.choices[0].message.content
    lines = text.split('\n')
    title = lines[0].replace('#', '').strip()
    body = '\n'.join(lines[1:])
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # 重要：保存先を src/pages/blog にして自動ページ化
    os.makedirs("src/pages/blog", exist_ok=True)
    with open(f"src/pages/blog/{date}.md", "w", encoding="utf-8") as f:
        f.write(f"---\nlayout: ../../layouts/Layout.astro\ntitle: \"{title}\"\ndate: \"{date}\"\n---\n\n{body}")

if __name__ == "__main__":
    generate()
