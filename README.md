# Agentic framework examples

Minimal Python examples showing how to build a basic agent with LangChain,
Google ADK, AutoGen, OpenAI Agents SDK, and CrewAI.

Each example gives one agent a typed `get_weather` tool and asks for the weather
in Paris. The tool returns **fixed mock data, not a real forecast**. The model
decides when to call the tool and turns its result into an answer.

## Examples

| Framework | Script | Dependencies | API key |
| --- | --- | --- | --- |
| [LangChain](https://docs.langchain.com/oss/python/langchain/quickstart) | [basic_agent.py](examples/langchain/basic_agent.py) | [requirements.txt](examples/langchain/requirements.txt) | `OPENAI_API_KEY` |
| [Google ADK](https://google.github.io/adk-docs/get-started/python/) | [basic_agent.py](examples/google_adk/basic_agent.py) | [requirements.txt](examples/google_adk/requirements.txt) | `GOOGLE_API_KEY` |
| [AutoGen](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/quickstart.html) | [basic_agent.py](examples/autogen/basic_agent.py) | [requirements.txt](examples/autogen/requirements.txt) | `OPENAI_API_KEY` |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/quickstart/) | [basic_agent.py](examples/openai_agents/basic_agent.py) | [requirements.txt](examples/openai_agents/requirements.txt) | `OPENAI_API_KEY` |
| [CrewAI](https://docs.crewai.com/en/quickstart) | [basic_agent.py](examples/crewai/basic_agent.py) | [requirements.txt](examples/crewai/requirements.txt) | `OPENAI_API_KEY` |

## Quick start

Use **Python 3.11 or 3.12** and a separate virtual environment for each example.
The frameworks can have incompatible transitive dependencies; do not install
all five requirements files into one environment.

From the repository root, choose a framework directory from the table:

```bash
cd examples/langchain
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` instead.

Set your provider key in the shell, then run the example:

```bash
export OPENAI_API_KEY="your-api-key"
python basic_agent.py
```

For Google ADK, use the Gemini Developer API instead:

```bash
export GOOGLE_API_KEY="your-api-key"
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
python basic_agent.py
```

In PowerShell use `$env:OPENAI_API_KEY = "your-api-key"` (or
`$env:GOOGLE_API_KEY` and `$env:GOOGLE_GENAI_USE_VERTEXAI = "FALSE"`).
Do not put real keys in source files or commit them.

The OpenAI-backed examples use `gpt-4o-mini`; Google ADK uses
`gemini-flash-latest`. You can change the model in the script if your account
requires a different model. Successful runs print an answer based on the mock
weather: sunny, 22 °C in Paris. Exact wording and tool selection vary by model.
Live runs need network access and may incur provider charges.

## What to compare

- **LangChain:** `create_agent` wraps a chat model and Python tool.
- **Google ADK:** an `Agent` runs through an in-memory session and async events.
- **AutoGen:** `AssistantAgent` uses a model client and reflects on tool results.
- **OpenAI Agents SDK:** `function_tool` exposes a function to an `Agent`;
  `Runner` executes it.
- **CrewAI:** an `Agent` owns a `Task`, executed by a single-agent `Crew`.

These are deliberately standalone scripts rather than production applications.
No real weather service, deployment setup, or test infrastructure is required.