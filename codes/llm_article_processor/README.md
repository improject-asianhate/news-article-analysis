# LLM-based Article Processor

This Python script processes text articles using OpenAI's GPT model and converts the responses into CSV files.

## Features

- Reads multiple text articles from a directory
- Uses a prompt template to create customized prompts for each article
- Sends prompts to OpenAI's GPT model for processing
- Converts responses into CSV format
- Saves results as individual CSV files

## Requirements

- Python 3.6+
- pandas
- openai

## Setup

1. Install required packages:
2. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```
3. Prepare your directory structure:
   ```
   project_directory/
    ├── process_articles.py
    ├── prompt.txt
    ├── articles/
    │   ├── 1.txt
    │   ├── 2.txt
    │   └── ...
    └── responses/
   ```

## Usage

1. Place your articles as .txt files in the `articles/` directory.

2. Ensure your prompt template is in `prompt.txt`. Use `[Insert the article text here]` where you want the article text to be inserted.

3. Run the script:
   ```
   python process_articles.py
   ```

4. Find the resulting CSV files in the `responses/` directory.

## How It Works

1. Reads the prompt template from `prompt.txt`.
2. Reads all .txt files from the `articles/` directory.
3. Creates a custom prompt for each article by inserting the article text into the template.
4. Sends each prompt to the OpenAI API and receives a response.
5. Extracts CSV data from each response.
6. Saves each extracted CSV as a separate file in the `responses/` directory.

## Customization

- To use a different GPT model, modify the `model` parameter in the `get_response()` function.
- To change the input or output directories, modify the respective paths in the `main()` function.

## Troubleshooting

- If you encounter API errors, ensure your OpenAI API key is correctly set and you have sufficient credits.
- For CSV parsing issues, check that the API responses are in the expected format.