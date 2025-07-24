from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests
import time
import os

# Helper function to generate bios
def generate_bio(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    return result['choices'][0]['message']['content']

# Load prompt template
def load_prompt(name):
    with open(f"prompts/{name}.txt", "r") as file:
        return file.read()

st.set_page_config(
    page_title="SocialCraft | AI Social Assistant", 
    page_icon="💎", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Modern CSS with beautiful UI elements
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    :root {
        --bg-primary: #0f0f13;
        --bg-secondary: #1a1a24;
        --bg-card: #252536;
        --accent-primary: #6a11cb;
        --accent-secondary: #2575fc;
        --text-primary: #ffffff;
        --text-secondary: #a0a0c0;
        --border-color: #34344a;
        --success: #00c9a7;
    }
    * {
        transition: all 0.3s ease;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Inter', sans-serif;
    }
    
    body {
        background: var(--bg-primary);
        color: var(--text-primary);
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .content-wrap {
        flex: 1;
        padding-bottom: 60px;
    }
    
    .header-container {
        text-align: center;
        padding: 1.5rem 1rem;
        background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
        border-radius: 0 0 25px 25px;
        margin: -1rem -1rem 1.5rem -1rem;
        box-shadow: 0 10px 30px rgba(106, 17, 203, 0.4);
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at top right, rgba(255,255,255,0.15) 0%, transparent 40%);
    }
    
    .emoji-header {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        color: white;
        font-weight: 700;
    }
    
    .subheader {
        font-size: 1.1rem;
        max-width: 500px;
        margin: 0 auto;
        opacity: 0.9;
        font-weight: 300;
        color: rgba(255,255,255,0.95);
    }
    
    .tip-container {
        background: rgba(37, 117, 252, 0.15);
        border-radius: 14px;
        padding: 1rem;
        margin: 0 auto 1.5rem;
        max-width: 700px;
        border-left: 4px solid var(--accent-secondary);
        text-align: center;
        font-size: 0.95rem;
    }
    
    .purpose-selector {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 1.5rem 0 2rem;
    }
    
    .purpose-card {
        flex: 1;
        max-width: 280px;
        background: var(--bg-card);
        border-radius: 18px;
        padding: 1.8rem 1.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .purpose-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(106, 17, 203, 0.3);
    }
    
    .purpose-card.selected {
        border-color: var(--accent-secondary);
        background: linear-gradient(135deg, var(--bg-card), #2a2a4a);
    }
    
    .purpose-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: var(--accent-secondary);
        background: rgba(37, 117, 252, 0.15);
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    
    .purpose-card h3 {
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        color: var(--text-primary);
    }
    
    .purpose-card p {
        font-size: 0.95rem;
        color: var(--text-secondary);
    }
    
    .section {
        background: var(--bg-card);
        border-radius: 18px;
        padding: 1.8rem;
        margin: 1.5rem 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        border: 1px solid var(--border-color);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, var(--accent-primary) 0%, var(--accent-secondary) 100%);
        color: white;
        border-radius: 14px;
        padding: 0.9rem 2rem;
        font-weight: 600;
        border: none;
        font-size: 1rem;
        box-shadow: 0 5px 15px rgba(106, 17, 203, 0.3);
        transition: all 0.3s ease !important;
        width: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(106, 17, 203, 0.4);
    }
    
    .stButton>button::after {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            to right,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.3) 50%,
            rgba(255, 255, 255, 0) 100%
        );
        transform: rotate(30deg);
        transition: all 0.8s;
    }
    
    .stButton>button:hover::after {
        transform: translateX(100%) rotate(30deg);
    }
    
    .stTextInput>div>div>input, 
    .stTextArea>textarea,
    .stSelectbox>div>div>select {
        border-radius: 14px !important;
        border: 1px solid var(--border-color) !important;
        padding: 14px 18px !important;
        color: var(--text-primary) !important;
        background: var(--bg-secondary) !important;
        font-size: 1rem;
    }
    
    .stTextInput>div>div>input:focus, 
    .stTextArea>textarea:focus,
    .stSelectbox>div>div>select:focus {
        border: 1px solid var(--accent-secondary) !important;
        box-shadow: 0 0 0 3px rgba(37, 117, 252, 0.2) !important;
    }
    
    .result-card {
        background: var(--bg-card);
        border-radius: 18px;
        padding: 2.2rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        border: 1px solid var(--border-color);
        margin: 2rem 0;
    }
    
    .footer {
        text-align: center;
        color: var(--text-secondary);
        font-size: 0.9rem;
        padding: 1.5rem;
        background: var(--bg-secondary);
        border-top: 1px solid var(--border-color);
        bottom: 0;
        left: 0;
        width: 100%;
        z-index: 100;
        border-radius: 25px 25px 0 0;
    }
    
    .icon-label {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
        color: var(--text-primary);
        font-weight: 500;
        font-size: 1.05rem;
    }
    
    .icon-label i {
        color: var(--accent-secondary);
        font-size: 1.2rem;
        width: 30px;
        text-align: center;
        background: rgba(37, 117, 252, 0.15);
        padding: 8px;
        border-radius: 50%;
    }
    
    .section-title {
        color: var(--text-primary);
        font-size: 1.6rem;
        margin-bottom: 1.8rem;
        display: flex;
        align-items: center;
        gap: 15px;
        padding-bottom: 10px;
        border-bottom: 1px solid var(--border-color);
    }
    
    .section-title i {
        background: rgba(37, 117, 252, 0.2);
        width: 45px;
        height: 45px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--accent-secondary);
        font-size: 1.2rem;
    }
    
    .result-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 1.8rem;
    }
    
    .result-header i {
        background: rgba(37, 117, 252, 0.2);
        width: 45px;
        height: 45px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--accent-secondary);
        font-size: 1.2rem;
    }
    
    .feedback-section {
        background: var(--bg-card);
        border-radius: 18px;
        padding: 2.2rem;
        margin: 2rem 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        border: 1px solid var(--border-color);
    }
    
    .creator-credit {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin-top: 12px;
        font-size: 1rem;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-secondary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--accent-primary);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-secondary);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'purpose' not in st.session_state:
    st.session_state.purpose = "Create a profile bio"

