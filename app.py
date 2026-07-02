import streamlit as st

from main import run_agent
from tools.tracker import get_progress

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------

st.title("📚 StudyMate AI")
st.subheader("Intelligent Multi-Agent Study Buddy")
st.markdown(
    "An AI agent that helps students create study plans, learn concepts, generate quizzes and track progress."
)

st.markdown("---")

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("🤖 Choose Agent")

agent = st.sidebar.selectbox(
    "Select an Agent",
    [
        "Study Planner",
        "Tutor",
        "Quiz",
        "Progress"
    ]
)

# ----------------------------
# Progress Dashboard
# ----------------------------

if agent == "Progress":

    st.header("📈 Progress Dashboard")

    data = get_progress()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Topics Completed",
            data["topics_completed"]
        )

    with col2:
        st.metric(
            "Quiz Score",
            f"{data['quiz_score']}%"
        )

    with col3:
        st.metric(
            "Remaining Syllabus",
            f"{data['remaining_syllabus']}%"
        )

# ----------------------------
# Other Agents
# ----------------------------

else:

    st.header(f"🤖 {agent}")

    examples = {
        "Study Planner":
        """Subjects:
DSA, DBMS, Java

Exam after 30 days

Study Hours:
4 hrs/day""",

        "Tutor":
        """Explain Binary Search with an example""",

        "Quiz":
        """Generate quiz on Trees in DSA"""
    }

    user_input = st.text_area(
        "Enter your query",
        value=examples.get(agent, ""),
        height=180
    )

    if st.button("Generate"):

        if user_input.strip() == "":

            st.warning("Please enter some input.")

        else:

            with st.spinner("Thinking..."):

                result = run_agent(
                    agent,
                    user_input
                )

            st.success("Done!")

            st.markdown("### Output")

            st.write(result)

# ----------------------------
# Footer
# ----------------------------

st.markdown("---")

st.caption(
    "Built using Gemini + Multi-Agent Architecture + Streamlit"
)