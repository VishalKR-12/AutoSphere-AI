# AutoSphere AI: Automate, Assist, Achieve

## 🚀 Project Overview

AutoSphere AI is an intelligent automation platform designed to leverage IBM's Watson AI services for creating end-to-end automation solutions. The project focuses on India-centric applications with social impact, particularly in areas like agriculture, healthcare, and education. Now featuring a modern, responsive web frontend with real-time backend integration.

## 🎯 Project Goals

- **Automate**: Streamline complex workflows using AI-powered automation
- **Assist**: Provide intelligent assistance for decision-making and task execution
- **Achieve**: Enable users to accomplish more with less effort through AI augmentation

## ✨ Latest Features & Enhancements

### 🎨 Modern UI/UX Design
- **ChatGPT-Style Interface**: Professional chat interface with modern design elements
- **Glass Morphism Effects**: Beautiful translucent glass effects throughout the interface
- **Custom Logo Integration**: AutoSphereAI logo prominently displayed in header and chat
- **Enhanced Dark Theme**: Improved visibility and contrast for all headings and text
- **Responsive Design**: Optimized for all devices with smooth animations

### 🎭 Advanced Theming
- **Dual Theme Support**: Seamless light/dark mode switching
- **Custom Color Palettes**: Deep blue color scheme with professional gradients
- **Smooth Transitions**: Animated theme switching with CSS transitions
- **Accessibility**: High contrast and proper color ratios for readability

### 💬 Enhanced Chat Experience
- **Real-time Messaging**: Live communication with IBM Watson AI backend
- **Message Formatting**: Markdown support for rich text responses
- **Chat History**: Persistent conversation memory
- **Export Functionality**: Download chat conversations
- **Status Indicators**: Real-time connection and typing indicators

## 🛠️ Technology Stack

### Backend (Python)
- **AI Framework**: IBM Watson AI (watsonx.ai)
- **Language Model**: IBM Granite-3-3-8b-instruct
- **Agent Framework**: LangGraph with React Agent
- **Web Framework**: Flask with CORS support
- **Tools Integration**: 
  - Google Search
  - Web Crawler
  - Wikipedia
  - DuckDuckGo
  - Weather API
- **Development Environment**: Python 3.11 with environment variables

### Frontend (Web)
- **HTML5**: Semantic markup with modern structure
- **CSS3**: Advanced styling with CSS Grid, Flexbox, CSS Variables, and Glass Morphism
- **JavaScript (ES6+)**: Modern JavaScript with classes and async/await
- **Responsive Design**: Mobile-first approach with breakpoints
- **Theme Support**: Light/Dark mode with smooth transitions
- **Animations**: CSS animations, keyframes, and JavaScript-powered interactions
- **API Integration**: Real-time communication with Python backend
- **Glass Effects**: Backdrop filters and translucent backgrounds

## 📋 Prerequisites

