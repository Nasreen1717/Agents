import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig  # ✅ Required

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Setup the Gemini provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Setup model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# ✅ Set up run config
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Greeting Agent
agent = Agent(
    name="Greeting Agent",
    instructions=(
        "You are a friendly Greeting Agent. "
        "If the user says 'hi' or any kind of greeting, respond with: 'Salam! This is Nasreen, wishing you a wonderful day!' "
        "If the user says 'bye' or any farewell, respond with: 'Allah Hafiz! Stay safe and take care — from Nasreen.' "
        "For anything else, respond with: 'Nasreen is here only to greet. I'm not programmed to answer other queries. Sorry!'"
    ),
    model=model
)

# Get user input
user_question = input("Please enter your question: ")

# ✅ Pass config to run_sync
result = Runner.run_sync(agent, user_question, run_config=config)

# Print result
print(result.final_output)
