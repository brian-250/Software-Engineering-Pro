# openAI library is imported
import openai
# gradio library is imported
import gradio

# Insert your openAI api key within the quotation marks
openai.api_key = ""

# messages list is defined with an initial element
# initial element is a dictionary in the messages list
# initial element communicates to the model what type of responses it should provide
messages = [{"role": "system", "content": "You are a software engineering expert."}]

def CustomChatGPT(user_input):

    # Messages from the user are added to the messages list as a dictionary element
    messages.append({"role": "user", "content": user_input})

    # A response is generated from the model by calling the openAI ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        # The model being used to generate a response is the gpt-3.5-turbo
        model = "gpt-3.5-turbo",
        # The messages list is added as a parameter so the model can generate a response based on all the conversation history
        messages = messages
    )
    # The generated response from the model is stored in ChatGPT_reply
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    # The model's generated reponse is added to the messages list as a dictionary element
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    # The model's response that is stored in ChatGPT_reply is returned to the user
    return ChatGPT_reply

# demo object is created from the gradio.Interface class with parameters to generate a user interface
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Software Engineering Pro")
