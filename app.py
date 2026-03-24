import streamlit as st

st.set_page_config(page_title="Binary & Unicode Explorer", page_icon="🔐")

st.title("🔐 Binary & Unicode Explorer")
st.write("Explore how 'Characters' vs 'Numbers' look inside your M1 Mac.")

text_input = st.text_input("Enter text or a number:")

if text_input:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Character Mode")
        st.write("Each symbol's unique ID (Unicode):")
        for c in text_input:
            code_decimal = ord(c)  # 这就是你要的 21016 和 30332
            st.info(f"Symbol: **{c}**")
            st.write(f"- Decimal ID: `{code_decimal}`")
            st.write(f"- Binary: `{bin(code_decimal)}`")
            st.write(f"- Hex: `{hex(code_decimal)}`")
            st.divider()
            
    with col2:
        st.subheader("2. Numeric Mode")
        if text_input.isdigit():
            num = int(text_input)
            binary_str = bin(num)
            bits_needed = len(binary_str) - 2 
            
            st.write(f"Treating `{text_input}` as a whole integer:")
            st.code(f"Decimal: {num}\nBinary:  {binary_str}\nHex:     {hex(num)}", language="bash")
            
            st.success(f"This is how ({num}) sits in a CPU register!")
            st.metric("Memory Usage", f"{bits_needed} Bits")
        else:
            st.warning("Numeric Mode is only for pure numbers (0-9).")

st.divider()
st.caption("Developed by Liu Wei in Tallinn | Mapping the M1 Architecture")
