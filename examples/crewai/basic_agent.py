import os

from crewai import Agent, Crew, Task
from crewai.tools import tool


@tool("get_weather")
def get_weather(city: str) -> str:
    """Return fixed mock weather for a city, not a real forecast."""
    return f"Mock weather in {city}: sunny, 22 degrees Celsius."


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this example.")

    agent = Agent(
        role="Weather assistant",
        goal="Answer weather questions using get_weather and label the data as mock.",
        backstory="You report mock weather accurately and concisely.",
        llm="openai/gpt-4o-mini",
        tools=[get_weather],
        allow_delegation=False,
    )
    task = Task(
        description="Use get_weather to find the weather in {city}.",
        expected_output="A concise weather report clearly labeled as mock data.",
        agent=agent,
    )
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff(inputs={"city": "Paris"})
    print(result.raw)


if __name__ == "__main__":
    main()
