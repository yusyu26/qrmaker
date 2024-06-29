import streamlit as st
import qrcode


#ボタンを右寄せ
st.markdown("""
    <style>
    .stButton button {
        float: right;
    }
    </style>
    """, unsafe_allow_html=True)


#タイトル
st.title('QRメーカー')


#フォームの作製
with st.form(key='profile_form'):   #ボタンが押されたときに画面をリロード
    #テキストボックス
    url = st.text_input('生成したいURLを入力してください:')
    submit_btn = st.form_submit_button('QRコードを生成')
    print(url)


#QRコードの生成
if submit_btn:
    img = qrcode.make(url)
    img = img.convert('RGB')
    st.image(img)
    st.write(url)
