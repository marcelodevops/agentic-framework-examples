import asyncio
import os

from agents import Agent, Runner, function_tool


@function_tool
def get_weather(city: str) -> str:
    """Return fixed mock weather for a city, not a real forecast."""
    return f"Mock weather in {city}: sunny, 22 degrees Celsius."


async def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this example.")

    agent = Agent(
        name="Weather assistant",
        model="gpt-4o-mini",
        instructions="Use get_weather for weather questions. Label the data as mock.",
        tools=[get_weather],
    )
    result = await Runner.run(agent, "What is the weather in Paris?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
