from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage
# Later we will replace this with MongoDB
student_profiles = []

CAREERS = {
    "python": {
        "career": "Python Developer",
        "skills": ["Python", "OOP", "Git", "APIs", "SQL"],
        "steps": [
            "Strengthen Python and object-oriented programming.",
            "Build 2-3 Python projects.",
            "Learn REST APIs and SQL.",
            "Create a GitHub portfolio.",
            "Apply for Python internships."
        ]
    },

    "machine learning": {
        "career": "Machine Learning Engineer",
        "skills": ["Python", "NumPy", "Pandas", "Scikit-learn", "SQL"],
        "steps": [
            "Learn Python for data science.",
            "Practice NumPy and Pandas.",
            "Learn supervised and unsupervised learning.",
            "Build and deploy ML projects.",
            "Apply for ML or data internships."
        ]
    },

    "ai": {
        "career": "AI Engineer",
        "skills": ["Python", "Machine Learning", "APIs", "LLMs", "RAG"],
        "steps": [
            "Strengthen Python and machine learning.",
            "Learn how APIs and LLMs work.",
            "Build small AI applications.",
            "Learn prompt engineering and RAG.",
            "Deploy an AI project."
        ]
    },

    "web": {
        "career": "Web Developer",
        "skills": ["HTML", "CSS", "JavaScript", "Flask", "Git"],
        "steps": [
            "Learn HTML and CSS.",
            "Learn JavaScript and DOM manipulation.",
            "Build Flask web applications.",
            "Learn databases and APIs.",
            "Deploy a complete web project."
        ]
    },

    "data": {
        "career": "Data Analyst",
        "skills": ["Python", "Pandas", "SQL", "Excel", "Data Visualization"],
        "steps": [
            "Learn Excel and SQL.",
            "Practice Python with Pandas.",
            "Learn data cleaning and EDA.",
            "Create dashboards and visualizations.",
            "Build a data analytics portfolio."
        ]
    },

    "cyber": {
        "career": "Cybersecurity Analyst",
        "skills": ["Networking", "Linux", "Python", "Security Basics"],
        "steps": [
            "Learn computer networking.",
            "Learn Linux fundamentals.",
            "Study cybersecurity fundamentals.",
            "Practice with safe cybersecurity labs.",
            "Build a cybersecurity portfolio."
        ]
    }
}


def generate_guidance(skills, interests, career_goal):

    text = f"{skills} {interests} {career_goal}".lower()

    if "machine learning" in text or "ml" in text:
        key = "machine learning"

    elif "cyber" in text or "security" in text:
        key = "cyber"

    elif "data" in text or "sql" in text:
        key = "data"

    elif "web" in text or "html" in text or "javascript" in text:
        key = "web"

    elif "ai" in text or "artificial intelligence" in text:
        key = "ai"

    else:
        key = "python"

    return CAREERS[key]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():

    if request.method == "POST":

        profile_data = {
            "name": request.form.get("name"),
            "education": request.form.get("education"),
            "skills": request.form.get("skills"),
            "interests": request.form.get("interests"),
            "career_goal": request.form.get("career_goal")
        }

        profile_data["guidance"] = generate_guidance(
            profile_data["skills"],
            profile_data["interests"],
            profile_data["career_goal"]
        )

        student_profiles.append(profile_data)

        return redirect(
            url_for(
                "guidance",
                student_id=len(student_profiles) - 1
            )
        )

    return render_template("profile.html")


@app.route("/guidance/<int:student_id>")
def guidance(student_id):

    if student_id < 0 or student_id >= len(student_profiles):
        return "Student profile not found", 404

    student = student_profiles[student_id]

    return render_template(
        "guidance.html",
        student=student
    )


@app.route("/counselor")
def counselor():

    return render_template(
        "counselor.html",
        students=student_profiles
    )


if __name__ == "__main__":
    app.run(debug=True)