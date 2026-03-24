import streamlit as st

st.set_page_config(page_title="Binary & Hex Lab", page_icon="✂️")

st.title("✂️ The 'Four-Bit Cut' Lab")
st.write("See how your M1 Mac groups 0s and 1s into Hexadecimal.")

# 用户输入原始二进制流
raw_binary = st.text_input("Paste a string of 0s and 1s (e.g., 11100101):", "111001011000100010011000")

# 过滤掉非 0/1 字符
clean_binary = "".join([c for c in raw_binary if c in "01"])

if clean_binary:
    # 1. 自动补齐 (Padding)：为了每 4 位一刀，前面可能需要补 0
    padding_needed = (4 - len(clean_binary) % 4) % 4
    padded_binary = "0" * padding_needed + clean_binary
    
    st.subheader("Step 1: Alignment & Padding")
    st.write(f"Original length: {len(clean_binary)} bits")
    if padding_needed > 0:
        st.warning(f"Added {padding_needed} zero(s) to the front to make it divisible by 4.")
    st.code(padded_binary, language="bash")

    # 2. 四位一刀切
    st.subheader("Step 2: The 'Four-Bit Cut'")
    groups = [padded_binary[i:i+4] for i in range(0, len(padded_binary), 4)]
    
    # 建立一个漂亮的显示界面
    cols = st.columns(len(groups))
    hex_result = "0x"
    
    for i, group in enumerate(groups):
        with cols[i]:
            # 计算这一组的十六进制
            hex_char = hex(int(group, 2))[2:].upper()
            hex_result += hex_char
            
            st.info(f"Group {i+1}")
            st.code(group)
            st.write(f"**→ {hex_char}**")
            
    # 3. 最终结果
    st.success(f"### Final Hexadecimal: `{hex_result}`")
    st.caption("Developed by Liu Wei | Learning the 'Speedy Shorthand' of M1 Architecture")
else:
    st.info("Please enter some binary (0 or 1) to start cutting!")
