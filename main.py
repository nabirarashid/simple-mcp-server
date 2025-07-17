from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    # docstring
    """
    
    Append a new note to the sticky notes file.

    Args:
        message (str): The note content to be added.

    Returns:
        str: Confirmation message indicating the note has been saved."""
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note saved!"

@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the sticky notes file.

    Returns:
        str: All notes as a single string separated by line breaks.
            If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
        return content or "No notes available."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """""
    Retrieve the latest note from the sticky notes file.
    Returns:
        str: The latest note content.
            If no notes exist, a default message is returned.
    """""
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes available."

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    
    Generate a prompt to summarize the current notes.
    Returns:
        str: A prompt string summarizing the current notes.
            If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "There are no notes to summarize."
    return f"Summarize the current notes {content}"