# Header Section
st.markdown("""
<div class="header-container">
    <h1 class="emoji-header">✨ SocialCraft</h1>
    <p class="subheader">AI-powered bios & captions that elevate your social presence</p>
</div>
<div class="content-wrap">
""", unsafe_allow_html=True)

# Tip Container
st.markdown("""
<div class="tip-container">
    <strong><i class="fas fa-lightbulb"></i> Pro Tip:</strong> Be specific about your brand and audience for the best results!
</div>
""", unsafe_allow_html=True)

# Beautiful purpose selector
st.markdown("""
<div class="purpose-selector">
    <div class="purpose-card" id="bio-card" onclick="selectPurpose('bio')">
        <div class="purpose-icon">
            <i class="fas fa-user-astronaut"></i>
        </div>
        <h3>Create Profile Bio</h3>
        <p>Craft authentic bios for your social profiles</p>
    </div>    
    <div class="purpose-card" id="caption-card" onclick="selectPurpose('caption')">
        <div class="purpose-icon">
            <i class="fas fa-comment-dots"></i>
        </div>
        <h3>Generate Post Captions</h3>
        <p>Create engaging content for your posts</p>
    </div>
</div>
            
<script>
function selectPurpose(type) {
    document.querySelectorAll('.purpose-card').forEach(card => {
        card.classList.remove('selected');
    });    
    if (type === 'bio') {
        document.getElementById('bio-card').classList.add('selected');
        Streamlit.setComponentValue('Create a profile bio');
    } else {
        document.getElementById('caption-card').classList.add('selected');
        Streamlit.setComponentValue('Generate post caption + hashtags');
    }
}            
// Initialize selection
document.getElementById('bio-card').classList.add('selected');
</script>
""", unsafe_allow_html=True)

# Get purpose from frontend
purpose = st.radio(
    "Purpose selection",
    ["Create a profile bio", "Generate post caption + hashtags"],
    index=0,
    label_visibility="collapsed",
    key="purpose_selector"
)

