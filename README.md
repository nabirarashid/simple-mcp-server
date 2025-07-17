# ai sticky notes mcp server

a model context protocol (mcp) server that provides ai assistants with the ability to manage persistent sticky notes. built with fastmcp for simplicity and ease of use.

## what it does

this server provides note-taking capabilities for ai assistants:

- **add note tool**: save new notes to persistent storage
- **read notes tool**: retrieve all saved notes
- **latest note resource**: access the most recently added note
- **note summary prompt**: generate prompts to summarize current notes

## features

- persistent note storage in a local text file
- simple file-based storage (no database required)
- automatic file creation and management
- integration with claude desktop app

## installation

1. make sure you have python 3.12+ installed
2. clone or download this project
3. install dependencies:
   ```bash
   uv add fastmcp
   ```

## running the server

### test locally

```bash
uv run python main.py stdio
```

### use with claude desktop app

1. create the claude config directory:

   ```bash
   mkdir -p ~/Library/Application\ Support/Claude
   ```

2. create a configuration file at `~/Library/Application Support/Claude/claude_desktop_config.json`:

   ```json
   {
     "mcpServers": {
       "sticky-notes": {
         "command": "uv",
         "args": ["run", "python", "/path/to/your/project/main.py"],
         "cwd": "/path/to/your/project"
       }
     }
   }
   ```

3. restart claude desktop app

## testing the features

once connected to claude, you can:

- ask claude to "add a note about today's meeting"
- request "show me all my notes" to read all saved notes
- ask "what was my latest note?" to get the most recent note
- request "summarize my notes" to use the summary prompt

## project structure

```
mcp server/
├── main.py              # main server code with note management
├── pyproject.toml       # project dependencies
├── README.md           # this file
├── notes.txt           # persistent note storage (auto-created)
└── uv.lock            # dependency lock file
```

## dependencies

- `fastmcp`: simplified mcp server framework
- `mcp`: core model context protocol library

## how it works

notes are stored in a simple text file (`notes.txt`) in the project directory. each note is stored on a new line, making it easy to read and manage. the server automatically creates the file if it doesn't exist.

## about mcp

the model context protocol (mcp) allows ai assistants like claude to connect to external tools and data sources. this server demonstrates how to create persistent storage capabilities that claude can use across conversations.
