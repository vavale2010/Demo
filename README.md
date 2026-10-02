# Demo - LangChain & Groq

A simple Python demo using [LangChain](https://www.langchain.com/) and [Groq](https://groq.com/) with the `openai/gpt-oss-120b` model.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vavale2010/Demo.git
   cd Demo
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv Myenv
   # On Windows:
   .\Myenv\Scripts\activate
   # On Linux/macOS:
   source Myenv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API Key:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Add your Groq API key:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage

Run the demo script:
```bash
python test.py
```