# =================== BIO GENERATOR ===================
if purpose == "Create a profile bio":
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("""
        <div class="section-title">
            <i class="fas fa-user-edit"></i>
            <span>Tell me about yourself</span>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="icon-label"><i class="fas fa-mobile-alt"></i> Platform</div>', unsafe_allow_html=True)
        platform = st.selectbox(
            "Platform",
            ["Instagram", "LinkedIn", "YouTube", "Twitter", "TikTok"],
            label_visibility="collapsed",
            help="Where will this bio appear?"
        )
        
        st.markdown('<div class="icon-label"><i class="fas fa-briefcase"></i> Profession</div>', unsafe_allow_html=True)
        profession = st.text_input(
            "Profession",
            placeholder="e.g. Fashion designer, Student entrepreneur",
            label_visibility="collapsed"
        )
        
    with col2:
        st.markdown('<div class="icon-label"><i class="fas fa-palette"></i> Tone</div>', unsafe_allow_html=True)
        tone = st.selectbox(
            "Tone",
            ["Professional", "Friendly", "Witty", "Inspirational", "Casual"],
            index=0,
            label_visibility="collapsed"
        )
        
        st.markdown('<div class="icon-label"><i class="fas fa-list-ol"></i> Bio Options</div>', unsafe_allow_html=True)
        num_bios = st.slider("Number of bios", 1, 5, 3, label_visibility="collapsed")

    # Profession-specific follow-up
    if profession and profession.strip().lower() in ["artist", "creator", "designer"]:
        st.markdown('<div class="icon-label"><i class="fas fa-paint-brush"></i> Specialization</div>', unsafe_allow_html=True)
        art_type = st.text_input(
            "Art type",
            placeholder="e.g. Oil painting, Digital art",
            label_visibility="collapsed",
            key="art_type"
        )
    elif profession and profession.strip().lower() in ["business", "entrepreneur", "founder"]:
        st.markdown('<div class="icon-label"><i class="fas fa-building"></i> Business Type</div>', unsafe_allow_html=True)
        business_type = st.text_input(
            "Business type",
            placeholder="e.g. Sustainable fashion, SaaS",
            label_visibility="collapsed",
            key="business_type"
        )
    elif profession and ("influencer" in profession.strip().lower() or "creator" in profession.strip().lower()):
        st.markdown('<div class="icon-label"><i class="fas fa-bullseye"></i> Content Niche</div>', unsafe_allow_html=True)
        niche = st.text_input(
            "Niche",
            placeholder="e.g. Vegan recipes, Tech reviews",
            label_visibility="collapsed",
            key="niche"
        )

    st.markdown('<div class="icon-label"><i class="fas fa-star"></i> Key Highlights</div>', unsafe_allow_html=True)
    highlights = st.text_area(
        "Highlights",
        placeholder="Graduated from X • Featured in Y • Passionate about Z",
        height=90,
        label_visibility="collapsed"
    )
    
    st.markdown('<div class="icon-label"><i class="fas fa-users"></i> Target Audience</div>', unsafe_allow_html=True)
    audience = st.text_input(
        "Audience",
        placeholder="e.g. Job seekers, Pet lovers",
        label_visibility="collapsed"
    )

    if st.button("✨ Craft My Bio", use_container_width=True, key="bio_btn"):
        if not profession.strip():
            st.warning("Please tell us about your profession")
        else:
            with st.spinner("Crafting bios that sound authentically you..."):
                time.sleep(1)
                prompt = load_prompt("bio")
                full_prompt = prompt.format(
                    platform=platform,
                    profession=profession,
                    highlights=highlights,
                    tone=tone,
                    specifics=art_type if 'art_type' in locals() else business_type if 'business_type' in locals() else niche if 'niche' in locals() else "",
                    count=num_bios,
                    audience=audience  
                )
                bios = generate_bio(full_prompt)

            st.markdown("</div>", unsafe_allow_html=True)  # Close section
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("""
                <div class="result-header">
                    <i class="fas fa-file-alt"></i>
                    <h3>Your Personalized Bio Options</h3>
                </div>
            """, unsafe_allow_html=True)
            
            st.text_area(
                "Generated bios", 
                value=bios, 
                height=280, 
                label_visibility="collapsed"
            )
            
            st.download_button("💾 Download All Bios", bios, file_name=f"{platform}_bios.txt", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

# =================== CAPTION GENERATOR ===================
else:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("""
        <div class="section-title">
            <i class="fas fa-pen-alt"></i>
            <span>Tell me about your post</span>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="icon-label"><i class="fas fa-mobile-alt"></i> Platform</div>', unsafe_allow_html=True)
        platform = st.selectbox(
            "Platform",
            ["Instagram", "TikTok", "YouTube", "Twitter", "Facebook"],
            label_visibility="collapsed",
            key="platform_cap"
        )
        
        st.markdown('<div class="icon-label"><i class="fas fa-camera"></i> Content Format</div>', unsafe_allow_html=True)
        post_type = st.selectbox(
            "Post type",
            ["Photo", "Reel/Short", "Video", "Carousel", "Story", "Text Quote"],
            label_visibility="collapsed",
            key="post_type"
        )
        
    with col2:
        st.markdown('<div class="icon-label"><i class="fas fa-smile"></i> Tone</div>', unsafe_allow_html=True)
        tone = st.selectbox(
            "Tone",
            ["Inspirational", "Funny/Humorous", "Educational", "Emotional", "Casual"],
            index=0,
            label_visibility="collapsed",
            key="tone_cap"
        )
        
        st.markdown('<div class="icon-label"><i class="fas fa-users"></i> Audience</div>', unsafe_allow_html=True)
        audience = st.text_input(
            "Audience",
            placeholder="e.g. Teenagers, Entrepreneurs",
            label_visibility="collapsed",
            key="audience_cap"
        )

    st.markdown('<div class="icon-label"><i class="fas fa-bullseye"></i> Post Topic</div>', unsafe_allow_html=True)
    genre = st.text_input(
        "Genre",
        placeholder="e.g. New product, Travel diary, Tutorial",
        label_visibility="collapsed",
        key="genre"
    )
    
    # Content-specific details
    if genre:
        if "product" in genre.lower():
            st.markdown('<div class="icon-label"><i class="fas fa-box-open"></i> Product Details</div>', unsafe_allow_html=True)
            product_details = st.text_area(
                "Product details",
                placeholder="Key features? Benefits?",
                height=70,
                label_visibility="collapsed"
            )
        elif "travel" in genre.lower():
            st.markdown('<div class="icon-label"><i class="fas fa-map-marker-alt"></i> Location</div>', unsafe_allow_html=True)
            location = st.text_input(
                "Location",
                placeholder="Where is this?",
                label_visibility="collapsed"
            )
        elif "recipe" in genre.lower() or "food" in genre.lower():
            st.markdown('<div class="icon-label"><i class="fas fa-utensils"></i> Cuisine Type</div>', unsafe_allow_html=True)
            cuisine = st.text_input(
                "Cuisine",
                placeholder="e.g. Italian, Vegan",
                label_visibility="collapsed"
            )

    st.markdown('<div class="icon-label"><i class="fas fa-comment-alt"></i> Core Message</div>', unsafe_allow_html=True)
    message = st.text_area(
        "Message",
        placeholder="What should people take away?",
        height=90,
        label_visibility="collapsed",
        key="message"
    )

    if st.button("🚀 Create Post Content", use_container_width=True, key="caption_btn"):
        if not genre.strip():
            st.warning("Please describe your post content")
        else:
            with st.spinner("Crafting captions that resonate..."):
                time.sleep(1)
                prompt = load_prompt("caption")
                final_prompt = prompt.format(
                    platform=platform,
                    post_type=post_type,
                    genre=genre,
                    tone=tone,
                    audience=audience,
                    specifics=product_details if 'product_details' in locals() else location if 'location' in locals() else cuisine if 'cuisine' in locals() else "",
                    message=message
                )
                caption_output = generate_bio(final_prompt)

            st.markdown("</div>", unsafe_allow_html=True)  # Close section
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("""
                <div class="result-header">
                    <i class="fas fa-comment-dots"></i>
                    <h3>Your Post Content</h3>
                </div>
            """, unsafe_allow_html=True)
            
            st.text_area(
                "Generated caption", 
                value=caption_output, 
                height=320, 
                label_visibility="collapsed"
            )
            
            st.download_button("💾 Copy Full Content", caption_output, file_name=f"{platform}_caption.txt", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

# =================== FEEDBACK SECTION ===================
google_form_embed_url = "https://docs.google.com/forms/d/e/1FAIpQLSf-Y7UgRH61zeEc1ouZaKBc7ivK31CnCW45ZrL0CjDAeDAVRw/viewform?embedded=true"
st.markdown(f"""
<div class="feedback-section">
    <div class="section-title">
        <i class="fas fa-comment-dots"></i>
        <span>We'd Love Your Feedback</span>
    </div>
    <p>Help us improve by sharing your thoughts about this tool.</p>
    <div style="
        width: 100%; 
        height: 600px; 
        border-radius: 14px; 
        overflow: hidden; 
        margin-top: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        border: 1px solid var(--border-color);
    ">
        <iframe 
            src="{google_form_embed_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            marginheight="0" 
            marginwidth="0"
            style="
                background: var(--bg-secondary);
                color: var(--text-primary);
                border: none;
            "
        >
            Loading...
        </iframe>
    </div>
    <p style="text-align: center; margin-top: 1rem; font-size: 0.9rem;">
        <i class="fas fa-info-circle"></i> Form might take a few seconds to load
    </p>
</div>
""", unsafe_allow_html=True)

# Close content wrap
st.markdown("</div>", unsafe_allow_html=True)

# Sticky Footer
st.markdown("""
<div class="footer">
    ⚡ Powered by OpenAI • ✨ Crafted with ❤️ for creators • 💎 v3.0
    <div class="creator-credit">
        <span>Created by</span>
        <span style="font-weight:500; color:#6a11cb;">Aditya Kachhawa / UNKNOWN_Famous</span>
    </div>
</div>
""", unsafe_allow_html=True)