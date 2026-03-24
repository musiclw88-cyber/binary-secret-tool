import streamlit as st

st.title("🎨 RGB Bitwise Color Lab")
st.write("Synthesize colors using Shifts and Masks like a GPU.")

# 1. 输入三个通道
col_r, col_g, col_b = st.columns(3)
with col_r:
    r = st.slider("Red", 0, 255, 210)
with col_g:
    g = st.slider("Green", 0, 255, 100)
with col_b:
    b = st.slider("Blue", 0, 255, 50)

# 2. 位运算合成
# (R << 16) 把红色推到最前面
# (G << 8) 把绿色推到中间
# | (OR) 把它们合并
combined = (r << 16) | (g << 8) | b

st.divider()

# 3. 展示结果
hex_color = f"#{combined:06X}"
st.subheader(f"Final Hex Code: `{hex_color}`")

# 用这个颜色画一个方块
st.markdown(
    f'<div style="background-color:{hex_color}; width:100%; height:100px; border-radius:10px; border:2px solid white;"></div>',
    unsafe_allow_html=True
)

# 4. 展示底层的二进制结构
st.write("### The 24-bit Structure inside Memory:")
binary_str = bin(combined)[2:].zfill(24)
r_bin = binary_str[0:8]
g_bin = binary_str[8:16]
b_bin = binary_str[16:24]

st.code(f"RED:   {r_bin}\nGREEN: {g_bin}\nBLUE:  {b_bin}", language="bash")
st.info(f"The CPU sees this as one big integer: {combined}")
