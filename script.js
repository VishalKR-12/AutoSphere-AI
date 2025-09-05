// AutoSphere AI - Frontend JavaScript

class AutoSphereAI {
    constructor() {
        this.conversationHistory = [];
        this.isConnected = false;
        this.currentTheme = 'light';
        this.apiBaseUrl = window.location.origin; // Use same origin for API calls
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadTheme();
        this.setupNavigation();
        this.initializeChat();
        this.checkServerHealth();
    }

    setupEventListeners() {
        // Theme toggle
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', () => this.toggleTheme());
        }

        // Navigation
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                this.navigateToSection(link.getAttribute('href').substring(1));
            });
        });

        // Chat functionality
        const startChatBtn = document.getElementById('start-chat');
        if (startChatBtn) {
            startChatBtn.addEventListener('click', () => this.scrollToChat());
        }

        const sendBtn = document.getElementById('send-btn');
        const chatInput = document.getElementById('chat-input');
        
        if (sendBtn && chatInput) {
            sendBtn.addEventListener('click', () => this.sendMessage());
            chatInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    this.sendMessage();
                }
            });
        }

        // Chat actions
        const clearChatBtn = document.getElementById('clear-chat');
        if (clearChatBtn) {
            clearChatBtn.addEventListener('click', () => this.clearChat());
        }

        const exportChatBtn = document.getElementById('export-chat');
        if (exportChatBtn) {
            exportChatBtn.addEventListener('click', () => this.exportChat());
        }

        // Learn more button
        const learnMoreBtn = document.getElementById('learn-more');
        if (learnMoreBtn) {
            learnMoreBtn.addEventListener('click', () => this.scrollToFeatures());
        }

        // Modal functionality
        this.setupModals();
    }

    setupNavigation() {
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Active navigation highlighting
        window.addEventListener('scroll', () => {
            this.updateActiveNavigation();
        });
    }

    updateActiveNavigation() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');
        
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    }

    toggleTheme() {
        this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', this.currentTheme);
        localStorage.setItem('autosphere-theme', this.currentTheme);
        
        // Update theme toggle icon
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            const icon = themeToggle.querySelector('i');
            if (icon) {
                icon.className = this.currentTheme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
            }
        }
    }

    loadTheme() {
        const savedTheme = localStorage.getItem('autosphere-theme') || 'light';
        this.currentTheme = savedTheme;
        document.documentElement.setAttribute('data-theme', this.currentTheme);
        
        // Update theme toggle icon
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            const icon = themeToggle.querySelector('i');
            if (icon) {
                icon.className = this.currentTheme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
            }
        }
    }

    scrollToChat() {
        const chatSection = document.getElementById('chat');
        if (chatSection) {
            chatSection.scrollIntoView({ behavior: 'smooth' });
            // Focus on chat input
            setTimeout(() => {
                const chatInput = document.getElementById('chat-input');
                if (chatInput) {
                    chatInput.focus();
                }
            }, 500);
        }
    }

    scrollToFeatures() {
        const featuresSection = document.getElementById('features');
        if (featuresSection) {
            featuresSection.scrollIntoView({ behavior: 'smooth' });
        }
    }

    async checkServerHealth() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/api/health`);
            const data = await response.json();
            
            if (data.status === 'healthy') {
                this.isConnected = true;
                this.updateStatus('Connected', 'success');
                console.log('✅ Server is healthy, AI initialized:', data.ai_initialized);
            } else {
                this.updateStatus('Server Error', 'error');
            }
        } catch (error) {
            console.warn('⚠️ Server health check failed:', error);
            this.updateStatus('Disconnected', 'warning');
        }
    }

    updateStatus(status, type) {
        const statusText = document.getElementById('status-text');
        const statusIndicator = document.getElementById('status-indicator');
        
        if (statusText) {
            statusText.textContent = status;
        }
        
        if (statusIndicator) {
            statusIndicator.className = `status-indicator ${type}`;
        }
    }

    initializeChat() {
        // Add welcome message if no messages exist
        const chatMessages = document.getElementById('chat-messages');
        if (chatMessages && chatMessages.children.length === 0) {
            this.addMessage('bot', 'Hi, I am AutoSphere AI. How can I help you today? I\'m here to assist with automation, provide intelligent solutions, and help you achieve more with AI-powered assistance.');
        }
    }

    async sendMessage() {
        const chatInput = document.getElementById('chat-input');
        const message = chatInput.value.trim();
        
        if (!message) return;

        // Add user message to chat
        this.addMessage('user', message);
        chatInput.value = '';

        // Show typing indicator
        this.showTypingIndicator();

        try {
            // Send message to backend API
            const response = await this.sendToAPI(message);
            
            // Remove typing indicator and add bot response
            this.hideTypingIndicator();
            this.addMessage('bot', response);
            
        } catch (error) {
            this.hideTypingIndicator();
            this.addMessage('bot', 'Sorry, I encountered an error. Please try again or check your connection.');
            console.error('Chat error:', error);
        }
    }

    addMessage(sender, content) {
        const chatMessages = document.getElementById('chat-messages');
        if (!chatMessages) return;

        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        if (sender === 'bot') {
            const logoImg = document.createElement('img');
            logoImg.src = 'AutoSphereAI Logo.png';
            logoImg.alt = 'AutoSphere AI Logo';
            logoImg.className = 'message-logo';
            avatar.appendChild(logoImg);
        } else {
            avatar.innerHTML = '<i class="fas fa-user"></i>';
        }
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        const messageText = document.createElement('div');
        messageText.className = 'message-text';
        
        // Format bot messages with markdown-like formatting
        if (sender === 'bot') {
            messageText.innerHTML = this.formatBotMessage(content);
        } else {
            messageText.textContent = content;
        }
        
        const messageTime = document.createElement('div');
        messageTime.className = 'message-time';
        messageTime.textContent = this.getCurrentTime();
        
        messageContent.appendChild(messageText);
        messageContent.appendChild(messageTime);
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        // Store in conversation history
        this.conversationHistory.push({
            role: sender,
            content: content,
            timestamp: new Date().toISOString()
        });
    }

    showTypingIndicator() {
        const chatMessages = document.getElementById('chat-messages');
        if (!chatMessages) return;

        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.id = 'typing-indicator';
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = '<i class="fas fa-robot"></i>';
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
        
        typingDiv.appendChild(avatar);
        typingDiv.appendChild(messageContent);
        chatMessages.appendChild(typingDiv);
        
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    async clearChat() {
        try {
            // Call backend to clear conversation
            await fetch(`${this.apiBaseUrl}/api/clear`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        } catch (error) {
            console.warn('Failed to clear conversation on server:', error);
        }
        
        // Clear frontend
        const chatMessages = document.getElementById('chat-messages');
        if (chatMessages) {
            chatMessages.innerHTML = '';
            this.conversationHistory = [];
            this.initializeChat();
        }
    }

    exportChat() {
        if (this.conversationHistory.length === 0) {
            alert('No chat history to export.');
            return;
        }

        const chatData = {
            title: 'AutoSphere AI Chat Export',
            timestamp: new Date().toISOString(),
            messages: this.conversationHistory
        };

        const blob = new Blob([JSON.stringify(chatData, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `autosphere-chat-${new Date().toISOString().split('T')[0]}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    formatBotMessage(content) {
        // Basic markdown-like formatting for bot messages
        let formatted = content
            // Bold text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            // Italic text
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            // Code blocks
            .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
            // Inline code
            .replace(/`(.*?)`/g, '<code>$1</code>')
            // Line breaks
            .replace(/\n/g, '<br>')
            // Lists
            .replace(/^\d+\.\s(.+)$/gm, '<li>$1</li>')
            .replace(/^[-*]\s(.+)$/gm, '<li>$1</li>')
            // Headers
            .replace(/^###\s(.+)$/gm, '<h3>$1</h3>')
            .replace(/^##\s(.+)$/gm, '<h2>$1</h2>')
            .replace(/^#\s(.+)$/gm, '<h1>$1</h1>')
            // Links
            .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
        
        // Wrap list items in ul tags
        formatted = formatted.replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>');
        
        return formatted;
    }

    // API Integration Methods
    async sendToAPI(message) {
        try {
            const response = await fetch(`${this.apiBaseUrl}/api/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    conversation_history: this.conversationHistory
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                return data.response;
            } else {
                throw new Error(data.error || 'Unknown error');
            }
        } catch (error) {
            console.error('API call failed:', error);
            
            // Fallback to simulated response if API is not available
            if (!this.isConnected) {
                return this.simulateAPIResponse(message);
            }
            
            throw error;
        }
    }

    // Fallback simulated response (for when API is not available)
    async simulateAPIResponse(message) {
        // Simulate network delay
        await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 2000));
        
        // Simple response logic based on keywords
        const lowerMessage = message.toLowerCase();
        
        if (lowerMessage.includes('hello') || lowerMessage.includes('hi')) {
            return 'Hello! I\'m AutoSphere AI, your intelligent automation assistant. How can I help you today?';
        } else if (lowerMessage.includes('agriculture') || lowerMessage.includes('farming')) {
            return 'I can help you with agriculture automation solutions! This includes crop monitoring, yield prediction, irrigation management, and precision farming techniques. Would you like to know more about any specific aspect?';
        } else if (lowerMessage.includes('healthcare') || lowerMessage.includes('medical')) {
            return 'For healthcare automation, I can assist with patient data management, appointment scheduling, medical record analysis, and diagnostic support systems. What specific healthcare automation are you interested in?';
        } else if (lowerMessage.includes('education') || lowerMessage.includes('learning')) {
            return 'Education automation can include personalized learning paths, automated grading, content generation, and student progress tracking. How can I help you implement educational technology solutions?';
        } else if (lowerMessage.includes('automation') || lowerMessage.includes('workflow')) {
            return 'I specialize in end-to-end workflow automation! I can help you identify automation opportunities, design efficient processes, and implement solutions that save time and reduce costs. What workflow would you like to optimize?';
        } else if (lowerMessage.includes('india') || lowerMessage.includes('indian')) {
            return 'As an India-centric AI platform, I\'m designed to address local challenges and opportunities. I can help with solutions tailored for Indian markets, including language support, cultural considerations, and local regulatory compliance.';
        } else {
            return 'Thank you for your message! I\'m AutoSphere AI, designed to help with automation, assistance, and achievement. I can help with agriculture, healthcare, education, and general workflow optimization. What would you like to explore?';
        }
    }

    setupModals() {
        // Settings modal
        const settingsModal = document.getElementById('settings-modal');
        const closeSettings = document.getElementById('close-settings');
        const cancelSettings = document.getElementById('cancel-settings');
        const saveSettings = document.getElementById('save-settings');

        if (closeSettings) {
            closeSettings.addEventListener('click', () => this.closeModal('settings-modal'));
        }

        if (cancelSettings) {
            cancelSettings.addEventListener('click', () => this.closeModal('settings-modal'));
        }

        if (saveSettings) {
            saveSettings.addEventListener('click', () => this.saveSettings());
        }

        // Close modal when clicking outside
        if (settingsModal) {
            settingsModal.addEventListener('click', (e) => {
                if (e.target === settingsModal) {
                    this.closeModal('settings-modal');
                }
            });
        }
    }

    openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    }

    saveSettings() {
        const apiKey = document.getElementById('api-key').value;
        const projectId = document.getElementById('project-id').value;
        const theme = document.getElementById('theme-select').value;

        // Save settings to localStorage
        localStorage.setItem('autosphere-api-key', apiKey);
        localStorage.setItem('autosphere-project-id', projectId);
        localStorage.setItem('autosphere-theme', theme);

        // Apply theme
        this.currentTheme = theme;
        document.documentElement.setAttribute('data-theme', theme);

        this.closeModal('settings-modal');
        alert('Settings saved successfully!');
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    const app = new AutoSphereAI();
    
    // Add typing animation CSS
    const style = document.createElement('style');
    style.textContent = `
        .typing-dots {
            display: flex;
            gap: 4px;
            align-items: center;
        }
        
        .typing-dots span {
            width: 8px;
            height: 8px;
            background-color: var(--text-muted);
            border-radius: 50%;
            animation: typing 1.4s infinite ease-in-out;
        }
        
        .typing-dots span:nth-child(1) { animation-delay: -0.32s; }
        .typing-dots span:nth-child(2) { animation-delay: -0.16s; }
        
        @keyframes typing {
            0%, 80%, 100% {
                transform: scale(0.8);
                opacity: 0.5;
            }
            40% {
                transform: scale(1);
                opacity: 1;
            }
        }
        
        .status-indicator.success {
            background-color: var(--success-color);
        }
        
        .status-indicator.warning {
            background-color: var(--warning-color);
        }
        
        .status-indicator.error {
            background-color: var(--error-color);
        }
    `;
    document.head.appendChild(style);
});

// Add smooth scrolling polyfill for older browsers
if (!('scrollBehavior' in document.documentElement.style)) {
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/smoothscroll-polyfill@0.4.4/dist/smoothscroll.min.js';
    document.head.appendChild(script);
}

// Add intersection observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.feature-card, .app-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});
