import streamlit as st

st.set_page_config(page_title="Binary & Unicode Explorer", page_icon="🔐")

st.title("🔐 Binary & Unicode Explorer")
st.write("Explore how 'Characters' vs 'Numbers' look inside your M1 Mac.")

text_input = st.text_input("Enter text or a number:", "19")

if text_input:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Character Mode")
        st.write("Treating each symbol individually (Unicode/ASCII):")
        for c in text_input:
            st.write(f"Symbol: `{c}` → Binary: `{bin(ord(c))}`")
            
    with col2:
        st.subheader("2. Numeric Mode")
        if text_input.isdigit():
            num = int(text_input)
            st.write(f"Treating `{text_input}` as a whole number:")
            st.code(f"Decimal: {num}\nBinary:  {bin(num)}\nHex:     {hex(num)}", language="bash")
            st.success(f"This is how (num) sits in a CPU register!")
        else:
            st.info("Enter a pure number (like 19) to see the Numeric Mode.")

st.divider()
st.caption("Developed by Liu Wei | Learning Logic Gates & M1 Architecture")
