from crewai import Task
from agents.repo_cloner import RepoCloner
from agents.dependency_checker import DependencyChecker
from agents.report_generator import ReportGenerator  # new agent

# Task 1: Clone Bitbucket repository
clone_task = Task(
    name="Clone Repository",
    description="Clone the Bitbucket repository into a local folder",
    expected_output="Path to the cloned repository on disk",
    agent=RepoCloner(),
    role="Clone the repository",
    goal="Provide the local path of the cloned repository",
    backstory="This task clones a Bitbucket repository for further analysis"
)

# Task 2: Extract dependencies
dependency_task = Task(
    name="Dependency Check",
    description="Extract all Go dependencies (direct + indirect) from the cloned repo",
    expected_output="Dependencies in JSON/DF format",
    agent=DependencyChecker(),
    role="Analyze project dependencies",
    goal="Provide a detailed dependency graph",
    backstory="This task lists all dependencies from go.mod and go mod graph"
)

# Task 3: Generate report
report_task = Task(
    name="Generate Report",
    description="Generate a report of all dependencies in CSV or JSON format",
    expected_output="Dependency report file path",
    agent=ReportGenerator(),
    role="Create a report from the dependency data",
    goal="Provide a human-readable report for auditing and vulnerability checks",
    backstory="This task takes dependency data and generates a structured report"
)
