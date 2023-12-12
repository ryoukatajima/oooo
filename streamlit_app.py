import streamlit as st

# タイトルを追加
st.title('朝ごはんを決める')

# 朝食の選択肢
options = ['トースト', 'シリアル', 'ヨーグルト', 'フルーツ', 'オムレツ', 'パンケーキ', 'ベーコン＆エッグ']

# 選択肢から朝食を選ぶ
selected_option = st.selectbox('今日の朝ごはんは？', options)

# 選択された朝食を表示
st.write('選ばれた朝ごはん:', selected_option)