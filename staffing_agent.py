from crewai import Agent

staffing_agent = Agent(
    role="Warehouse Workforce Planner",

    goal="""
    Recommend workforce actions including:
    VET,
    VTO,
    staffing stabilization,
    and operational labor balancing.
    """,

    backstory="""
    You specialize in warehouse staffing strategy,
    labor balancing,
    workforce stabilization,
    and operational labor planning.
    """,


    llm="gpt-4o-mini",

    verbose=True
)