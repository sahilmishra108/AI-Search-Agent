# AI Search Agent

AI Search Agent is a multi-source research assistant that leverages Google, Bing, and Reddit to provide comprehensive answers to user queries. Powered by Google Gemini API, LangGraph, and Streamlit, it offers a modern frontend for interactive research.

## Features
- **Multi-source search:** Aggregates results from Google, Bing, and Reddit.
- **AI-powered analysis:** Uses Gemini (Google Generative AI) for deep analysis and synthesis of search results.
- **Streamlit frontend:** User-friendly web interface for asking questions and viewing results.
- **Parallel research:** Executes searches and analyses in parallel for faster responses.

## Technologies Used
- Python 3.12+
- LangGraph
- Google Generative AI (Gemini)
- Streamlit
- BrightData API (for web search)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sahilmishra108/AI-Search-Agent.git
   cd AI-Search-Agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or use `uv`:
   ```bash
   uv add langchain langgraph python-dotenv google-generativeai streamlit requests
   ```

3. **Configure environment variables:**
   - Create a `.env` file in the project root:
     ```env
     GOOGLE_API_KEY=your_google_gemini_api_key
     BRIGHTDATA_API_KEY=your_brightdata_api_key
     ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   The app will be available at [http://localhost:8501](http://localhost:8501).

## Usage
- Enter your question in the input box and click "Search".
- The agent will fetch and analyze results from Google, Bing, and Reddit.
- View the synthesized answer and individual analyses in the results panel.

## Project Structure


```
AI-Search-Agent/
├── app.py                  # Streamlit frontend
├── main.py                 # Core agent logic
├── web_operations.py       # Web search and Reddit API operations
├── snapshot_operations.py  # Snapshot polling and download logic
├── prompts.py              # Prompt templates for LLM
├── pyproject.toml          # Project metadata and build system
├── uv.lock                 # uv dependency lock file
├── requirements.txt        # Python dependencies (if present)
├── LICENSE                 # Project license
├── .env                    # API keys and environment variables
├── .gitignore              # Git ignore rules
├── .python-version         # Python version specification
├── README.md               # Project documentation
├── .git/                   # Git repository data
├── .venv/                  # Python virtual environment
├── __pycache__/            # Python bytecode cache
```

## License
This project is licensed under the MIT License.

## Author
[Sahil Mishra](https://github.com/sahilmishra108)
