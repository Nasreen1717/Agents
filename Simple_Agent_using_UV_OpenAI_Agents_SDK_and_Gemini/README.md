# 🤖 Simple Agent using UV OpenAI Agents SDK & Gemini

A beginner-friendly AI agent project built using [OpenAI's UV Agents SDK](https://github.com/openai/agents) and integrated with **Gemini**, Google's LLM. This simple agent demonstrates how tools and language models can collaborate to solve tasks through reasoning and interaction.

---

## 📁 Folder Structure

```
Simple_Agent_using_UV_OpenAI_Agents_SDK_and_Gemini/
│
├── agent.py            # Core logic to run the agent
├── tool.py             # Custom tool used by the agent
├── requirements.txt    # Required dependencies
└── README.md           # Documentation (this file)
```

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Nasreen1717/Agents.git
cd Agents/Simple_Agent_using_UV_OpenAI_Agents_SDK_and_Gemini
```

### 2. (Optional) Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Agent

```bash
python main.py
```

---

## 🧠 What This Agent Can Do

* 🔧 Use custom tools to perform tasks
* 💬 Interact using Gemini LLM
* 🔄 Loop through reasoning steps to refine results
* 🧹 Easily extendable with new tools and models

---

## 📌 Requirements

* Python 3.8 or above
* Access to Gemini API (Google)
* OpenAI `agents` or `uv` package
* Internet connection (for API calls)

---

## 🔐 API Key Note

Make sure to:

* Store your Gemini API key securely
* Avoid committing secrets to GitHub

Use `.env` or config files for best practices.

---

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

## 🙏 Credits

* [OpenAI Agents SDK](https://github.com/openai/agents)
* [Google Gemini](https://deepmind.google/technologies/gemini)

---

**Start simple. Build smart. Deploy agents.**
