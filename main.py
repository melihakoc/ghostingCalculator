import streamlit as st

def calculate_ghosting_probability(response_time, online_no_reply, excuse, watched_story,
                                   watched_reels, sent_reels, likes_stories, bad_influence_trip, relationship_status):
    score = 0

    if response_time == "More than a day":
        score += 30
    elif response_time == "A few hours":
        score += 10

    if online_no_reply == "Yes":
        score += 40

    if excuse == "Yes, frequently":
        score += 20

    if watched_story == "Yes":
        score += 20

    if watched_reels == "No":
        score += 15

    if sent_reels in ["More than a week ago", "N/A"]:
        score += 25

    if likes_stories == "No":
        score += 15

    if bad_influence_trip == "Yes":
        score += 30

    if relationship_status == "Situationship":
        score += 25
    elif relationship_status == "Flirt":
        score += 15

    ghosting_probability = min(score, 100)
    
    result_message = f"**Ghosting Probability: {ghosting_probability}%**\n\n"
    if ghosting_probability < 30:
        result_message += "✅ You're probably safe! 🫡"
    elif ghosting_probability < 60:
        result_message += "⚠️ Might be losing interest... 😬"
    else:
        result_message += "💀 They're definitely ghosting you."
    
    return result_message

# Streamlit UI
st.title("Are They Ghosting Me? 💔")
st.markdown("A simple tool to check your ghosting probability!")

# Collect user input
response_time = st.selectbox("How long has it been since they last replied?", 
                             ["Less than an hour", "A few hours", "More than a day"])

online_no_reply = st.selectbox("Are they online but not responding?", ["No", "Yes"])

excuse = st.selectbox("Have they made excuses for not meeting up?", ["No", "Yes, once", "Yes, frequently"])

watched_story = st.selectbox("Have they watched your stories but ignored your texts?", ["No", "Yes"])

watched_reels = st.selectbox("Did they watch the reels you sent them?", ["No", "Yes"])

sent_reels = st.selectbox("When was the last time they sent reels?", ["Today", "This week", "More than a week ago", "N/A"])

likes_stories = st.selectbox("Do they still like your stories?", ["Yes", "No"])

bad_influence_trip = st.selectbox("Are they on a trip with the bad influence friend?", ["No", "Yes"])

relationship_status = st.selectbox("What's your relationship status?", ["Boyfriend", "Flirt", "Situationship"])

if st.button("Check Ghosting Probability 💔"):
    result = calculate_ghosting_probability(response_time, online_no_reply, excuse, watched_story,
                                            watched_reels, sent_reels, likes_stories, bad_influence_trip, relationship_status)
    st.markdown(result)
