"""
app.py - AI-Powered Alzheimer's Language Insight Tool
Educational demonstration of language pattern analysis
"""

import streamlit as st
import re
from collections import Counter
import time

# ============================================
# MOCK AI ANALYSIS FUNCTION
# ============================================

def mock_ai_analyze(text):
    """
    Mock AI function that simulates language pattern analysis.
    No external API keys required - runs entirely locally.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Analysis results including metrics and insights
    """
    
    # Simulate processing delay for realism
    time.sleep(1)
    
    # Text preprocessing
    text_lower = text.lower()
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    words = re.findall(r'\b\w+\b', text_lower)
    
    # Calculate metrics
    word_count = len(words)
    sentence_count = len(sentences)
    
    # Vocabulary variety (lexical diversity)
    unique_words = len(set(words))
    vocab_variety = (unique_words / word_count * 100) if word_count > 0 else 0
    
    # Sentence structure (average words per sentence)
    avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
    
    # Repetition analysis
    word_freq = Counter(words)
    repeated_words = sum(1 for count in word_freq.values() if count > 1)
    repetition_rate = (repeated_words / unique_words * 100) if unique_words > 0 else 0
    
    # Self-referential language (first-person pronouns)
    self_ref_pronouns = ['i', 'me', 'my', 'myself', 'mine', 'we', 'us', 'our']
    self_ref_count = sum(words.count(pronoun) for pronoun in self_ref_pronouns)
    self_ref_percentage = (self_ref_count / word_count * 100) if word_count > 0 else 0
    
    # Generate AI-style insights
    insights = []
    
    # Vocabulary insights
    if vocab_variety > 70:
        insights.append("✓ Rich vocabulary variety detected - diverse word usage")
    elif vocab_variety > 50:
        insights.append("• Moderate vocabulary variety - adequate word diversity")
    else:
        insights.append("○ Limited vocabulary variety - repetitive word patterns observed")
    
    # Sentence structure insights
    if avg_sentence_length > 20:
        insights.append("✓ Complex sentence structures - detailed expression")
    elif avg_sentence_length > 12:
        insights.append("• Balanced sentence length - clear communication style")
    else:
        insights.append("○ Short sentences - simplified language structure")
    
    # Repetition insights
    if repetition_rate < 30:
        insights.append("✓ Low repetition - varied expression throughout")
    elif repetition_rate < 50:
        insights.append("• Moderate repetition - some recurring themes")
    else:
        insights.append("○ High repetition - frequent reuse of same words")
    
    # Self-referential insights
    if self_ref_percentage > 8:
        insights.append("• High self-reference - personal narrative focus")
    elif self_ref_percentage > 3:
        insights.append("• Moderate self-reference - balanced perspective")
    else:
        insights.append("• Low self-reference - objective communication style")
    
    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'vocab_variety': vocab_variety,
        'avg_sentence_length': avg_sentence_length,
        'repetition_rate': repetition_rate,
        'self_ref_percentage': self_ref_percentage,
        'insights': insights
    }


# ============================================
# STREAMLIT APP CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Alzheimer's Language Insight Tool",
    page_icon="🧠",
    layout="centered"
)

# ============================================
# APP HEADER
# ============================================

st.title("🧠 AI-Powered Alzheimer's Language Insight Tool")
st.markdown("*Educational demonstration of language pattern analysis*")
st.markdown("---")

# ============================================
# USER INPUT SECTION
# ============================================

st.subheader("📝 Enter Text for Analysis")

user_text = st.text_area(
    "Paste or type text below:",
    height=200,
    placeholder="Enter text here for language pattern analysis...",
    help="Type or paste any text sample to analyze language patterns"
)

# Analyze button
analyze_btn = st.button("🔍 Analyze Language Patterns", type="primary", use_container_width=True)

# ============================================
# ANALYSIS EXECUTION AND RESULTS
# ============================================

if analyze_btn:
    if not user_text.strip():
        st.error("❌ Please enter some text to analyze")
    else:
        # Show progress
        with st.spinner("🤖 AI analyzing language patterns..."):
            results = mock_ai_analyze(user_text)
        
        st.success("✅ Analysis Complete!")
        st.markdown("---")
        
        # ============================================
        # METRICS DISPLAY
        # ============================================
        
        st.subheader("📊 Language Pattern Metrics")
        
        # Display metrics in columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="Vocabulary Variety",
                value=f"{results['vocab_variety']:.1f}%",
                help="Percentage of unique words used"
            )
        
        with col2:
            st.metric(
                label="Avg Sentence Length",
                value=f"{results['avg_sentence_length']:.1f}",
                help="Average number of words per sentence"
            )
        
        with col3:
            st.metric(
                label="Repetition Rate",
                value=f"{results['repetition_rate']:.1f}%",
                help="Percentage of words used multiple times"
            )
        
        with col4:
            st.metric(
                label="Self-Reference",
                value=f"{results['self_ref_percentage']:.1f}%",
                help="Percentage of first-person pronouns"
            )
        
        # Additional basic metrics
        st.markdown("---")
        col5, col6 = st.columns(2)
        with col5:
            st.metric("Total Words", results['word_count'])
        with col6:
            st.metric("Total Sentences", results['sentence_count'])
        
        # ============================================
        # AI INSIGHTS SECTION
        # ============================================
        
        st.markdown("---")
        st.subheader("💡 AI-Generated Insights")
        
        for insight in results['insights']:
            st.markdown(f"• {insight}")
        
        # Educational context
        st.info("""
        **Educational Note:** Language patterns are influenced by many factors including:
        - Personal communication style
        - Topic and context
        - Educational background
        - Emotional state
        - Cultural influences
        
        These metrics provide general observations about language structure.
        """)

# ============================================
# DISCLAIMER (ALWAYS VISIBLE)
# ============================================

st.markdown("---")
st.warning("⚠️ **This tool is for educational purposes only and does not provide medical diagnosis.**")

# Footer information
st.caption("""
**Important:** This is a demonstration tool using simulated AI analysis. 
Language patterns alone cannot diagnose any medical condition. 
Consult qualified healthcare professionals for medical concerns.
""")