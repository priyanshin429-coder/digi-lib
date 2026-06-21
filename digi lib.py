import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Digital Library Assistant", page_icon="📚", layout="centered")

# 2. App Title and Description
st.title("📚 Digital Library Assistant")
st.subheader("Your one-stop portal for Class X AI & Computer Science course materials.")

# 3. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home & Search", "Study Materials by Topic", "Add to Reading List"])

# 4. Library Data (Books and Materials)
library_data = [
    {"title": "Introduction to Artificial Intelligence", "topic": "AI Basics", "type": "PDF Note"},
    {"title": "Python Programming Guide for Beginners", "topic": "Python", "type": "E-Book"},
    {"title": "Computer Networks and Internet Protocols", "topic": "Computer Science", "type": "Reference"},
    {"title": "Data Science & Machine Learning Foundations", "topic": "AI Advanced", "type": "PDF Note"},
    {"title": "SQL and Database Management Systems", "topic": "Computer Science", "type": "E-Book"}
]

# 5. Page Logic
if page == "Home & Search":
    st.header("🔍 Search Library Materials")
    search_query = st.text_input("Enter book title or keyword:").lower()
    
    st.write("### Available Materials:")
    found = False
    for book in library_data:
        if search_query in book["title"].lower() or search_query in book["topic"].lower():
            with st.expander(f"📖 {book['title']} ({book['type']})"):
                st.write(f"**Topic:** {book['topic']}")
                
                # --- Real Download Button Feature Added Here ---
                file_content = f"Thank you for using the Digital Library!\n\nNotes for: {book['title']}\nTopic: {book['topic']}"
                st.download_button(
                    label="📥 Click here to download file",
                    data=file_content,
                    file_name=f"{book['title']}.txt",
                    mime="text/plain"
                )
                
            found = True
    if not found:
        st.warning("No materials found matching your search.")

elif page == "Study Materials by Topic":
    st.header("🗂️ Browse Materials by Topic")
    topics = list(set(book["topic"] for book in library_data))
    selected_topic = st.selectbox("Select a topic to filter:", topics)
    
    st.write(f"### Materials under '{selected_topic}':")
    for book in library_data:
        if book["topic"] == selected_topic:
            st.info(f"**{book['title']}** — {book['type']}")

elif page == "Add to Reading List":
    st.header("⏳ Interactive Reading Planner")
    st.write("Plan your study goals by adding tasks below:")
    
    if "reading_list" not in st.session_state:
        st.session_state.reading_list = ["Read Chapter 1 of AI Basics", "Practice Python Loops"]
        
    new_task = st.text_input("Enter a new study task or book title:")
    if st.button("Add to Planner"):
        if new_task.strip():
            st.session_state.reading_list.append(new_task.strip())
            st.success(f"Added: '{new_task}'")
        else:
            st.error("Please enter a valid task name.")
            
    st.write("### Your Current Plan:")
    for i, task in enumerate(st.session_state.reading_list, 1):
        st.write(f"{i}. {task}")

# 6. Session Details
# Managing state changes automatically via Streamlit framework

# 7. Footer containing student details
st.markdown("---")
st.caption("Developed by: Kavya Singhal (Roll No. 34) & Priyanshi Nagpal (Roll No. 35) | Session 2026-2027")
