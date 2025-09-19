from crewai import Agent
import subprocess, os, re, pandas as pd

class DependencyChecker(Agent):
    def __init__(self):
        super().__init__(
            role="Go Dependency Analyzer",
            goal="Extract Go module dependencies (direct and indirect) from go.mod and go mod graph.",
            backstory="You are skilled in analyzing Go projects and building parent-child dependency graphs.",
            tools=[],
            verbose=True
        )

    def run(self, inputs):
        project_path = inputs.get("repo_path")
        if not os.path.exists(os.path.join(project_path, "go.mod")):
            return {"error": "go.mod not found in the repository."}

        try:
            # List all dependencies
            result = subprocess.run(
                ["go", "list", "-m", "all"],
                cwd=project_path,
                capture_output=True, text=True, check=True
            )
            dependencies = [line.split()[0] for line in result.stdout.strip().split("\n")]

            # Build dependency graph
            graph_result = subprocess.run(
                ["go", "mod", "graph"],
                cwd=project_path,
                capture_output=True, text=True, check=True
            )
            graph_lines = graph_result.stdout.strip().split("\n")

            graph_data = []
            for dep in dependencies:
                for line in graph_lines:
                    if dep in line:
                        parent, child = line.strip().split()
                        parent_name, parent_version = parent.rsplit('@', 1) if '@' in parent else (parent, "v1")
                        child_name, child_version = child.rsplit('@', 1) if '@' in child else (child, "N/A")

                        graph_data.append({
                            "Direct dependency": parent_name,
                            "Direct dependency Version": parent_version,
                            "Indirect Dependency": child_name,
                            "Indirect dependency Version": child_version
                        })

            df = pd.DataFrame(graph_data)
            return {"dependencies": df.to_dict(orient="records")}

        except subprocess.CalledProcessError as e:
            return {"error": e.stderr}
