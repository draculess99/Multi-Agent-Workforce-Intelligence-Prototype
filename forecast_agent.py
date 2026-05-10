from crewai import Agent
from dotenv import load_dotenv

load_dotenv()


forecast_agent = Agent(

    role="Warehouse Forecast Analyst",

    goal="""
    Analyze warehouse demand forecasts
    and workforce planning risks.
    """,

    backstory="""
    Expert in warehouse staffing,
    VET/VTO planning,
    and operational forecasting.
    """,

    llm="gpt-4o-mini",

    verbose=True
)