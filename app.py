import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def get_restaurant_alternatives(city, current_restaurant, dish):
    """Get alternative restaurants using Gemini API"""
    
    prompt = f"""
    You are a restaurant recommendation system. A customer ordered "{dish}" from "{current_restaurant}" in {city}, but it's taking too long.
    
    Please suggest 4-5 alternative restaurants in {city} that:
    1. Serve similar dishes to "{dish}"
    2. Are known for faster delivery/service
    3. Have good ratings
    4. Include a mix of nearby and other locations in the city
    
    For each restaurant, provide:
    - Restaurant name
    - Cuisine type
    - Estimated delivery time
    - Distance/location area in {city}
    - Why it's a good alternative (brief reason)
    - Price range (₹, ₹₹, ₹₹₹)
    
    Assume realistic restaurant names and details for {city}. Make the suggestions practical and diverse.
    
    Format as JSON:
    {{
        "alternatives": [
            {{
                "name": "Restaurant Name",
                "cuisine": "Cuisine Type",
                "delivery_time": "15-25 mins",
                "location": "Area name",
                "reason": "Known for quick service and authentic taste",
                "price_range": "₹₹"
            }}
        ]
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        # Clean the response text
        response_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        return json.loads(response_text)
    except Exception as e:
        st.error(f"Error getting recommendations: {str(e)}")
        return None

def main():
    # Page configuration
    st.set_page_config(
        page_title="QuickEats - Restaurant Alternative Finder",
        page_icon="🍽️",
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    .restaurant-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-container {
        display: flex;
        justify-content: space-between;
        margin-top: 1rem;
    }
    .metric-item {
        text-align: center;
        flex: 1;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🍽️ QuickEats - Restaurant Alternative Finder</h1>
        <p>Find faster alternatives when your order is delayed!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input form
    col1, col2, col3 = st.columns(3)
    
    with col1:
        city = st.text_input("🏙️ Your City", placeholder="e.g., Mumbai, Delhi, Bangalore")
    
    with col2:
        current_restaurant = st.text_input("🏪 Current Restaurant", placeholder="e.g., Domino's, KFC, Local Restaurant")
    
    with col3:
        dish = st.text_input("🍕 Dish Ordered", placeholder="e.g., Pizza, Biryani, Burger")
    
    # Search button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔍 Find Alternatives", use_container_width=True):
            if city and current_restaurant and dish:
                with st.spinner("Finding the best alternatives for you..."):
                    results = get_restaurant_alternatives(city, current_restaurant, dish)
                
                if results and "alternatives" in results:
                    st.success(f"Found {len(results['alternatives'])} great alternatives!")
                    
                    # Display results
                    st.markdown("### 🚀 Recommended Alternatives")
                    
                    for i, restaurant in enumerate(results['alternatives'], 1):
                        with st.container():
                            st.markdown(f"""
                            <div class="restaurant-card">
                                <h3>#{i} {restaurant['name']}</h3>
                                <p><strong>Cuisine:</strong> {restaurant['cuisine']}</p>
                                <p><strong>Location:</strong> {restaurant['location']}</p>
                                <p><strong>Why Choose:</strong> {restaurant['reason']}</p>
                                
                                <div class="metric-container">
                                    <div class="metric-item">
                                        <h4>⏱️ Delivery Time</h4>
                                        <p>{restaurant['delivery_time']}</p>
                                    </div>
                                    <div class="metric-item">
                                        <h4>💰 Price Range</h4>
                                        <p>{restaurant['price_range']}</p>
                                    </div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                    
                    # Additional tips
                    st.markdown("### 💡 Pro Tips")
                    tips_col1, tips_col2 = st.columns(2)
                    
                    with tips_col1:
                        st.info("📞 **Call ahead** to confirm availability and current wait times")
                    
                    with tips_col2:
                        st.info("🎯 **Check reviews** on food delivery apps for real-time ratings")
                
                else:
                    st.error("Sorry, couldn't find alternatives. Please try again!")
            
            else:
                st.warning("Please fill in all fields to get recommendations!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Built for Hackathon • Powered by Gemini AI • Find food faster! 🚀"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()