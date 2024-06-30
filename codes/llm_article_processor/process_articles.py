import os
import pandas as pd
from io import StringIO
from openai import OpenAI

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def read_articles(directory):
    articles = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            articles[filename] = read_file(os.path.join(directory, filename))
    return articles

def create_prompts(prompt_template, articles):
    return {filename: prompt_template.replace('[Insert the article text here]', article) 
            for filename, article in articles.items()}

def get_response(prompt):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

def process_response(response):
    content = response[response.find("```\n")+3:response.rfind("\n```")]
    return pd.read_csv(StringIO(content), sep="/")

def save_csv(df, filename, directory):
    output_path = os.path.join(directory, filename.replace(".txt", ".csv"))
    df.to_csv(output_path, index=False)
    print(f'{filename} done')

def main():
    # Read the prompt template
    prompt_template = read_file('prompt.txt')

    # Read and process articles
    articles = read_articles('./articles')
    prompts = create_prompts(prompt_template, articles)

    # Get responses
    responses = {filename: get_response(prompt) for filename, prompt in prompts.items()}

    # Process and save responses
    for filename, response in responses.items():
        df = process_response(response)
        save_csv(df, filename, './responses')

if __name__ == "__main__":
    main()