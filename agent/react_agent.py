import os
import datetime
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent
from mcp_use import MCPClient, LangChainAdapter
from typing import List
from loguru import logger