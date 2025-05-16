import re

def process_input(user_input):
    data = {
        "name": None,
        "degree": None,
        "major": None,
        "university": None,
        "bachelor_degree": None,
        "bachelor_major": None,
        "bachelor_university": None,
        "experiences": [],
        "projects": [],
        "skills": [],
        "age": None,
        "gender": None,
        "birthday": None,
        "location": None,
    }
    # Naive name extraction if input starts with "My name is ..." or "I'm ..."
    # Name extraction: match "my name is", "I am", or "I'm"
    name_match = re.search(r"\b(?:my name is|i am|i'm)\s+([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)", user_input, re.IGNORECASE)
    if name_match:
        data["name"] = name_match.group(1).strip().title()


    # Degree & Major (Master's)
    if "master" in user_input.lower():
        match = re.search(r"master.*?in ([\w\s]+)", user_input, re.IGNORECASE)
        if match:
            data["degree"] = "Master's"
            data["major"] = match.group(1).strip()
    
    # Degree & Major (Bachelor's)
    if "bachelor" in user_input.lower():
        match = re.search(r"bachelor.*?in ([\w\s]+)", user_input, re.IGNORECASE)
        if match:
            data["bachelor_degree"] = "Bachelor's"
            data["bachelor_major"] = match.group(1).strip()
    gender_match = re.search(r"\b(male|female|non-binary|man|woman)\b", user_input, re.IGNORECASE)
    if gender_match:
        data["gender"] = gender_match.group(1).capitalize()

# Age
    age_match = re.search(r"\b(\d{1,2})\s*years old\b", user_input, re.IGNORECASE)
    if age_match:
        data["age"] = age_match.group(1)

# Birthday
    bday_match = re.search(r"\bborn on (\w+ \d{1,2}, \d{4})\b", user_input, re.IGNORECASE)
    if bday_match:
        data["birthday"] = bday_match.group(1)

# Location
    loc_match = re.search(r"\bfrom ([A-Za-z ,]+)", user_input, re.IGNORECASE)
    if loc_match:
         data["location"] = loc_match.group(1).strip()
    # University detection
    unis = ["Columbia University", "Harvard", "MIT", "Stanford", "UCBerkeley", "UCDavis"]
    for uni in unis:
        if uni.lower() in user_input.lower():
            if uni == "Columbia University":
                data["university"] = "Columbia University"
            elif uni == "Harvard":
                data["university"] = "Harvard University"
            elif uni == "MIT":
                data["university"] = "Massachusetts Institute of Technology"
            elif uni == "Stanford":
                data["university"] = "Stanford University"
            elif uni == "UCBerkeley":
                data["university"] = "UC Berkeley"
            elif uni == "UCDavis":
                data["university"] = "UC Davis"

    # Experience extraction
    exp_match = re.findall(r"(interned at .+?[\.!?])", user_input, re.IGNORECASE)
    for match in exp_match:
        data["experiences"].append(match.strip())
    
    project_match = re.findall(r"(worked on|developed|built|created) .*?project.*?[\.]", user_input, re.IGNORECASE)
    for match in project_match:
        data["projects"].append(match.strip())
    # Skills extraction
    skills_match = re.search(r"skills? in ([\w\s,]+)", user_input, re.IGNORECASE)
    if skills_match:
        skills_str = skills_match.group(1)
        skills_list = [s.strip() for s in skills_str.split(",")]
        data["skills"] = skills_list

    return data

def build_structured_data(form_data):
    """
    Accepts dictionary-style structured input and returns the same format as process_input().
    """
    data = {
        "name": form_data.get("name"),
        "age": form_data.get("age"),
        "gender": form_data.get("gender"),
        "birthday": form_data.get("birthday"),
        "location": form_data.get("location"),
        "degree": form_data.get("degree"),
        "major": form_data.get("major"),
        "university": form_data.get("university"),
        "bachelor_degree": form_data.get("bachelor_degree"),
        "bachelor_major": form_data.get("bachelor_major"),
        "bachelor_university": form_data.get("bachelor_university"),
        "experiences": form_data.get("experiences", []),
        "projects": form_data.get("projects", []),
        "skills": form_data.get("skills", []),
    }
    return data
