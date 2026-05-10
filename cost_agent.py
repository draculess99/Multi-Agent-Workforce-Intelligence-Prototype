from crewai import Agent

cost_agent = Agent(
    role="Labor Cost Optimization Analyst",

    goal="""
    Evaluate labor costs,
    overtime exposure,
    staffing efficiency,
    and operational budget concerns.
    """,

    backstory="""
    You are an expert in warehouse labor economics,
    workforce optimization,
    overtime management,
    and fulfillment operational budgeting.
    """,

    llm="gpt-4o-mini",
    
    verbose=True
)