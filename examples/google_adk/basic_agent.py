import asyncio
import os

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types


def get_weather(city: str) -> dict[str, str | int]:
    """Return fixed mock weather for a city, not a real forecast."""
    return {"city": city, "weather": "sunny", "temperature_c": 22, "source": "mock"}


async def main() -> None:
    if not os.environ.get("GOOGLE_API_KEY"):
        raise SystemExit("Set GOOGLE_API_KEY before running this example.")
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

    agent = Agent(
        name="weather_agent",
        model="gemini-flash-latest",
        instruction="Use get_weather for weather questions. Label the data as mock.",
        tools=[get_weather],
    )
    runner = InMemoryRunner(agent=agent, app_name="weather_example")
    try:
        session = await runner.session_service.create_session(
            app_name=runner.app_name, user_id="example_user"
        )
        message = types.Content(
            role="user",
            parts=[types.Part.from_text(text="What is the weather in Paris?")],
        )
        async for event in runner.run_async(
            user_id=session.user_id,
            session_id=session.id,
            new_message=message,
        ):
            if event.is_final_response() and event.content:
                text = "".join(part.text or "" for part in event.content.parts or [])
                if text:
                    print(text)
    finally:
        await runner.close()


if __name__ == "__main__":
    asyncio.run(main())
