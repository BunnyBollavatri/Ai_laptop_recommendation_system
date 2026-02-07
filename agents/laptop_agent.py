from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from tools.laptop_tools import gaming_laptops

from config import GROQ_API_KEY
from tools.laptop_tools import (
    search_by_budget,
    filter_by_ram,
    best_value_laptops
)

# -----------------------------
# TOOLS
# -----------------------------

@tool
def budget_search(max_price: int):
    """Find laptops under a given budget."""
    return search_by_budget(max_price)


@tool
def ram_search(min_ram: int):
    """Find laptops with minimum RAM."""
    return filter_by_ram(min_ram)


@tool
def best_value_search(max_price: int):
    """Find best value laptops."""
    return best_value_laptops(max_price)

@tool
def gaming_search(max_price: int = 150000, limit: int = 20):
    """Find high performance gaming laptops."""
    return gaming_laptops(max_price, limit)



tools = [
    budget_search,
    ram_search,
    best_value_search,
    gaming_search
]



# -----------------------------
# LLM
# -----------------------------

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)


# -----------------------------
# PROMPT
# -----------------------------

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert laptop recommendation AI. Always use tools."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])


# -----------------------------
# AGENT
# -----------------------------

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# ⭐ THIS is what Streamlit imports
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False
)
