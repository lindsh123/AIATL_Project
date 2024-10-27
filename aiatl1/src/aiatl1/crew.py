from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM
from crewai.flow.flow import Flow, and_, listen, start
from tools.custom_tool import CardioMedicalReportRAG, PulmoMedicalReportRAG
from crewai_tools import FileWriterTool, FileReadTool	


file_writer_tool = FileWriterTool()
file_reader_tool = FileReadTool()

google_api_key = os.getenv("GOOGLE_API_KEY")
llm = LLM(
    model="gemini/gemini-1.5-flash", verbose=True, temperature=0.9, google_api_key=google_api_key
)

@CrewBase
class Aiatl1Crew():
    """Aiatl1 crew"""

    @agent
    def cardiologist(self) -> Agent:
        return Agent(
            config=self.agents_config['cardiologist'],
            verbose=True,
            llm=llm,
            memory = True,
            tools = [CardioMedicalReportRAG()],
            allow_delegation = False,
            max_iter = 3,
        )

    @agent
    def pulmonologist(self) -> Agent:
        return Agent(
            config=self.agents_config['pulmonologist'],
            verbose=True,
            llm=llm,
            memory = True,
            tools = [PulmoMedicalReportRAG()],
            allow_delegation = False,
            max_iter = 3,
        )

    @agent
    def general_practitioner(self) -> Agent:
        return Agent(
            config=self.agents_config['general_practitioner'],
            verbose=True,
            llm=llm,
            memory = True,
            allow_delegation = False,
            max_iter = 3,
        )

    @agent
    def diagnosis_decider(self) -> Agent:
        return Agent(
            config=self.agents_config['diagnosis_decider'],
            verbose=True,
            llm=llm,
            memory = True,
            max_iter = 3,
            tools = [file_reader_tool],
        )
    @agent
    def diagnosis_dei(self) -> Agent:
        return Agent(
            config=self.agents_config['diagnosis_dei'],
            verbose=True,
            llm=llm,
            memory = True,
            max_iter = 3,
        )
    
    @agent
    def diagnosis_deliverer(self) -> Agent:
        return Agent(
            config=self.agents_config['diagnosis_deliverer'],
            verbose=True,
            llm=llm,
            memory = True,
            allow_delegation = False,
            max_iter = 3,
        )

    @task
    def diagnosis_task_cardiologist(self) -> Task:
        return Task(
            config=self.tasks_config['diagnosis_task_cardiologist'],
            output_file='cardiologist_analysis.txt',
        )

    @task
    def diagnosis_task_pulmonologist(self) -> Task:
        return Task(
            config=self.tasks_config['diagnosis_task_pulmonologist'],
            output_file='pulmonologist_analysis.txt',
        )

    @task
    def diagnosis_task_general_practitioner(self) -> Task:
        return Task(
            config=self.tasks_config['diagnosis_task_general_practitioner']
        )


    @task
    def diagnosis_decision(self) -> Task:
        return Task(
            config=self.tasks_config['diagnosis_decision'],
            tools = FileReadTool(file_paths=['pulmonologist_analysis.txt', 'cardiologist_analysis.txt']),
        )
    
    @task
    def diagnosis_dei_customizer(self) -> Task:
        return Task(
            config=self.tasks_config['diagnosis_dei_customizer'],
        )
    


    @task
    def diagnosis_delivery(self) -> Task:
        return Task(
            config=self.tasks_config['diagnosis_delivery'],
            output_file='report.txt'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Aiatl1 crew"""
        return Crew(
            agents=self.agents,
            tasks=[
                self.diagnosis_task_cardiologist(), 
                self.diagnosis_task_pulmonologist(), 
                self.diagnosis_decision(), 
                self.diagnosis_dei_customizer(), 
                self.diagnosis_delivery()
            ],
            process=Process.sequential,
            verbose=True,
        )