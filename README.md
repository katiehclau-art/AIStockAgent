# Description
An AI Stock Agent that checks stock prices, stock news, and more related information.

The AI Agent is built with Lanchain/Langraph, and uses OpenAI LLM, and live data from yahoo finance.

## Create and activate the virtual environment in MacOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
## Install required packages
```
pip install -r requirements.txt
```
## Setting the environment variable:
```
export OPENAI_API_KEY=<your OPENAI API KEY>
```

## Running the AI Agent:
```
python AiStockAgent.py
```
## Example:
````
User: What is the stock price of microsoft and what news is there about the company?
Assistant: The current stock price of Microsoft (MSFT) is approximately $479.28.

Here are some recent news highlights related to Microsoft:
1. Fiserv (FISV) announced a strategic collaboration with Microsoft to ramp up innovation by embedding AI into Fiserv development platforms and empowering the global workforce with AI.
2. There is a discussion on top AI stock picks including Nvidia, Intel, and AMD, with expert insights on the latest market action.
3. Bill Gates has 59% of his foundation's $38 billion portfolio invested in three phenomenal stocks, with a focus on value stocks.
4. Other news includes AI infrastructure growth, security breach concerns, and AI shopping initiatives involving Microsoft Copilot.
````
