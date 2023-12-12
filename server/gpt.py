from openai import OpenAI

with open("openaikey.txt", "r") as f:
    client = OpenAI(api_key=f.readline())


def generate_new(msg):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": f"""Sử dụng tiếng Việt, The following is set of summaries:\n{msg}\nSort major changes to the top, take these and distill it into a final, consolidated summary of the main themes.\nHelpful Answer:"""}],
        max_tokens=1000,
        n=1,
        temperature=0
    )
    return response.choices[0].message.content
