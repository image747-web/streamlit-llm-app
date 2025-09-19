# .envファイルに記載したAPIキーを読み込む
from dotenv import load_dotenv
load_dotenv()


# 必要となるライブラリのインポート
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


# 引数を入力テキストとラジオボタンとする回答生成関数の定義
def generate_answer(input_message, selected_item):
    # OpenAIのAPIキーを環境変数から取得し、ChatOpenAIクラスのインスタンスを生成する。
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    # ラジオボタンの選択に応じてシステムメッセージを切り替える。
    if selected_item == "首都回答の専門家による回答生成":
        system_message = SystemMessage(content="あなたは、世界の首都に関する質問に答える優秀なアシスタントです。")
    else:
        system_message = SystemMessage(content="あなたは、世界の観光地に関する質問に答える優秀なアシスタントです。")
    # ユーザーメッセージを作成する。
    human_message = HumanMessage(content=input_message)
    # システムメッセージとユーザーメッセージをリストにまとめる。
    messages = [system_message, human_message]
    # ChatOpenAIクラスのインスタンスにメッセージを渡して回答を生成する。
    result = llm(messages)
    return result.content


# streamlitによるWebアプリの作成
import streamlit as st
st.title("Lesson21:Chapter 6 【提出課題】LLM機能を搭載したWebアプリを開発しよう")
st.write("##### 動作モード1: 首都回答の専門家モード")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで首都回答の専門家による回答生成できます。")
st.write("##### 動作モード2: 観光地紹介の専門家による回答モード")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで観光地紹介の専門家による回答生成できます。")
selected_item = st.radio(
    "動作モードを選択してください。",
    ["首都回答の専門家による回答生成", "観光地紹介の専門家による回答生成"]
)
st.divider()

# 首都回答の専門家による回答生成モード
if selected_item == "首都回答の専門家による回答生成":
    input_message = st.text_input(label="質問事項を入力してください")
    if st.button("実行(首都回答専門家モード)"):
        if not input_message:
            st.error("質問事項を入力してください")
        else:
            answer=generate_answer(input_message, selected_item)
            st.write(answer)


# 観光地紹介の専門家による回答生成モード
if selected_item == "観光地紹介の専門家による回答生成":
    input_message = st.text_input(label="質問事項を入力してください")
    if st.button("実行(観光地紹介専門家モード)"):
        if not input_message:
            st.error("質問事項を入力してください")
        else:
            answer=generate_answer(input_message, selected_item)
            st.write(answer)