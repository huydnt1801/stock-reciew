from openai import OpenAI

with open("openaikey.txt", "r") as f:
    client = OpenAI(api_key=f.readline())


def generate_new(msg):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": f"""từ những thông tin sau hãy viết 1 bản tin về tình hình tiền ảo:\n{msg}"""}],
        max_tokens=2048,
        n=1,
        temperature=0
    )
    return response.choices[0].message.content
