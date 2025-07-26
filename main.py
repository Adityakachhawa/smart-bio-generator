import streamlit as st

st.set_page_config(
    page_title="SparkSocial AI - Create Human-Like Social Content",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load CSS
try:
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        # st.success("✅ CSS Loaded Successfully")
except FileNotFoundError:
    st.error("❌ styles.css file not found. Please check the path.")

# Load Font Awesome
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# Hero Section with Form
st.markdown("""
<div class="hero">
    <div class="hero-content">
        <h1 class="hero-title">Transform Your Social Media with AI That Sounds Human</h1>
        <p class="hero-subtitle">Create authentic bios and captions in seconds - no robotic language, just your unique voice</p>
        <div>
            <a href="/app" target="_self" class="cta-button">Get Started Free</a>
            <a href="#features" target="_self" class="cta-button cta-secondary">See How It Works</a>
        </div>
        <div class="stats">
            <div class="stat-item">
                <div class="stat-number">12,500+</div>
                <div class="stat-label">Bios Created</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">98%</div>
                <div class="stat-label">User Satisfaction</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">90%</div>
                <div class="stat-label">More Engagement</div>
            </div>
        </div>
    </div>
    <div class="pattern pattern-1">
        <i class="fas fa-comment-alt"></i>
    </div>
    <div class="pattern pattern-2">
        <i class="fas fa-hashtag"></i>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div class="container">
    <div class="section-title">
        <h2>Why Creators Love SparkSocial AI</h2>
        <p>Our AI understands nuance and personality to create content that actually sounds like you</p>
    </div>
    <div class="features">
        <div class="feature-card">
            <div class="feature-badge">Most Popular</div>
            <div class="feature-icon">
                <i class="fas fa-user-edit"></i>
            </div>
            <h3>Authentic Voice</h3>
            <p>Our AI captures your unique personality and tone, creating content that sounds genuinely human.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">
                <i class="fas fa-bolt"></i>
            </div>
            <h3>Lightning Fast</h3>
            <p>Generate content in seconds, saving you hours of manual work.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">
                <i class="fas fa-robot"></i>
            </div>
            <h3>Platform Optimized</h3>
            <p>Tailored content for Instagram, TikTok, LinkedIn, Twitter, and more.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# How It Works Section
st.markdown("""
<div class="how-it-works">
    <div class="container">
        <div class="section-title">
            <h2 style="color: white;">How It Works (Updated 2025)</h2>
            <p style="color: rgba(255,255,255,0.9);">Get amazing content in 3 simple steps</p>
        </div>
        <div class="steps">
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>Tell Us About You</h3>
                <p>Share your personality, profession, and goals. The more details, the better the results!</p>
            </div>
            <div class="step-card">
                <div class="step-number">2</div>
                <h3>AI Generates Options</h3>
                <p>Our advanced AI creates multiple tailored options based on your input and platform.</p>
            </div>
            <div class="step-card">
                <div class="step-number">3</div>
                <h3>Copy & Shine</h3>
                <p>Choose your favorite, copy it to your social media, and watch your engagement grow!</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonials Section
st.markdown("""
<div class="container">
    <div class="section-title">
        <h2>What Users Say</h2>
        <p>Join thousands of creators and professionals who transformed their social presence</p>
    </div>
    <div class="testimonials">
        <div class="testimonial-card">
            <p class="testimonial-text">"As a solo founder building everything from scratch, I used to spend hours trying to come up with the perfect bio or caption — and still never felt satisfied. Then I found SparkSocial. The bios felt like me, but sharper, smarter, and more confident. Within a month, my Instagram engagement exploded — 40% more followers, tons of profile visits, and people actually DMing me saying, 'Love your vibe!' SparkSocial didn’t just save me time — it gave my brand a voice I’m proud of."</p>
            <div class="testimonial-author">
                <div class="author-avatar">SJ</div>
                <div class="author-info">
                    <h4>Anurag Tanwar</h4>
                    <p>Founder & CEO, THEREAL_BIKANA Company</p>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p class="testimonial-text">"As a small business owner, I struggled with social media. Now I get perfectly branded captions in seconds. Best investment I've made for my online presence!"</p>
            <div class="testimonial-author">
                <div class="author-avatar">MR</div>
                <div class="author-info">
                    <h4>Somdev Solanki</h4>
                    <p>Content Creator | 25K follower</p>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p class="testimonial-text">"The AI actually understands nuance! I've tried other tools, but SparkSocial is the only one that captures my professional yet approachable tone for LinkedIn."</p>
            <div class="testimonial-author">
                <div class="author-avatar">TJ</div>
                <div class="author-info">
                    <h4>Thomas James</h4>
                    <p>Marketing Director</p>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Pricing Section
st.markdown("""
<div class="pricing">
    <div class="container">
        <div class="section-title">
            <h2>Simple, Transparent Pricing</h2>
            <p style="color: rgba(0,0,0,0.7);">Choose the plan that works for you</p>
        </div>
        <div class="pricing-cards">
            <div class="pricing-card">
                <div class="pricing-header">
                    <h3 class="pricing-name">Starter</h3>
                    <div class="pricing-price">$0</div>
                    <div class="pricing-period">Free Forever</div>
                </div>
                <ul class="pricing-features">
                    <li>5 bios per month</li>
                    <li>3 caption sets</li>
                    <li>Basic tone options</li>
                    <li class="disabled">Priority support</li>
                    <li class="disabled">Advanced customization</li>
                </ul>
                <a href="/app" target="_self" class="cta-button" style="width: 100%; margin: 0;">Get Started</a>
            </div>
            <div class="pricing-card">
                <div class="feature-badge" style="position: static; margin-bottom: 1.5rem;">Most Popular</div>
                <div class="pricing-header">
                    <h3 class="pricing-name">Creator</h3>
                    <div class="pricing-price">$12</div>
                    <div class="pricing-period">per month</div>
                </div>
                <ul class="pricing-features">
                    <li>Unlimited bios</li>
                    <li>Unlimited captions</li>
                    <li>All tone options</li>
                    <li>Priority support</li>
                    <li>Advanced customization</li>
                </ul>
                <a href="/app" target="_self" class="cta-button" style="width: 100%; margin: 0; background: var(--gradient-purple); color: white !important;">Upgrade Now</a>
            </div>
            <div class="pricing-card">
                <div class="pricing-header">
                    <h3 class="pricing-name">Agency</h3>
                    <div class="pricing-price">$99</div>
                    <div class="pricing-period">per month</div>
                </div>
                <ul class="pricing-features">
                    <li>Unlimited everything</li>
                    <li>10 team members</li>
                    <li>Brand voice profiles</li>
                    <li>Dedicated account manager</li>
                    <li>Bulk content generation</li>
                </ul>
                <a href="/app" target="_self" class="cta-button" style="width: 100%; margin: 0;">Contact Sales</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="container">
    <div class="section-title">
        <h2>Frequently Asked Questions</h2>
        <p>Everything you need to know about SparkSocial AI</p>
    </div>
</div>
""", unsafe_allow_html=True)
with st.expander("How does SparkSocial create human-like content?"):
    st.write("Our AI has been trained on millions of authentic social media posts...")
with st.expander("Can I customize the tone of the generated content?"):
    st.write("Absolutely! You can choose from professional, friendly, witty...")
with st.expander("Which social platforms does SparkSocial support?"):
    st.write("We currently support Instagram, TikTok, LinkedIn, Twitter, YouTube...")
with st.expander("Is my content stored or used for training?"):
    st.write("Never! We respect your privacy and creativity...")

# Final CTA Section
st.markdown("""
<div class="final-cta">
    <div class="container">
        <h2>Ready to Transform Your Social Presence?</h2>
        <p>Join thousands of creators and professionals who save hours every week with SparkSocial AI</p>
        <a href="/app" target="_self" class="cta-button" style="background: var(--gradient-accent); font-size: 1.4rem; padding: 1.3rem 4rem;">Get Started Free</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-column">
            <h3>SparkSocial AI</h3>
            <p style="color: #a0aec0; margin-bottom: 1.5rem; max-width: 300px;">Creating authentic social content that sounds human, not robotic.</p>
            <div class="social-icons">
                <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-linkedin-in"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-facebook-f"></i></a>
            </div>
        </div>
        <div class="footer-column">
            <h3>Product</h3>
            <ul class="footer-links">
                <li><a href="#">Features</a></li>
                <li><a href="#">Pricing</a></li>
                <li><a href="#">Use Cases</a></li>
                <li><a href="#">Roadmap</a></li>
                <li><a href="#">Changelog</a></li>
            </ul>
        </div>
        <div class="footer-column">
            <h3>Resources</h3>
            <ul class="footer-links">
                <li><a href="#">Blog</a></li>
                <li><a href="#">Tutorials</a></li>
                <li><a href="#">Documentation</a></li>
                <li><a href="#">Community</a></li>
                <li><a href="#">Support</a></li>
            </ul>
        </div>
        <div class="footer-column">
            <h3>Company</h3>
            <ul class="footer-links">
                <li><a href="#">About Us</a></li>
                <li><a href="#">Careers</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#">Partners</a></li>
                <li><a href="#">Legal</a></li>
            </ul>
        </div>
    </div>
    <div class="copyright">
        <p>© 2023 SparkSocial AI. All rights reserved.</p>
        <p>Created with ❤️ by Aditya Kachhawa</p>
    </div>
</div>
""", unsafe_allow_html=True)
