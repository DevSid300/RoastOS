import ollama
from prompts import prompts

def roast_user(activity):

    prompt_template = prompts["roast"]

    prompt = prompt_template.format(activity=activity)

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    result = response['message']['content'].strip()

    # Cleanup
    result = result.replace("\n\n", "\n")
    result = result.replace("\n", " ")

    # Keep concise
    words = result.split()[:25]

    result = " ".join(words)

    return result