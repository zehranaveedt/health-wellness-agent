# health-wellness-agent
A beginner-friendly AI-powered health planner agent built with the **OpenAI Agents SDK**.  
This smart assistant helps users achieve their health goals by suggesting personalized meal & workout plans, tracking progress, and handing off to specialized agents when needed.

---

## 🚀 Features

✅ Collects and analyzes user fitness/diet goals  
✅ Generates 7-day meal and workout plans  
✅ Tracks weekly progress and schedules check-ins  
✅ Provides handoff to:
- 👨‍⚕️ Injury Support Agent (for injuries)
- 🥗 Nutrition Expert Agent (for complex diets like diabetes)
- 🧑‍🏫 Escalation Agent (to talk to a human)

✅ Real-time chat interaction  
✅ Guardrails to validate input/output  
✅ Modular & easy-to-read codebase

---

## 🗂️ Project Structure

health_wellness_agent/
├── main.py # Starts the agent and runs the loop
├── agent.py # Defines the main Health Planner agent
├── context.py # User session context setup
├── guardrails.py # Input/output validation rules
├── hooks.py # (Optional) lifecycle hooks
├── .env # Stores your OpenAI API key
├── README.md # You're reading it!
│
├── tools/
│ ├── goal_analyzer.py # Extracts structured goals
│ ├── meal_planner.py # Async meal plan tool
│ ├── workout_recommender.py # Workout plan tool
│ ├── scheduler.py # Check-in scheduler
│ └── tracker.py # Progress tracker
│
├── agents/
│ ├── injury_support_agent.py # For injury-based guidance
│ ├── nutrition_expert_agent.py # For complex dietary needs
│ └── escalation_agent.py # Human support
│
├── utils/
│ └── streaming.py # (Optional) streaming helper

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone or download this project
```bash
cd health_wellness_agent
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # for Windows
3. Install dependencies
bash
Copy
Edit
uv pip install -r requirements.txt
If uv not installed, use:

bash
Copy
Edit
pip install -r requirements.txt
4. Add your OpenAI API key
Create a file named .env in the root folder and add this:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
▶️ Run the Agent
CLI version:
bash
Copy
Edit
python main.py
Streamlit (optional UI):
bash
Copy
Edit
streamlit run streamlit_main.py
🧪 Example Conversation
vbnet
Copy
Edit
You: I want to lose 5kg in 2 months  
→ GoalAnalyzerTool will structure this goal

You: I’m vegetarian  
→ MealPlannerTool will stream 7-day veg plan

You: I have knee pain  
→ Automatically handed off to InjurySupportAgent

You: I’m also diabetic  
→ Automatically handed off to NutritionExpertAgent

You: I want a real coach  
→ EscalationAgent will take over
📦 Requirements
Python 3.11+

openai-agents

streamlit

pydantic

python-dotenv

uv (optional, faster pip alternative)

