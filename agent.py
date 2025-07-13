# 👉 Yeh main agent define karta hai with tools and handoffs

from openai_agents.core.agent import Agent
from tools.goal_analyzer import analyze_goal
from tools.meal_planner import meal_planner
from tools.workout_recommender import workout_recommender
from tools.scheduler import schedule_checkins
from tools.tracker import track_progress

from agents.injury_support_agent import injury_support_agent
from agents.nutrition_expert_agent import nutrition_expert_agent
from agents.escalation_agent import escalation_agent

# Main agent bana rahy hain
main_agent = Agent(
    name="Health Planner",
    instructions="Aap ek AI wellness assistant hain. User ke goals ko samjhyen aur tools use kar k plan banaiye.",
    tools=[analyze_goal, meal_planner, workout_recommender, schedule_checkins, track_progress],
    handoffs={
        "injury_support": injury_support_agent,
        "nutrition_expert": nutrition_expert_agent,
        "escalation": escalation_agent
    }
)
