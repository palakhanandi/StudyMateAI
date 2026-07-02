import json


FILE_PATH = "data/progress.json"


def update_progress(
        topics_completed,
        quiz_score,
        remaining_syllabus):


    data = {

        "topics_completed":

        topics_completed,

        "quiz_score":

        quiz_score,

        "remaining_syllabus":

        remaining_syllabus

    }


    with open(FILE_PATH, "w") as file:

        json.dump(data, file, indent=4)



def get_progress():

    with open(FILE_PATH, "r") as file:

        return json.load(file)