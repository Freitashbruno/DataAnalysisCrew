from crewai import Agent, Task, Crew, Process
from data_analysis_crew.tools.data_tool import DataCollectionTool, StatisticalAnalysisTool, DataVisualizationTool


data_collector = Agent(
    role='Data Collector',
    goal='Gather data from various sources for analysis.',
    tools=[DataCollectionTool]
)

data_analyst = Agent(
    role='Data Analyst',
    goal='Perform statistical analysis on collected data.',
    tools=[StatisticalAnalysisTool]
)

data_visualizer = Agent(
    role='Data Visualizer',
    goal='Create compelling visualizations from analyzed data.',
    tools=[DataVisualizationTool]
)

collect_data_task = Task(
    description='Collect data from various sources, ensuring it is clean and ready for analysis.',
    expected_output='A cleaned dataset ready for analysis.',
    agent=data_collector,
)

analyze_data_task = Task(
    description='Perform a detailed statistical analysis on the collected dataset.',
    expected_output='A report summarizing the statistical findings.',
    agent=data_analyst,
)

visualize_data_task = Task(
    description='Create visualizations that highlight key insights from the data analysis. Ensure the use of coherent graphs and storytelling techniques to present the data effectively.',
    expected_output='A set of visualizations that effectively communicate the analysis results using storytelling techniques.',
    agent=data_visualizer,
)

crew = Crew(
    agents=[data_collector, data_analyst, data_visualizer],
    tasks=[collect_data_task, analyze_data_task, visualize_data_task],
    process=Process.sequential
)
