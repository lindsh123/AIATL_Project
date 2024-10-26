import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process, LLM
from crew import Aiatl1Crew

def run():
    """
    Run the crew with user input.
    """
    user_input = input("Please provide your newest symptoms along with their pain level: ")
    user_name = input("What is your name?")
    #cardiologist_file = input("Please provide the cardiologist file name:")
    #pulmonologist_file = input("Please provide the pulmonologist file name:")

    # Create an instance of the crew
    crew_instance = Aiatl1Crew()

    # Prepare the input as a dictionary
    inputs = {
        'symptoms': user_input,  # Adjust the key as per your task's requirements
        'name': user_name,
        #'cardiologist_file': cardiologist_file,
        #'pulmonologist_file': pulmonologist_file,
    }

    crew_instance.crew().kickoff(inputs = inputs)
if __name__ == "__main__":
    run()