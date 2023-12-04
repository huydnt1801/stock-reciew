import openai

model = "text-davinci-003"
with open(".txt", "r") as f:
    openai.api_key = f.readline()

def res_from_chatgpt(question):
    response = openai.Completion.create(
        engine = model,
        prompt = question,
        max_tokens = 1024,
        n = 1,
        temperature = 0.5
    )
    response_text = response.choices[0].text
    return response_text