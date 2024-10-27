import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process, LLM
from crew import Aiatl1Crew
import os
from dotenv import load_dotenv

def run():
    load_dotenv()
    """
    Run the crew with user input.
    """
    user_input = input("Please provide your newest symptoms along with their pain level: ")
    user_name = input("What is your name?")
    user_race = input("What is your race?")
    user_gender = input("What is your gender?")

    crew_instance = Aiatl1Crew()

    inputs = {
        'symptoms': user_input,  
        'name': user_name,
        'race': user_race,
        'gender': user_gender,
    }

    crew_instance.crew().kickoff(inputs = inputs)
if __name__ == "__main__":
    run()