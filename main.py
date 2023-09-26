#from dotenv import load_dotenv
#load_dotenv()
from langchain.chat_models import ChatOpenAI
import streamlit as st
from PIL import Image


# # 줄글 생성
# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 책은")
# print(result)

#대화형 인공지능
chat_model = ChatOpenAI()
st.title('모든 생물학의 신')
image = Image.open('god-frog.jpg')
st.header('모르는게 있으면 나에게 물어보거라')
st.image(image)
content = st.text_input('여쭤보기')


if st.button('생물학의 신께 여쭤보기'):
    with st.spinner(text='신께서 고민중...'):
        result = chat_model.predict("생물학, 생명공학을 50년간 공부한 전문가라고 가정하고 다음 질문에 답해주세요. 답변은 마치 신이 인간에게 답변하듯 해주세요."+content)
        st.write(result)
