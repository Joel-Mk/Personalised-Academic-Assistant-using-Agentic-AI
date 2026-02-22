from prompts import AGENT_PROMPT
from actions import plan_study, generate_notes, suggest_resources
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_agent(user_input: str):
    prompt = AGENT_PROMPT.format(user_input=user_input)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    action = response.choices[0].message.content.strip()

    if action == "PLAN_STUDY":
        output = plan_study(user_input)
    elif action == "GENERATE_NOTES":
        output = generate_notes(user_input)
    elif action == "SUGGEST_RESOURCES":
        output = suggest_resources(user_input)
    else:
        output = "Could not decide an action."

    return action, output
