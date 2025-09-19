from crewai import Agent
import json
import os

class ReportGenerator(Agent):
    def __init__(self):
        super().__init__(
            role="Report Generator",
            goal="Generate structured JSON or Markdown reports from dependency scan results.",
            backstory="You organize scanned data into readable reports for auditing and vulnerability checking.",
            tools=[],
            verbose=True
        )

    def run(self, inputs):
        deps = inputs.get("dependencies")
        if not deps:
            return {"error": "No dependency data available to generate report."}

        # Ensure data folder exists
        os.makedirs("data", exist_ok=True)
        report_path = os.path.join("data", "report.json")

        # Write JSON report
        with open(report_path, "w") as f:
            json.dump(deps, f, indent=2)

        return {"report_path": report_path}
