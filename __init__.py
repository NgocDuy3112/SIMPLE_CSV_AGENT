from langchain.agents import AgentExecutor

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_experimental.agents.agent_toolkits.pandas.prompt import PREFIX

from langchain_core.prompts import PromptTemplate

from langchain_ollama import OllamaLLM

from langchain_huggingface import HuggingFaceEmbeddings

import pandas as pd
import streamlit as st