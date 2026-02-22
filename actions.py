from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def plan_study(topic):
    prompt = f"Create a 4-week structured study plan for {topic}."
    return call_llm(prompt)

def generate_notes(topic):
    prompt = f"Generate concise beginner-friendly notes on {topic}."
    return call_llm(prompt)

def suggest_resources(topic):
    prompt = f"Suggest books, videos, and online resources to learn {topic}."
    return call_llm(prompt)

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

