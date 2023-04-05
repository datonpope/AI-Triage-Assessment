import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

patients = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 32,
        "symptoms": [
            "fever",
            "cough",
            "shortness of breath",
            "loss of taste and smell"
        ],
        "medical_history": [
            "asthma",
            "seasonal allergies"
        ],
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 28,
        "symptoms": [
            "fatigue",
            "headache",
            "sore throat",
            "congestion"
        ],
        "medical_history": [
            "type 2 diabetes",
            "high blood pressure"
        ],
    },
    {
        "id": 3,
        "name": "Alice Johnson",
        "age": 45,
        "symptoms": [
            "chest pain",
            "irregular heartbeat",
            "dizziness",
            "nausea"
        ],
        "medical_history": [
            "previous heart attack",
            "smoker"
        ],
    },
    {
        "id": 4,
        "name": "Bob Brown",
        "age": 40,
        "symptoms": [
            "abdominal pain",
            "vomiting",
            "diarrhea",
            "dehydration"
        ],
        "medical_history": [
            "irritable bowel syndrome",
            "lactose intolerance"
        ],
    },
    {
        "id": 5,
        "name": "Charlie Green",
        "age": 60,
        "symptoms": [
            "severe headache",
            "stiff neck",
            "fever",
            "sensitivity to light"
        ],
        "medical_history": [
            "migraines",
            "family history of meningitis"
        ],
    },
    {
        "id": 6,
        "name": "Eva White",
        "age": 23,
        "symptoms": [
            "swollen joints",
            "morning stiffness",
            "fatigue",
            "low-grade fever"
        ],
        "medical_history": [
            "rheumatoid arthritis",
            "family history of autoimmune disorders"
        ],
    },
    {
        "id": 7,
        "name": "Frank Black",
        "age": 35,
        "symptoms": [
            "muscle weakness",
            "difficulty swallowing",
            "slurred speech",
            "muscle cramps"
        ],
        "medical_history": [
            "family history of ALS",
            "smoker"
        ],
    },
    {
        "id": 8,
        "name": "Grace Gray",
        "age": 55,
        "symptoms": [
            "memory loss",
            "difficulty concentrating",
            "trouble finding words",
            "mood changes"
        ],
        "medical_history": [
            "family history of Alzheimer's disease",
            "previous head injury"
        ],
    },
    {
        "id": 9,
        "name": "Hank Blue",
        "age": 50,
        "symptoms": [
            "persistent cough",
            "chest pain",
            "weight loss",
            "coughing up blood"
        ],
        "medical_history": [
            "smoker",
            "previous pneumonia diagnosis"
        ],
    },
    {
        "id": 10,
        "name": "Ivy Red",
        "age": 27,
        "symptoms": [
            "intense itching",
            "red or brown rash",
            "small, raised bumps",
            "blistering"
        ],
        "medical_history": [
            "eczema",
            "family history of psoriasis"
        ],
    },
]

def generate_prompt(patient, template):

    return template.format(
        name=patient["name"],
        age=patient["age"],
        symptoms=", ".join(patient["symptoms"]),
        medical_history=", ".join(patient["medical_history"])
    )


prompt_template = """Patient Name: {name}
Age: {age}
Symptoms: {symptoms}
Medical History: {medical_history}

Please triage this patient and provide a brief explanation for your decision. Consider the patient's symptoms and medical history in your assessment."""

prompts = [generate_prompt(patient, prompt_template) for patient in patients]


def query_ai(prompt, model="text-davinci-002", max_tokens=100):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()


openai.api_key = api_key
responses = [query_ai(prompt) for prompt in prompts]

print(responses)
