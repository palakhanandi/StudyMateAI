from agents.planner_agent import planner_agent
from agents.tutor_agent import tutor_agent
from agents.quiz_agent import quiz_agent
from agents.progress_agent import progress_agent


def run_agent(task_type, user_input=""):

    if task_type == "Study Planner":
        return planner_agent(user_input)

    elif task_type == "Tutor":
        return tutor_agent(user_input)

    elif task_type == "Quiz":
        return quiz_agent(user_input)

    elif task_type == "Progress":
        return progress_agent()

    else:
        return "Invalid Agent Selected"