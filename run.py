#!/usr/bin/env python3
"""
AutoSphere AI - Startup Script
Checks dependencies and starts the server
"""

import os
import sys
import subprocess
import importlib.util

def check_dependency(module_name, package_name=None):
    """Check if a Python module is available"""
    if package_name is None:
        package_name = module_name
    
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"❌ Missing dependency: {package_name}")
        return False
    else:
        print(f"✅ {package_name} - OK")
        return True

def install_dependencies():
    """Install missing dependencies"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_config():
    """Check if config file exists and has required values"""
    config_file = "config.env"
    
    if not os.path.exists(config_file):
        print(f"❌ Config file {config_file} not found!")
        print("📝 Creating config file with template values...")
        
        with open(config_file, 'w') as f:
            f.write("""# AutoSphere AI Environment Configuration
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

# CORS Configuration (for frontend-backend communication)
ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
""")
        print("✅ Config file created!")
        print("⚠️  Please update config.env with your IBM Cloud credentials before running the server.")
        return False
    
    # Check if credentials are set
    with open(config_file, 'r') as f:
        content = f.read()
        if 'your_ibm_cloud_api_key_here' in content or 'your_project_id_here' in content:
            print("⚠️  Please update config.env with your IBM Cloud credentials.")
            return False
    
    print("✅ Config file is properly configured!")
    return True

def main():
    """Main startup function"""
    print("🚀 AutoSphere AI - Startup Check")
    print("=" * 50)
    
    # Check dependencies
    print("🔍 Checking dependencies...")
    required_deps = [
        ('flask', 'Flask'),
        ('flask_cors', 'Flask-CORS'),
        ('dotenv', 'python-dotenv'),
        ('langchain_ibm', 'langchain_ibm'),
        ('ibm_watsonx_ai', 'ibm_watsonx_ai'),
        ('langchain_core', 'langchain_core'),
        ('langgraph', 'langgraph'),
        ('requests', 'requests')
    ]
    
    missing_deps = []
    for module, package in required_deps:
        if not check_dependency(module, package):
            missing_deps.append(package)
    
    if missing_deps:
        print(f"\n❌ Missing dependencies: {', '.join(missing_deps)}")
        response = input("Would you like to install missing dependencies? (y/n): ")
        if response.lower() in ['y', 'yes']:
            if not install_dependencies():
                print("❌ Failed to install dependencies. Please install them manually:")
                print(f"pip install {' '.join(missing_deps)}")
                return
        else:
            print("❌ Cannot start without required dependencies.")
            return
    
    # Check config
    print("\n🔍 Checking configuration...")
    if not check_config():
        print("\n📋 Next steps:")
        print("1. Update config.env with your IBM Cloud API key and project ID")
        print("2. Run: python autosphere_server.py")
        return
    
    # Start server
    print("\n🚀 Starting AutoSphere AI Server...")
    print("=" * 50)
    
    try:
        # Import and run the server
        from autosphere_server import main as run_server
        run_server()
    except ImportError as e:
        print(f"❌ Failed to import server: {e}")
        print("Please ensure all dependencies are installed.")
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user.")
    except Exception as e:
        print(f"❌ Server error: {e}")

if __name__ == "__main__":
    main()
