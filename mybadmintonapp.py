import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="World's Best Badminton Players", layout="wide")

# 2. Custom Colorful Title
st.markdown("<h1 style='color: #F9A826; text-align: center;'>🏸 Ultimate Badminton Hub</h1>", unsafe_allow_html=True)

# 3. Player Data (including specific racket models)
data = {
    "Rank": [1, 2, 3, 4],
    "Player Name": ["Viktor Axelsen", "An Se Young", "Kunlavut Vitidsarn", "Tai Tzu Ying"],
    "Category": ["Men's Singles", "Women's Singles", "Men's Singles", "Women's Singles"],
    "Win Rate (%)": [82.5, 85.1, 75.6, 77.4],
    "Racket": ["Astrox 100 ZZ", "Astrox 77 Play", "Astrox 88D Play", "Thruster F"],
    "Photo": [
        "https://upload.wikimedia.org/wikipedia/commons/8/87/Viktor_Axelsen_at_Indonesia_Masters_2020_02.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/An_Se-young_at_Indonesia_Masters_2020_03.jpg/800px-An_Se-young_at_Indonesia_Masters_2020_03.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kunlavut_Vitidsarn_at_Indonesia_Masters_2020.jpg/800px-Kunlavut_Vitidsarn_at_Indonesia_Masters_2020.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Tai_Tzu-Ying_at_Indonesia_Masters_2020.jpg/800px-Tai_Tzu-Ying_at_Indonesia_Masters_2020.jpg"
    ]
}
df = pd.DataFrame(data)

# 4. Create Interactive Tabs
tab1, tab2 = st.tabs(["📊 Player Database", "⚔️ Head-to-Head Stats"])

# --- TAB 1: Database & Spotlight ---
with tab1:
    st.subheader("Current Top Rankings")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.divider()
    st.subheader("Player Spotlight")
    selected_player = st.selectbox("Choose a player:", df["Player Name"])
    
    if selected_player:
        player_info = df[df["Player Name"] == selected_player].iloc[0]
        col1, col2, col3 = st.columns(3)
        
        # Adding colorful metrics
        col1.metric(label="World Rank", value=player_info["Rank"], delta="Top Tier")
        col2.metric(label="Win Rate", value=f"{player_info['Win Rate (%)']}%", delta="Active")
        col3.metric(label="Weapon of Choice", value=player_info["Racket"])

# --- TAB 2: Comparison Tool ---
with tab2:
    st.subheader("Compare Players")
    p1_col, p2_col = st.columns(2)
    
    with p1_col:
        p1 = st.selectbox("Player 1", df["Player Name"], key="p1")
        p1_stats = df[df["Player Name"] == p1].iloc[0]
        st.metric(label="Win Rate", value=f"{p1_stats['Win Rate (%)']}%")
        st.write(f"**Racket:** {p1_stats['Racket']}")
        
    with p2_col:
        p2 = st.selectbox("Player 2", df["Player Name"], key="p2")
        p2_stats = df[df["Player Name"] == p2].iloc[0]
        st.metric(label="Win Rate", value=f"{p2_stats['Win Rate (%)']}%")
        st.write(f"**Racket:** {p2_stats['Racket']}")