import os

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


def get_weather(city: str) -> str:
    """Return fixed mock weather for a city, not a real forecast."""
    return f"Mock weather in {city}: sunny, 22 degrees Celsius."


def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this example.")

    agent = create_agent(
        model=ChatOpenAI(model="gpt-4o-mini"),
        tools=[get_weather],
        system_prompt="Use get_weather for weather questions. Label the data as mock.",
    )
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What is the weather in Paris?"}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
