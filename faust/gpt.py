from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_KEY)


def generate_new(msg):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": f"""từ những thông tin sau hãy viết 1 bản tin về tình hình tiền ảo giữ nguyên cặp mã tiền ảo:\n{msg}"""}],
        max_tokens=2048,
        n=1,
        temperature=0
    )
    return response.choices[0].message.content
