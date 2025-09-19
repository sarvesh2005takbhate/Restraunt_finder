# 🍽️ QuickEats - Restaurant Alternative Finder

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://restrauntfinder-ej9ycbed8cwbyypwyoigvd.streamlit.app/)

## 🚀 Live Demo
**Try it now:** [https://restrauntfinder-oc92ffvbfu2wgh8ycjfqu8.streamlit.app/](https://restrauntfinder-oc92ffvbfu2wgh8ycjfqu8.streamlit.app/)

## 📖 Problem Statement
Ever ordered food online and it's taking forever? You're hungry, the estimated delivery time keeps increasing, and you're stuck waiting. **QuickEats** solves this problem by instantly finding you alternative restaurants that serve similar dishes with faster delivery times!

## ✨ Features

### 🎯 Core Functionality
- **Smart Restaurant Matching**: Finds restaurants serving similar dishes to what you ordered
- **Speed Optimization**: Prioritizes restaurants with faster delivery/service times
- **Location-Aware**: Provides alternatives across different areas in your city
- **Comprehensive Details**: Shows delivery time, price range, location, and reasons to choose

### 🎨 User Experience
- **Clean, Professional UI**: Gradient-based design perfect for hackathon presentations
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Real-time Loading**: Smooth loading animations and feedback
- **Error Handling**: Graceful error management and user guidance

### 🧠 AI-Powered Intelligence
- **Context-Aware Suggestions**: Understanding cuisine types and restaurant categories
- **Realistic Recommendations**: Generates practical, location-specific alternatives
- **Multi-factor Analysis**: Considers speed, quality, price, and distance
- **Diverse Options**: Provides 4-5 varied alternatives for better choice

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Engine**: Google Gemini Flash API
- **Styling**: Custom CSS with gradients and modern design
- **Deployment**: Streamlit Cloud
- **Environment Management**: Python dotenv for secure API key handling

## 🎮 How to Use

1. **Enter Your City** - Type your current city (e.g., Mumbai, Delhi, Bangalore)
2. **Current Restaurant** - Enter the restaurant where you placed your order
3. **Dish Ordered** - Specify what you ordered (e.g., Pizza, Biryani, Burger)
4. **Click "Find Alternatives"** - Get instant recommendations!

### 📝 Example Usage
```
City: Mumbai
Current Restaurant: Domino's Pizza
Dish: Margherita Pizza
```

**Result**: Get 4-5 alternative pizza places in Mumbai with faster delivery, including local favorites and chain alternatives!

## 🏗️ Project Structure

```
restaurant-finder/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not committed)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🚀 Local Development

### Prerequisites
- Python 3.7+
- Google Gemini API key

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd restaurant-finder
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
```

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open your browser** to `http://localhost:8501`

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini Flash API key | Yes |

## 📱 Deployment

This app is deployed on **Streamlit Cloud**. To deploy your own version:

1. Push code to GitHub repository
2. Connect to [share.streamlit.io](https://share.streamlit.io)
3. Add `GEMINI_API_KEY` in Streamlit Cloud secrets
4. Deploy and share your link!

## 🎯 Hackathon Ready Features

### For Judges
- **Professional UI**: Clean, modern design suitable for presentations
- **Live Demo**: Fully functional web application
- **Real-time Results**: Instant AI-powered recommendations
- **Error Resilience**: Handles edge cases gracefully
- **Comprehensive Output**: Detailed restaurant information

### Technical Highlights
- **AI Integration**: Seamless integration with Google Gemini API
- **Smart Prompting**: Engineered prompts for realistic, contextual results
- **Responsive Design**: Professional-grade user interface
- **Scalable Architecture**: Clean code structure for easy expansion

## 📊 Sample Output

When you search for alternatives, you get:

```
🚀 Recommended Alternatives

#1 Pizza Express Downtown
Cuisine: Italian Fast Food
Location: Fort Area
Why Choose: Known for 10-minute express delivery and wood-fired pizzas
⏱️ Delivery Time: 10-15 mins | 💰 Price Range: ₹₹

#2 Local Pizza Corner
Cuisine: Continental
Location: Bandra West  
Why Choose: Family-owned restaurant with consistently fast service
⏱️ Delivery Time: 12-18 mins | 💰 Price Range: ₹
```

## 🎨 Design Philosophy

- **User-First**: Intuitive interface requiring minimal explanation
- **Speed-Focused**: Quick loading and instant results
- **Professional**: Suitable for business presentations and demos
- **Accessible**: Clear typography and good color contrast
- **Modern**: Contemporary design trends and visual appeal

## 🔮 Future Enhancements

- Real-time restaurant data integration
- User reviews and ratings display
- Distance calculation and mapping
- Price comparison features
- Order history and preferences
- Multi-cuisine filtering options

## 👥 Contributing

This project was built for a hackathon. For contributions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Google Gemini API** for powerful AI capabilities
- **Streamlit** for the amazing web framework
- **The Hackathon Community** for inspiration and innovation

---

**Built with ❤️ for the hackathon community**

*Need help? Have questions? Feel free to reach out!*