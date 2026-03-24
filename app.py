import streamlit as st
import numpy as np

st.title("🎵 Audio Binary Lab")
st.write("See how sound waves are sliced into 0s and 1s.")

# 1. 调整频率（音调）
freq = st.slider("Frequency (Hz)", 100, 1000, 440) # 440Hz 是标准音 A

# 2. 生成 100 个采样点（极短的一瞬间）
t = np.linspace(0, 0.01, 100)
# 将波形映射到 16 位整数范围 (-32768 到 32767)
waveform = (np.sin(2 * np.pi * freq * t) * 32767).astype(np.int16)

# 3. 画出波形图
st.line_chart(waveform)

# 4. 抽取其中一个点，看它的二进制
sample_idx = st.number_input("Select a sample point to inspect:", 0, 99, 50)
sample_val = int(waveform[sample_idx])

col1, col2 = st.columns(2)
with col1:
    st.metric("Decimal Value", sample_val)
with col2:
    # 处理负数的二进制显示 (使用 16 位掩码)
    st.write("16-bit Binary:")
    st.code(bin(sample_val & 0xFFFF), language="bash")

st.info("When you play music, your M1 chip processes millions of these bits every second!")
