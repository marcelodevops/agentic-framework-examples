import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def get_weather(city: str) -> str:
    """Return fixed mock weather for a city, not a real forecast."""
    return f"Mock weather in {city}: sunny, 22 degrees Celsius."


async def main() -> None:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("Set OPENAI_API_KEY before running this example.")

    client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    try:
        agent = AssistantAgent(
            name="weather_agent",
            model_client=client,
            tools=[get_weather],
            system_message="Use get_weather for weather questions. Label the data as mock.",
            reflect_on_tool_use=True,
        )
        result = await agent.run(task="What is the weather in Paris?")
        print(result.messages[-1].content)
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
