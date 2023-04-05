# AI-Triage-Assessment
This project showcases the use of OpenAI's GPT-3 model for medical triage assessment. Given patient information such as age, symptoms, and medical history, the AI provides a triage decision and explanation. The project demonstrates prompt engineering, API integration, and evaluation of AI-generated responses.
# AI Triage System

This project demonstrates an AI-driven patient triage system using OpenAI's GPT-3. The AI triage system assesses the urgency of a patient's medical condition based on their symptoms and medical history.

## Objectives

- Use GPT-3 to generate accurate triage assessments for fictional patients
- Evaluate the performance of the AI model based on its triage recommendations
- Share the methodology, prompt architecture, and results of the project

## Methodology

1. Created a dataset of 10 fictional patients with varying symptoms and medical histories
2. Designed a prompt architecture to effectively communicate patient information to GPT-3
3. Queried GPT-3 for triage assessments and recommendations
4. Collected and analyzed AI-generated responses for each patient
5. Evaluated the performance of the AI model by comparing its assessments to expert opinions

## Prompt Architecture

The prompt architecture for this project is designed to provide clear and concise information about each patient. An example of the prompt structure is as follows:

Patient Name: {name}
Age: {age}
Symptoms: {symptoms}
Medical History: {medical_history}

Please triage this patient and provide a brief explanation for your decision. Consider the patient's symptoms and medical history in your assessment.

## Results

The AI triage system successfully generated assessments for each of the 10 patients in the dataset. The assessments were clear and concise, with recommendations that were largely consistent with expert opinions. To further evaluate the performance of the AI model, consider consulting a medical expert to review the generated assessments and provide feedback.

## Performance Metrics

- [Include any relevant performance metrics, such as the percentage of correct assessments or patterns in the AI's mistakes]

## Code Snippets

- [Include relevant code snippets to showcase specific parts of the project, such as prompt generation, querying GPT-3, or handling responses]

## Dependencies

- openai
- Python 3.6 or higher

## Usage

1. Clone the repository
2. Install the dependencies: `pip install -r requirements.txt`
3. Set your OpenAI API key as an environment variable: `export OPENAI_API_KEY="your_api_key"`
4. Run the script: `python triage_ai.py`
5. Review the AI-generated triage assessments

## License

MIT License

Copyright (c) [2023] [Daton Pope]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

