import streamlit as st
import os
from main import graph

st.set_page_config(page_title="AI Search Agent", layout="wide")
st.title("Multi-Source Research Agent")
st.write("Ask any question and get answers from Google, Bing, and Reddit!")

user_input = st.text_input("Ask me anything:", "")

if st.button("Search") and user_input:
    state = {
        "messages": [{"role": "user", "content": user_input}],
        "user_question": user_input,
        "google_results": None,
        "bing_results": None,
        "reddit_results": None,
        "selected_reddit_urls": None,
        "reddit_post_data": None,
        "google_analysis": None,
        "bing_analysis": None,
        "reddit_analysis": None,
        "final_answer": None,
    }
    with st.spinner("Running parallel research..."):
        final_state = graph.invoke(state)
    st.subheader("Final Answer:")
    st.write(final_state.get("final_answer", "No answer found."))
    st.subheader("Google Analysis:")
    st.write(final_state.get("google_analysis", "No analysis."))
    st.subheader("Bing Analysis:")
    st.write(final_state.get("bing_analysis", "No analysis."))
    st.subheader("Reddit Analysis:")
    st.write(final_state.get("reddit_analysis", "No analysis."))
