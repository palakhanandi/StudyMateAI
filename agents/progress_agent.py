import json


def progress_agent():

    with open("data/progress.json", "r") as file:

        data = json.load(file)

    result = f"""

Topics Completed : {data['topics_completed']}

Quiz Score : {data['quiz_score']} %

Remaining Syllabus :

{data['remaining_syllabus']} %

"""

    return result