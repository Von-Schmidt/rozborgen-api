import openai
import os

openai.api_key = 'apikey' #your key goes here

initial_system_prompt = "Nyní se s tebe stává učitel českého jazyka na kvalitním gymnáziu. Momentálně připravuješ pro studenty materiály, které jim budou sloužit k maturitě z českého jazyka. Tvým úkolem je připravit pouze vybranou rást literárního rozboru povinné četby k maturitě, která studentům pomůže se na ústní maturitní zkoušku se připravit."

# Function to rewrite a given text using OpenAI API
def rewrite_text(category, instructions, piece):
    messages = [
        {"role": "system", "content": "'{instructions}'"},
        {"role": "user", "content": f"'{category}', '{piece}'"},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.9,
        top_p=1,
    )

    return response.choices[0].message['content'].strip()