- Python 3.11 or higher
- IBM Cloud account with API key
- Access to watsonx.ai services
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🔧 Installation & Setup

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AutoSphere-AI
   ```

2. **Run the startup script**
   ```bash
   python run.py
   ```
   
   This will:
   - Check and install dependencies
   - Create configuration file if needed
   - Guide you through setup
   - Start the server

### Manual Setup

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**
   - Edit `config.env` file
   - Add your IBM Cloud API key and project ID:
   ```env
   IBM_API_KEY=your_actual_api_key_here
   IBM_PROJECT_ID=your_actual_project_id_here
   ```

3. **Start the server**
   ```bash
   python autosphere_server.py
   ```

4. **Access the application**
   - Open your browser to: http://localhost:8000
   - The frontend will automatically connect to the backend API
   - See the [Screenshots](#-screenshots) section below for UI previews

## 🚀 Usage

### Web Interface

1. **Open the application**
   - Navigate to http://localhost:8000
   - The interface will show connection status

2. **Start chatting**
   - Type your questions in the chat input
   - Press Enter or click the send button
   - View real-time responses from IBM Watson AI

3. **Features available**
   - **Real-time Chat**: Live communication with AI backend
   - **Conversation History**: Persistent chat memory
   - **Theme Toggle**: Light/dark mode switching
   - **Delete Chat**: Clear all conversation history with one click
   - **Export Chat**: Download conversation history as JSON file
   - **Responsive Design**: Works on all devices
   - **Glass Effects**: Beautiful translucent interface elements
   - **Custom Branding**: AutoSphereAI logo throughout

### Command Line Interface

For direct command-line access:

```bash
python autosphere_ai.py
```

This provides the original interactive CLI experience.

## 🎯 Key Features

### AI Agent Capabilities
- **Multi-source Information Retrieval**: Combines data from web search, Wikipedia, and other sources
- **Intelligent Reasoning**: Uses IBM Granite models for advanced reasoning and summarization
- **Workflow Automation**: Orchestrates complex tasks using IBM Agent Development Kit
- **RAG Implementation**: Retrieval-Augmented Generation for factual, grounded responses
- **Conversation Memory**: Maintains context across multiple interactions

### Web Interface Features
- **Modern Design**: Clean, professional interface with ChatGPT-style layout
- **Glass Morphism**: Beautiful translucent effects with backdrop blur
- **Custom Logo**: AutoSphereAI branding throughout the interface
- **Responsive Layout**: Optimized for desktop, tablet, and mobile devices
- **Theme Support**: Light and dark mode with automatic preference detection
- **Real-time Chat**: Interactive chat interface with typing indicators
- **Chat Management**: Delete chat history and export functionality
  - **Delete Chat**: Clear all conversation history with one click
  - **Export Chat**: Download conversation history as JSON file for backup
- **Smooth Navigation**: Single-page application with smooth scrolling
- **Accessibility**: Keyboard navigation and screen reader support
- **API Integration**: Seamless communication with Python backend
- **Message Formatting**: Rich text support with markdown rendering

### India-Centric Focus
- Agriculture automation solutions
- Healthcare assistance and optimization
- Educational technology applications
- Social impact initiatives

### Automation Principles
- End-to-end workflow automation
- Time and cost optimization
- Efficiency improvement recommendations
- Interdisciplinary collaboration suggestions

## 📁 Project Structure

```
AutoSphere AI/
├── Frontend/
│   ├── index.html              # Main HTML file
│   ├── styles.css              # CSS styles, animations, and glass effects
│   ├── script.js               # JavaScript functionality
│   └── AutoSphereAI Logo.png   # Custom logo file
├── Backend/
│   ├── autosphere_server.py    # Flask server with API endpoints
│   ├── autosphere_ai.py        # AI agent class
│   ├── run.py                  # Startup script
│   └── requirements.txt        # Python dependencies
├── Configuration/
│   ├── config.env              # Environment variables
│   └── test_setup.py           # Setup validation script
├── Screenshots/
│   ├── Light UI/               # Light theme screenshots
│   │   ├── 1.png              # Hero section
│   │   ├── 2.png              # Features section
│   │   ├── 3.png              # Chat interface
│   │   ├── 4.png              # About section
│   │   └── 5.png              # Footer
│   └── Dark UI/                # Dark theme screenshots
│       ├── 1.png              # Hero section
│       ├── 2.png              # Features section
│       ├── 3.png              # Chat interface
│       ├── 4.png              # About section
│       └── 5.png              # Footer
└── Documentation/
    ├── README.md               # This file
    └── AutoSphere AI Abstract.pdf # Project abstract
