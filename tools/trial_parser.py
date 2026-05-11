import re
import json
from typing import Dict, Any, List

def clean_text(text: str) -> str:
    """Cleans whitespace and formatting from raw clinical text."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def find_section(text: str, section_name: str) -> str:
    # naive section finder (works surprisingly well for protocols)
    pattern = rf"({section_name})(.*?)(Inclusion Criteria|Exclusion Criteria|Eligibility Criteria|Endpoints|Study Design|$)"
    match   = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(2).strip()
    return ""

#def extract_eligibility_chunk(full_text: str) -> str:
#    """
#    Locates the 'Eligibility Criteria' section and extracts a 
#    manageable portion for LLM processing.
#    """
#    # Best effort: cut around "Eligibility Criteria"
#    start = re.search(r"Eligibility Criteria", full_text, re.IGNORECASE)
#    if not start:
#        return full_text[:20000]  # fallback: first pages only
#   chunk = full_text[start.start(): start.start() + 40000]
#    return chunk

def extract_eligibility_chunk(full_text: str) -> str:
    """
    Locates the 'Eligibility Criteria' section and extracts a 
    manageable portion for LLM processing.
    """
    start = re.search(r"Eligibility Criteria", full_text, re.IGNORECASE)
    if not start:
        return full_text[:20000]
    return full_text[start.start(): start.start() + 40000]


def chunk_text(text: str, max_chars: int = 12000) -> List[str]:
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]