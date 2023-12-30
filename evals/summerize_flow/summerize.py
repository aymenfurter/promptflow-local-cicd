from promptflow import tool
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from summarizer import summarize_text


@tool
def test_summarize(text: str) -> str:
    return summerize_text(text)