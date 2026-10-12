# day32_basic_sol.py
# 주제 :
# python streamlit run day32_basic_sol.py


import psycopg
import streamlit as st
from day32_basic_logic import cal_shipping_fee
from day32_basic_db import save_basic, get_basic, list_basic


def main():
    try:
        st.title('day32_basic')
        if 'id' not in st.session_state:
            st.session_state.id = None
        if 'cal_result' not in st.session_state:
            st.session_state.cal_result = []
        if 'weight' not in st.session_state:
            st.session_state.weight = []


        with st.form('입력'):
            label = st.text_input(
                '견적 제목',
                placeholder= '제목을 입력하세요',
                max_chars = 80
            )
            if label is None:
                st.error('제목이 공백입니다')

            weights = st.number_input(
                '무게',
                min_value = 1,
                max_value = 20000,
                step = 1
            )
            submitted = st.form_submit_button('저장')
            cal_result = cal_shipping_fee(weights)
            if submitted:
                st.success('저장되었습니다')
            cal_fee = st.session_state.cal_result.append(cal_result)
            rows = list_basic(weights)
            st.dataframe({
                'ID': [x['id'] for x in rows],
                '요금': [cal_fee]
            })
    except psycopg.Error:
        st.error('DB연결을 확인하세요')



if __name__ == '__main__':
    main()













































































