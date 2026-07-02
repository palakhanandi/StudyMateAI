def generate_mcq(topic):

    questions = {

        "DSA":

        {

            "question":

            "Which data structure is used in BFS?",

            "options":

            ["Stack", "Queue", "Heap", "Tree"],

            "answer":

            "Queue"

        },

        "DBMS":

        {

            "question":

            "What does SQL stand for?",

            "options":

            [

                "Structured Query Language",

                "Simple Query Language",

                "Sequential Query Language",

                "System Query Language"

            ],

            "answer":

            "Structured Query Language"

        }

    }

    return questions.get(topic, "No quiz found")