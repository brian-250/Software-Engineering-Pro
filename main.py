# openAI library is imported
import openai
# gradio library is imported
import gradio

# Insert your openAI api key within the quotation marks
openai.api_key = ""

# messages list is defined with an initial element
# initial element is a dictionary in a the messages list
# initial element communicates to the model what type of responses it should provide
messages = [{"role": "system", "content": "You are a software engineering expert."}]
