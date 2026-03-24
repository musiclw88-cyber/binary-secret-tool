import streamlit as st
import numpy as np

# --- 页面配置 ---
st.set_page_config(
    page_title="M1 Architecture Explorer",
    page_icon="💻",
    layout="wide"
)

# --- 侧边栏导航 ---
st.sidebar.title("🚀 Navigation")
app_mode = st.sidebar.radio(
    "Choose a Lab:",
    ["1. Character & Bit-Shift", "2. Four-Bit Cut (Hex)", "3. Bitmask Shield", "4. RGB Color Lab", "5. Audio Binary Lab"]
)

st.sidebar.divider()
st.sidebar.info(f"Developed by Liu Wei | Tallinn, Estonia\nTarget: M1 Architecture Study")

# --- 1. 字符与位移实验室 ---
if app_mode == "1. Character & Bit-Shift":
    st.title("🔠 Character & Bit-Shift Lab")
    st.write("See how Unicode characters turn into shifted binary.")
    
    text_input = st.text_input("Enter text (try '刘' or 'Š'):", "刘")
    
    if text_input:
        cols = st.columns(len(text_input) if len(text_input) < 4 else 4)
        for i, c in enumerate(text_input[:4]): # 最多显示前4个字符
            with cols[i]:
                code = ord(c)
                st.metric(f"Symbol: {c}", f"ID: {code}")
                st.write("**Shift Left (<<1):**")
                st.code(bin(code << 1))
                st.write("**Shift Right (>>1):**")
                st.code(bin(code >> 1))

# --- 2. 四位一刀实验室 ---
elif app_mode == "2. Four-Bit Cut (Hex)":
    st.title("✂️ The 'Four-Bit Cut' (Hex) Lab")
    st.write("Convert raw binary into clean Hexadecimal shorthand.")
    
    raw_bin = st.text_input("Enter Binary (0s and 1s):", "111001011000100010011000")
    clean_bin = "".join([c for c in raw_bin if c in "01"])
    
    if clean_bin:
        padding = (4 - len(clean_bin) % 4) % 4
        padded = "0" * padding + clean_bin
        groups = [padded[i:i+4] for i in range(0, len(padded), 4)]
        
        st.write(f"Padded Binary: `{padded}`")
        hex_display = "0x"
        cols = st.columns(len(groups))
        for i, g in enumerate(groups):
            h = hex(int(g, 2))[2:].upper()
            hex_display += h
            cols[i].code(f"{g}\n↓\n{h}")
        st.success(f"Final Hex: `{hex_display}`")

# --- 3. 位掩码盾牌 ---
elif app_mode == "3. Bitmask Shield":
    st.title("🛡️ The Bitmask Shield (AND Logic)")
    st.write("Use 0xF0 or 0x0F to filter data bits.")
    
    c1, c2 = st.columns(2)
    val_hex = c1.text_input("Data (Hex):", "0xB5")
    mask_hex = c2.text_input("Mask (Hex):", "0xF0")
    
    try:
        v, m = int(val_hex, 16), int(mask_hex, 16)
        res = v & m
        st.divider()
        st.write(f"Data: `{bin(v)}`")
        st.write(f"Mask: `{bin(m)}`")
        st.success(f"Result: `{bin(res)}` (Hex: {hex(res)})")
    except: st.error("Invalid Hex")

# --- 4. RGB 颜色实验室 ---
elif app_mode == "4. RGB Color Lab":
    st.title("🎨 RGB Bitwise Color Lab")
    r = st.slider("Red", 0, 255, 229)
    g = st.slider("Green", 0, 255, 136)
    b = st.slider("Blue", 0, 255, 152)
    
    combined = (r << 16) | (g << 8) | b
    hex_c = f"#{combined:06X}"
    
    st.markdown(f'<div style="background-color:{hex_c};height:100px;border-radius:10px;"></div>', unsafe_allow_html=True)
    st.write(f"Hex Code: `{hex_c}` | Integer: `{combined}`")
    st.code(f"Binary: {bin(combined).zfill(24)}")

# --- 5. 音频二进制实验室 ---
elif app_mode == "5. Audio Binary Lab":
    st.title("🎵 Audio Binary Lab")
    freq = st.select_slider("Tone Frequency (Hz)", options=[262, 294, 330, 349, 392, 440, 494], value=440)
    t = np.linspace(0, 0.01, 100)
    wave = (np.sin(2 * np.pi * freq * t) * 32767).astype(np.int16)
    
    st.line_chart(wave)
    idx = st.slider("Sample Index", 0, 99, 50)
    val = int(wave[idx])
    st.write(f"Sample Value: `{val}` | 16-bit Binary: `{bin(val & 0xFFFF)}`")

st.divider()
st.caption("© 2026 M1 Architecture Explorer | Built with Streamlit & Passion")
