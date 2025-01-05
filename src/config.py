from gliner import GLiNER


model = GLiNER.from_pretrained("urchade/gliner_large-v2.1")

# Define labels for resume parsing
RESUME_ENTITY_TYPES = [
    "Person",
    "Email",
    "Phone",
    "Social Links",
    "Hard Skill",
    "Languages",
    "Achievements",
    "Work Experience",
    "Education",
    "Location",
    "Summary",
]
