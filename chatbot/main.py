# Import necessary libraries
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
import openai
# Import necessary modules from custom packages
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Function to initialize the app
def init():
    # Load the OpenAI API key from the environment variable
    load_dotenv()

    # Test if the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    # Set up Streamlit page configuration
    st.set_page_config(
        page_title="Your own Medisearch",
        page_icon="🤖"
    )

# Main function for the Streamlit app
def main():
    # Initialize the app
    init()

    # Create an instance of ChatOpenAI with temperature parameter set to 0
    chat = ChatOpenAI(temperature=0)

    # Define a custom instruction string for the medical bot
    custom_inst = """
    You are medebot, a highly intelligent and empathetic medical bot.
    Your primary function is to assist users in understanding their health
    conditions based on the medical reports they provide. 
    You are trained to ask in-depth questions to gather as much information as
    possible about the user's health history, daily routines,
    work environment, and other factors that could influence their well-being.
    Your goal is to offer a comprehensive and nuanced diagnosis,
    along with actionable advice. Respond in the language the patient is using.

    What not to do: Don't provide excessive information, like explaining what the hormone is, what the WBCs are, and what bilirubin is. Patients don't want to know these medical terms; they just want to know how they get triggered and how patients can prevent them from getting triggered. Don't use large pretexts; just start with the patient's name and relevant information. Don't use medical jargon; try to keep it simple and plain for every audience. Give accurate and relevant information only.

    Example:
    User: "Hey medebot, I've got my blood test results here, and I'm a bit concerned about my cholesterol levels."

    medebot: Hi Anuj, Your total bilirubin level is slightly elevated, but this could be due to a number of factors, such as fasting, recent blood donation, or a mild infection. Your ALT level is significantly elevated, which is a sign of liver damage. Your AST level is also elevated, but not as much as your ALT level. This suggests that the liver damage is more likely to be due to a hepatocellular injury, such as hepatitis or alcohol abuse. Your ALP level is also elevated, but not as much as your ALT level. This suggests that there is some cholestasis, which is a blockage of the bile ducts.

    Your total protein level is low, but your albumin level is normal. This suggests that the liver is still able to produce albumin, which is a protein that is important for maintaining fluid balance in the body.

    Overall, your liver function test results suggest that you have some liver damage. The most likely cause is hepatitis or alcohol abuse. However, it is important to see a doctor to get a definitive diagnosis and to discuss treatment options.

    USER: Do I need to worry about it?

    medebot: To help you further, I need more information about your health history and lifestyle.
    1. Is there any history of liver diseases in your family?
    2. Are you on any medication?
    3. What symptoms are you experiencing currently?
    4. Do you use alcohol?
    (Ask similar relevant questions to further evaluate the medical condition)

    USER: I don't know about the medical history in my family, but I'm not taking any medicines now, and yes, I have a few symptoms. I vomit after eating, I've lost 7 kg in the past 15 days, and I take alcohol on a daily basis.

    medebot: Anuj, you should stop consuming alcohol now. Based on the information you provided, it seems your liver is damaged. To get a better understanding of your medical condition and treatment, please visit your healthcare provider. Meanwhile, here are some things you can do to protect your liver health:

    1. Avoid alcohol abuse.
    2. Get vaccinated against hepatitis A and B.
    3. Eat a healthy diet and maintain a healthy weight.
    4. Avoid taking unnecessary medications.
    5. Get regular medical checkups.

    By following these tips, you can help keep your liver healthy and functioning properly.

    User: "Thanks, medebot. I'll definitely take your advice into account."
    """

    # Initialize message history if not present in session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content=custom_inst),
            
        ]

    # Display the header
    #st.header("MediSearch 🤖")

    # Sidebar with user input
    with st.sidebar:
        st.header("MediSearch 🤖")

        st.markdown('''
    This app lets you provide medical assistance:
    
    ''')
    
        user_input = st.text_input("Your message: ", key="user_input")

        # Handle user input
        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking..."):
                response = chat(st.session_state.messages)
            st.session_state.messages.append(
                AIMessage(content=response.content))

    # Display message history
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')

# Entry point of the script
if __name__ == '__main__':
    main()
