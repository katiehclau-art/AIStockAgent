from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate
from langgraph.checkpoint.memory import InMemorySaver
import yfinance as yf
import python_weather
import asyncio
import os

# openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    # model="gpt-5",
    # model="gpt-5-nano",
    # model="gpt-5-mini",
    model="gpt-4.1-mini",
    temperature=0.1,
    max_tokens=1000,
    timeout=30,
    # ... (other params)
)


@tool
def get_stock_price(ticker_symbol: str) -> str:
    """Get stock price for a given symbol."""

    # Define the ticker symbol (e.g., Apple)
    # ticker_symbol = "AAPL"

    # Get the ticker object
    tckr = yf.Ticker(ticker_symbol)

    # Access fast_info for current price
    # The 'last_price' attribute provides the actual current or last traded price
    current_price = tckr.fast_info.last_price

    print(f"The current price for {ticker_symbol} is: {current_price}")
    return f"stock price for {ticker_symbol} is {current_price}"


@tool
def get_stock_info(ticker_symbol: str) -> str:
    """Get stock information for a given symbol."""

    # Define the ticker symbol (e.g., Apple)
    # ticker_symbol = "AAPL"

    # Get the ticker object
    tckr = yf.Ticker(ticker_symbol)

    stock_info = tckr.fast_info

    data_json = stock_info.toJSON()

    return f"stock information is {data_json}"
    # return f"stock information is {stock_info}"


@tool
def get_stock_news(ticker_symbol: str) -> str:
    """Get stock news for a given symbol."""

    # Get the ticker object
    stock = yf.Ticker(ticker_symbol)

    # Get the news feed
    news_feed = stock.news

    return f"stock new for {ticker_symbol} is {news_feed}"


@tool
def get_weather(city: str) -> str:
    """Get weather or the tempature for a given city."""

    print(f"The weather !!")

    # # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
    # client = python_weather.Client(unit=python_weather.IMPERIAL)

    # # Fetch a weather forecast from a city.
    # weather = client.get('New York')

    # # Fetch the temperature for today.
    # print(weather.temperature)

    return f"It's always sunny in {city}!"
    # return f"The temperature of {city} is {weather.temperature} !"


checkpointer = InMemorySaver()

agent = create_agent(
    model=llm,
    checkpointer=checkpointer,
    # system_prompt="You are a helpful AI assistant to know everything about stock",
    tools=[get_stock_price, get_stock_info, get_stock_news, get_weather],
    # debug=True
    name="stockAgent",
)

# Specify an ID for the thread
config = {"configurable": {"thread_id": "abc123"}}

while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break

    # Run the agent with the user's input
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]}, config=config)

    # Print the agent's final response
    print("Assistant:", result["messages"][-1].content)
