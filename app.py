import streamlit as st

# 页面设置
st.set_page_config(page_title="Binary & Unicode Explorer", page_icon="🔐")

st.title("🔐 Binary & Unicode Explorer")
st.write("Discover how your name looks inside the memory of an M1 chip.")

# 使用 Tabs 让界面更整洁
tab1, tab2 = st.tabs(["Encode (Text to 0101)", "Decode (0101 to Text)"])

with tab1:
    text_input = st.text_input("Enter text (English, Chinese, or Estonian):", "刘炜")
    if text_input:
        # 获取二进制 (Binary)
        binary_output = " ".join([bin(ord(c)) for c in text_input])
        # 获取十六进制 (Hex)
        hex_output = " ".join([hex(ord(c)) for c in text_input])
        # 计算字节数 (Bytes) - UTF-8 编码下汉字通常占 3 字节
        byte_count = len(text_input.encode('utf-8'))
        
        st.subheader("Results:")
        st.write("**Binary (0b...):**")
        st.code(binary_output, language="bash")
        
        st.write("**Hexadecimal (0x...):**")
        st.code(hex_output, language="bash")
        
        st.info(f"💡 Memory Tip: '{text_input}' takes up **{byte_count} bytes** in UTF-8 memory.")

with tab2:
    binary_input = st.text_area("Paste binary code (starting with 0b, separated by spaces):")
    if st.button("Decode Now"):
        try:
            decoded_text = "".join([chr(int(b, 2)) for b in binary_input.split()])
            st.success(f"Decoded Text: **{decoded_text}**")
        except:
            st.error("Format Error! Make sure it looks like '0b10101... 0b1100...'")

st.divider()
st.caption("Built in Tallinn | Exploring Computer Architecture")
