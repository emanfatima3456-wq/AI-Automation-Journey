import streamlit as st
from email_assistant import analyze_email

# Page config
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Email Assistant")
st.subheader("Analyze any email instantly with AI!")
st.divider()

# Input
email_input = st.text_area(
    "📧 Paste your email here:",
    height=150,
    placeholder="Type or paste your email here..."
)

# Button
if st.button("🔍 Analyze Email", use_container_width=True):
    if email_input:
        with st.spinner("🤖 AI is analyzing your email..."):
            result = analyze_email(email_input)

        st.divider()
        st.success("✅ Analysis Complete!")

        # Results
        col1, col2, col3 = st.columns(3)
        col1.metric("📌 Category", result["category"].upper())
        col2.metric("💬 Sentiment", result["sentiment"].upper())
        col3.metric("🚨 Priority", result["priority"].upper())

        st.divider()

        # Reply
        st.subheader("✍️ Suggested Reply:")
        st.info(result["reply"])

    else:
        st.warning("⚠️ Please enter an email first!")
# Footer
st.markdown("""
<div class="footer">
    Built with ❤️ by Eman Fatima | Powered by Cohere AI
</div>
""", unsafe_allow_html=True)