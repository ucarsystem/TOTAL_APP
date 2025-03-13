import streamlit as st
import os
import subprocess

# 기본 경로 설정
BASE_DIR = "TOTAL_APP"

ID_DIR = os.path.join("pages", "id_lookup.py")
DASHBOARD_DIR = os.path.join("pages", "dashboard")

# 대시보드 메뉴
st.sidebar.title("메뉴")
# 모드 선택
mode = st.sidebar.radio("모드를 선택하세요", ["관리자 모드", "운전자 모드"])

if mode == "관리자 모드":
    admin_menu = st.sidebar.radio("관리자 메뉴", ["ID 현황", "운전성향분석표", "개별분석표"])
    if admin_menu == "ID 현황":
        st.title("ID 현황")
        st.write("여기에 ID 현황 데이터 표시")
    elif admin_menu == "운전성향분석표":
        st.title("운전성향분석표")
        st.write("운전성향분석표 데이터 표시")
    elif admin_menu == "개별분석표":
        st.title("개별분석표")
        st.write("개별 분석 데이터 표시")

elif mode == "운전자 모드":
    driver_menu = st.sidebar.radio("운전자 메뉴", ["ID 조회", "내 등급현황 조회"])
    
    if driver_menu == "ID 조회":
        st.title("ID 조회 페이지로 이동 중...")
        st.write("ID 조회 시스템을 실행합니다.")
        with open(ID_DIR, encoding="utf-8") as f:
            code = f.read()
            exec(code)

    
    elif driver_menu == "내 등급현황 조회":
        st.title("내 등급현황 조회 페이지로 이동 중...")
        st.write("등급 현황 시스템을 실행합니다.")
        st.switch_page("pages/grade_status.py")
