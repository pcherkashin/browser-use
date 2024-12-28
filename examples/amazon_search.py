"""
Simple try of the agent.

@dev You need to add ANTHROPIC_API_KEY to your environment variables.
"""

import os
import sys

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from langchain_anthropic import ChatAnthropic

from browser_use import Agent

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

# Ensure ANTHROPIC_API_KEY is set in the environment variables
api_key = os.getenv('ANTHROPIC_API_KEY')
if not api_key:
	raise ValueError('The ANTHROPIC_API_KEY environment variable is not set')

llm = ChatAnthropic(model_name='claude-3-5-sonnet-20240620', api_key=api_key)
agent = Agent(
	task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
	llm=llm,
)


async def main():
	await agent.run(max_steps=10)
	# Commenting out the method call as it doesn't exist
	# agent.create_history_gif()


asyncio.run(main())
