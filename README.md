## Model Context Protocol (MCP) 
![Screenshot 2025-06-13 233758](https://github.com/user-attachments/assets/f1da4dd5-c265-4c05-986a-cdd31ee6cac0)

## 🔍 Project Overview 
MCP (*Model Context Protocol*) is a standardized approach to:  
- **Manage conversational context** in AI agents (memory, session states).  
- **Integrate external tools** (web scraping, APIs, databases) via unified protocols.  
- **Support multi-component workflows** (e.g., search → data extraction → storage).  

Built with:  
- **UV Python** for dependency management.  
- **Playwright** for browser automation.  
- **DuckDuckGo** for search.  
- **Airbnb API** (or scraping) for accommodation data.  

---

## 🛠 **Features**  
1. **Context-Aware Chat Interface**  
   - Interactive CLI with memory (`clear`/`exit` commands).  
   - Async support for concurrent operations.  
2. **Tool Integration**  
   - Web search (DuckDuckGo).  
   - Browser automation (Playwright).  
   - Custom Airbnb data pipelines.  
3. **Protocol Extensibility**  
   - Add new tools via MCP-compliant modules.  

---

## ⚙️ **Installation**  
```bash
# Clone & set up (UV Python recommended)
git clone https://github.com/yourusername/mcp-protocol.git
cd mcp-protocol
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install with UV
uv pip install -r requirements.txt
```

---

## 🚀 **Usage**  
Run the interactive agent:  
```bash
python app.py
```  
**Commands**:  
- `exit`/`quit`: End session.  
- `clear`: Reset conversation memory.  
- Custom tool triggers (e.g., `search <query>`).  

Example workflow:  
```plaintext
You: search hotels in Paris
Assistant: [DuckDuckGo results...]
You: scrape Airbnb listings
Assistant: [Playwright extracts data...]
```

---


## 📜 **MCP Specification**  
1. **Context Protocol**: JSON-based schema for model state.  
   Example:  
   ```json
   {
     "session_id": "xyz",
     "memory": ["user: search Paris", "agent: results..."],
     "tools": ["search", "scrape"]
   }
   ```  
2. **Tool Adapters**: Standardized `execute()` method for all integrations.  

---

# Notes
The system currently includes basic functionality for:

Web searches via DuckDckGo

Airbnb data processing

Interactive chat interface with memory management

Future improvements may include enhanced search capabilities, more Airbnb-specific features, and additional automation options.