```

## 🔍 Core Components

### Backend Components
1. **Flask Server** (`autosphere_server.py`)
   - **API Endpoints**: `/api/chat`, `/api/health`, `/api/clear`
     - **POST /api/chat**: Process chat messages and return AI responses
     - **GET /api/health**: Server health check and AI initialization status
     - **POST /api/clear**: Clear conversation history on server
   - **Static File Serving**: Serves frontend files
   - **CORS Support**: Cross-origin resource sharing
   - **Error Handling**: Comprehensive error management

2. **AI Agent** (`autosphere_ai.py`)
   - **Model**: IBM Granite-3-3-8b-instruct
   - **Parameters**: Optimized for detailed responses (2000 max tokens, temperature 0)
   - **Memory**: Persistent conversation memory using MemorySaver
   - **Environment Support**: Configurable via environment variables

3. **Tool Integration**
   - **GoogleSearch**: Web search capabilities
   - **WebCrawler**: Content extraction from web pages
   - **Wikipedia**: Knowledge base access
   - **DuckDuckGo**: Alternative search engine
   - **Weather**: Real-time weather information

### Frontend Components
1. **User Interface**
   - **Hero Section**: Eye-catching introduction with animated AI orb
   - **Features Section**: Grid layout showcasing key capabilities
   - **Chat Interface**: ChatGPT-style real-time messaging with glass effects
   - **About Section**: Technology stack and application areas

2. **Interactive Elements**
   - **Theme Toggle**: Switch between light and dark modes
   - **Navigation**: Smooth scrolling with active section highlighting
   - **Chat Actions**: Send, clear, and export chat functionality
   - **Responsive Design**: Mobile-optimized layout
   - **API Communication**: Real-time backend integration
   - **Logo Integration**: Custom AutoSphereAI logo throughout

3. **Animations & Effects**
   - **AI Orb Animation**: Pulsing core with rotating rings and floating particles
   - **Glass Morphism**: Translucent backgrounds with backdrop blur effects
   - **Scroll Animations**: Elements fade in as they enter the viewport
   - **Hover Effects**: Interactive feedback on buttons and cards
   - **Typing Indicators**: Animated dots during AI response generation
   - **Message Animations**: Smooth slide-in effects for chat messages

## 📸 Screenshots

### Light Theme UI
Experience the clean, modern light theme with professional blue gradients and glass morphism effects:

| Screenshot | Description |
|------------|-------------|
| ![Light UI 1](ScreenShots/Light%20UI/1.png) | **Hero Section** - Welcome screen with animated AI orb and call-to-action buttons |
| ![Light UI 2](ScreenShots/Light%20UI/2.png) | **Features Section** - Showcase of AI capabilities with glass effect cards |
| ![Light UI 3](ScreenShots/Light%20UI/3.png) | **Chat Interface** - Real-time chat with AutoSphere AI assistant |
| ![Light UI 4](ScreenShots/Light%20UI/4.png) | **About Section** - Technology stack and application areas |
| ![Light UI 5](ScreenShots/Light%20UI/5.png) | **Footer** - Team information and project details |

### Dark Theme UI
Immerse yourself in the sophisticated dark theme with enhanced contrast and glowing effects:

| Screenshot | Description |
|------------|-------------|
| ![Dark UI 1](ScreenShots/Dark%20UI/1.png) | **Hero Section** - Dark mode welcome screen with glowing AI orb |
| ![Dark UI 2](ScreenShots/Dark%20UI/2.png) | **Features Section** - Dark theme feature cards with enhanced visibility |
| ![Dark UI 3](ScreenShots/Dark%20UI/3.png) | **Chat Interface** - Dark mode chat with improved contrast and readability |
| ![Dark UI 4](ScreenShots/Dark%20UI/4.png) | **About Section** - Dark theme technology showcase |
| ![Dark UI 5](ScreenShots/Dark%20UI/5.png) | **Footer** - Dark mode footer with glowing logo effects |

### Key Visual Features
- **Glass Morphism**: Translucent backgrounds with backdrop blur effects
- **Animated AI Orb**: Pulsing core with rotating rings and floating particles
- **Responsive Design**: Optimized layouts for desktop, tablet, and mobile
- **Smooth Transitions**: Professional animations and hover effects
- **Custom Branding**: AutoSphereAI logo integration throughout the interface

## 🎨 Design Features

### Glass Morphism Effects
- **Backdrop Blur**: 20px blur for authentic glass appearance
- **Translucent Backgrounds**: Semi-transparent elements with depth
- **Layered Shadows**: Multiple shadow layers for realistic depth
- **Inset Highlights**: White borders for glass-like shine
- **Smooth Transitions**: Animated effects for all interactions

### Color Palette
- **Primary Colors**: Deep blue gradient (#00072d to #a6e1fa)
- **Accent Colors**: Professional blue tones
- **Glass Effects**: White/transparent overlays
- **Dark Theme**: Enhanced contrast with bright white text
- **Light Theme**: Clean, modern appearance

### Typography
- **Modern Fonts**: Clean, readable typography
- **Gradient Text**: Beautiful color gradients for headings
- **Text Shadows**: Enhanced readability in dark theme
- **Responsive Sizing**: Scales appropriately across devices

## 🔧 Configuration

### Environment Variables (`config.env`)

```env
# IBM Cloud API Credentials
IBM_API_KEY=your_ibm_cloud_api_key_here
IBM_PROJECT_ID=your_project_id_here
IBM_URL=https://us-south.ml.cloud.ibm.com

# Server Configuration
HOST=localhost
PORT=8000
DEBUG=True

