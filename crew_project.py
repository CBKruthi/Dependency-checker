# from crewai import Crew, Process
# from tasks import clone_task, dependency_task
# import getpass

# def main():
#     print("=== CrewAI Repo Dependency Scanner ===")

#     # Ask user for details
#     repo_url = input("Enter the Bitbucket repo URL: ").strip()
#     folder_name = input("Enter folder name to clone into (leave blank for default): ").strip()
#     username = input("Enter Bitbucket username (leave blank if public repo): ").strip()
#     token = ""
#     if username:
#         token = getpass.getpass("Enter Bitbucket app password (token): ").strip()

#     # Initialize Crew
#     crew = Crew(
#         agents=[clone_task.agent, dependency_task.agent],
#         tasks=[clone_task, dependency_task],
#         process=Process.sequential
#     )

#     # Kick off with dynamic inputs
#     result = crew.kickoff(inputs={
#         "repo_url": repo_url,
#         "folder_name": folder_name if folder_name else None,
#         "username": username if username else None,
#         "token": token if token else None
#     })

#     print("\n=== Final Crew Output ===")
#     print(result)

# if __name__ == "__main__":
#     main()





# import os
# from dotenv import load_dotenv
# from crewai import Crew, Process, LLM
# from tasks import clone_task, dependency_task, report_task

# # Load environment variables from .env
# load_dotenv()
# API_KEY = os.getenv("CREW_GEMINI_API_KEY")

# if not API_KEY:
#     API_KEY = input("Enter your Gemini API key: ").strip()  # fallback

# # Initialize LLM with Gemini
# gemini_llm = LLM(
#     model="gemini/gemini-2.5-pro",  # choose the Gemini model
#     api_key=API_KEY,
#     provider="google",               # specify the provider
#     temperature=0.0                  # optional, adjust response variability
# )

# def main():
#     crew = Crew(
#         agents=[clone_task.agent, dependency_task.agent, report_task.agent],
#         tasks=[clone_task, dependency_task, report_task],
#         process=Process.sequential,
#         llm=gemini_llm
#     )

#     repo_url = input("Enter the Bitbucket repo URL: ").strip()
#     folder_name = input("Enter folder name to clone into (leave blank for default): ").strip()
#     username = input("Enter Bitbucket username (leave blank if public repo): ").strip()
#     token = input("Enter Bitbucket app password (leave blank if public repo): ").strip()

#     result = crew.kickoff(inputs={
#         "repo_url": repo_url,
#         "folder_name": folder_name,
#         "username": username,
#         "token": token
#     })

#     print("=== Final Crew Output ===")
#     print(result)

# if __name__ == "__main__":
#     main()



# import os
# from dotenv import load_dotenv
# from crewai import Crew, Process, LLM
# from tasks import clone_task, dependency_task, report_task

# load_dotenv()
# API_KEY = os.getenv("CREW_GEMINI_API_KEY") or input("Enter Gemini API key: ").strip()

# gemini_llm = LLM(
#     model="gemini/gemini-2.5-pro",
#     api_key=API_KEY,
#     provider="google",
#     temperature=0.0
# )

# def main():
#     crew = Crew(
#         agents=[clone_task.agent, dependency_task.agent, report_task.agent],
#         tasks=[clone_task, dependency_task, report_task],
#         process=Process.sequential,
#         llm=gemini_llm
#     )

#     repo_url = input("Enter Bitbucket repo URL: ").strip()
#     folder_name = input("Enter folder name (blank for default): ").strip()
#     username = input("Enter Bitbucket username (blank if public): ").strip()
#     token = input("Enter Bitbucket app password (blank if public): ").strip()

#     result = crew.kickoff(inputs={
#         "repo_url": repo_url,
#         "folder_name": folder_name,
#         "username": username,
#         "token": token
#     })

#     print("=== Final Crew Output ===")
#     print(result)

# if __name__ == "__main__":
#     main()










# from crewai.llms import Gemini

# import os
# from dotenv import load_dotenv
# from crewai import Crew, Process
# from tasks import clone_task, dependency_task, report_task

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("CREW_GEMINI_API_KEY") or input("Enter your Gemini API key: ").strip()

# # Initialize Gemini LLM
# gemini_llm = Gemini(
#     api_key=API_KEY,
#     model="gemini/gemini-2.5-pro",  # pick model
#     temperature=0.0
# )

# def main():
#     crew = Crew(
#         agents=[clone_task.agent, dependency_task.agent, report_task.agent],
#         tasks=[clone_task, dependency_task, report_task],
#         process=Process.sequential,
#         llm=gemini_llm  # pass Gemini LLM here
#     )

#     repo_url = input("Enter Bitbucket repo URL: ").strip()
#     folder_name = input("Enter folder name (blank for default): ").strip()
#     username = input("Enter Bitbucket username (blank if public): ").strip()
#     token = input("Enter Bitbucket app password (blank if public): ").strip()

#     result = crew.kickoff(inputs={
#         "repo_url": repo_url,
#         "folder_name": folder_name,
#         "username": username,
#         "token": token
#     })

#     print("=== Final Crew Output ===")
#     print(result)

# if __name__ == "__main__":
#     main()


# from crewai.llms import OpenAI

# import os
# from dotenv import load_dotenv
# from crewai import Crew, Process
# from tasks import clone_task, dependency_task, report_task

# # Load environment variables
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY") or input("Enter your OpenAI API key: ").strip()

# # Initialize OpenAI LLM
# openai_llm = OpenAI(
#     api_key=API_KEY,
#     model="gpt-4o",  # or another OpenAI model
#     temperature=0.0
# )

# def main():
#     crew = Crew(
#         agents=[clone_task.agent, dependency_task.agent, report_task.agent],
#         tasks=[clone_task, dependency_task, report_task],
#         process=Process.sequential,
#         llm=openai_llm  # pass OpenAI LLM here
#     )

#     repo_url = input("Enter Bitbucket repo URL: ").strip()
#     folder_name = input("Enter folder name (blank for default): ").strip()
#     username = input("Enter Bitbucket username (blank if public): ").strip()
#     token = input("Enter Bitbucket app password (blank if public): ").strip()

#     result = crew.kickoff(inputs={
#         "repo_url": repo_url,
#         "folder_name": folder_name,
#         "username": username,
#         "token": token
#     })

#     print("=== Final Crew Output ===")
#     print(result)

# if __name__ == "__main__":
#     main()

import os
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from tasks import clone_task, dependency_task, report_task

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY") or input("Enter your OpenAI API key: ").strip()

# Initialize OpenAI LLM
openai_llm = LLM(
    model="openai/gpt-4o",  # You can use gpt-4o, gpt-4, gpt-3.5-turbo, etc.
    api_key=API_KEY,
    temperature=0.0
)

def main():
    crew = Crew(
        agents=[clone_task.agent, dependency_task.agent, report_task.agent],
        tasks=[clone_task, dependency_task, report_task],
        process=Process.sequential,
        llm=openai_llm  # pass LLM here
    )

    repo_url = input("Enter Bitbucket repo URL: ").strip()
    folder_name = input("Enter folder name (blank for default): ").strip()
    username = input("Enter Bitbucket username (blank if public): ").strip()
    token = input("Enter Bitbucket app password (blank if public): ").strip()

    result = crew.kickoff(inputs={
        "repo_url": repo_url,
        "folder_name": folder_name,
        "username": username,
        "token": token
    })

    print("=== Final Crew Output ===")
    print(result)

if __name__ == "__main__":
    main()



