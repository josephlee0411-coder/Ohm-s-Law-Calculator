import streamlit as st

st.title("⚡ Circuit Calculator")

menu = st.sidebar.selectbox(
    "메뉴 선택",
    ["옴의 법칙", "직렬 저항", "병렬 저항"]
)

# 옴의 법칙
if menu == "옴의 법칙":
    st.header("옴의 법칙 계산기")

    V = st.text_input("전압 V (Volt)")
    I = st.text_input("전류 I (Ampere)")
    R = st.text_input("저항 R (Ohm)")

    if st.button("계산"):
        try:
            if V and I:
                st.success(f"저항 R = {float(V)/float(I)} Ω")
            elif V and R:
                st.success(f"전류 I = {float(V)/float(R)} A")
            elif I and R:
                st.success(f"전압 V = {float(I)*float(R)} V")
            else:
                st.warning("두 개의 값을 입력하세요.")
        except:
            st.error("입력 오류")

# 직렬 저항
elif menu == "직렬 저항":
    st.header("직렬 저항 계산")

    values = st.text_input("저항값들 (쉼표로 구분)")

    if st.button("계산"):
        try:
            nums = list(map(float, values.split(',')))
            st.success(f"총 저항 = {sum(nums)} Ω")
        except:
            st.error("입력 오류")

# 병렬 저항
elif menu == "병렬 저항":
    st.header("병렬 저항 계산")

    values = st.text_input("저항값들 (쉼표로 구분)")

    if st.button("계산"):
        try:
            nums = list(map(float, values.split(',')))
            inv = sum(1/x for x in nums)
            st.success(f"총 저항 = {1/inv} Ω")
        except:
            st.error("입력 오류")