# Model Configuration
MODEL_ID=ibm/granite-3-3-8b-instruct
MAX_TOKENS=2000
TEMPERATURE=0

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

### API Endpoints

- `GET /` - Serve frontend
- `POST /api/chat` - Process chat messages and return AI responses
- `GET /api/health` - Server health check and AI initialization status
- `POST /api/clear` - Clear conversation history on server

## 🚀 Deployment

### Development
```bash
# Quick start
python run.py

# Manual start
python autosphere_server.py
```

### Production
1. **Environment Setup**
   - Set production environment variables
   - Configure proper CORS origins
   - Enable HTTPS

2. **Server Deployment**
   - Use production WSGI server (Gunicorn, uWSGI)
   - Set up reverse proxy (Nginx)
   - Configure SSL certificates

3. **Frontend Deployment**
   - Build and optimize static files
   - Deploy to CDN for global distribution

## 🔧 Development

### Adding New Features
1. **Backend**: Add new endpoints in `autosphere_server.py`
2. **Frontend**: Update JavaScript in `script.js`
3. **Styling**: Modify CSS in `styles.css`
4. **Glass Effects**: Add backdrop-filter and transparency

### Testing
```bash
# Run startup checks
python run.py

# Test API endpoints
curl http://localhost:8000/api/health
```

## 🎯 Recent Updates

### Version 2.0 Features
- ✅ **ChatGPT-Style Interface**: Modern chat design with professional layout
- ✅ **Glass Morphism Effects**: Beautiful translucent interface elements
- ✅ **Custom Logo Integration**: AutoSphereAI branding throughout
- ✅ **Enhanced Dark Theme**: Improved visibility and contrast
- ✅ **Message Formatting**: Rich text support with markdown
- ✅ **Responsive Design**: Optimized for all screen sizes
- ✅ **Smooth Animations**: Professional transitions and effects

### UI/UX Improvements
- ✅ **Modern Color Palette**: Deep blue professional theme
- ✅ **Glass Effects**: Backdrop blur and transparency
- ✅ **Logo Alignment**: Perfect logo positioning in chat
- ✅ **Dark Theme Fixes**: High contrast headings and text
- ✅ **Chat Interface**: ChatGPT-style message bubbles
- ✅ **Theme Switching**: Smooth light/dark mode transitions

## 👥 Team

- **Vasantha Bhavishya**
- **Yatish Balaji G**
- **Vishal K R**

## 🤝 Contributing

This project was developed for the Gen AI India AI Hackathon. For contributions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly (frontend and backend)
5. Submit a pull request

### Development Guidelines
- Follow existing code style and conventions
- Add comments for complex logic
- Update documentation for new features
- Test on multiple browsers and devices
- Ensure accessibility compliance
- Maintain glass morphism design consistency

## 📄 License

This project is subject to the International License Agreement for Non-Warranted Programs (ILAN License). See the notebook for detailed licensing information.

## 🙏 Acknowledgments

- IBM Watson AI team for providing the foundation models
- Gen AI India AI Hackathon organizers
- LangChain and LangGraph communities
- Font Awesome for icons
- Google Fonts for typography

## 📞 Support

For questions or support regarding this project, please refer to:
- IBM Watson AI documentation
- LangGraph documentation
- Project abstract and hackathon materials
- GitHub issues for bug reports

## 🔮 Future Enhancements

### Planned Features
- **User Authentication**: Secure user accounts and preferences
- **Advanced Analytics**: Chat analytics and usage insights
- **Multi-language Support**: Hindi and other Indian languages
- **Voice Interface**: Speech-to-text and text-to-speech capabilities
- **Mobile App**: Native mobile applications for iOS and Android
- **Advanced Glass Effects**: More sophisticated morphism designs
- **Custom Themes**: User-defined color schemes and effects

### Technical Improvements
- **Performance Optimization**: Code splitting and lazy loading
- **Progressive Web App**: Offline functionality and app-like experience
- **Advanced Theming**: Custom theme builder with glass effects
- **Real-time Collaboration**: Multi-user chat sessions
- **API Rate Limiting**: Proper backend API management
- **Enhanced Animations**: More sophisticated CSS and JavaScript effects

---

**AutoSphere AI: Empowering automation through intelligent assistance for a better tomorrow.** 🚀

*Now featuring ChatGPT-style interface, glass morphism effects, and custom branding for a premium user experience.*"# AutoSphere-AI" 
