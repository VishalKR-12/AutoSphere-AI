#!/usr/bin/env python3
"""
Health check script for AutoSphere AI
Tests the application locally before deployment
"""

import requests
import json
import sys
import os
from dotenv import load_dotenv

def test_local_server():
    """Test the local server if it's running"""
    try:
        response = requests.get('http://localhost:8000/api/health', timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Local server is running")
            print(f"   Status: {data.get('status')}")
            print(f"   AI Initialized: {data.get('ai_initialized')}")
            return True
        else:
            print(f"❌ Local server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Local server is not running")
        return False
    except Exception as e:
        print(f"❌ Error testing local server: {e}")
        return False

def test_environment():
    """Test environment configuration"""
    print("🔍 Checking environment configuration...")
    
    # Load environment variables
    load_dotenv('config.env')
    
    required_vars = ['IBM_API_KEY', 'IBM_PROJECT_ID']
    missing_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.startswith('your_'):
            missing_vars.append(var)
            print(f"❌ {var}: Not set or using placeholder value")
        else:
            print(f"✅ {var}: Set")
    
    if missing_vars:
        print(f"\n⚠️  Missing required environment variables: {', '.join(missing_vars)}")
        return False
    
    print("✅ Environment configuration looks good")
    return True

def test_dependencies():
    """Test if all required dependencies are available"""
    print("🔍 Checking dependencies...")
    
    required_modules = [
        'flask',
        'flask_cors',
        'dotenv',
        'langchain_ibm',
        'ibm_watsonx_ai',
        'langchain_core',
        'langgraph',
        'requests',
        'gunicorn'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}: Available")
        except ImportError:
            missing_modules.append(module)
            print(f"❌ {module}: Missing")
    
    if missing_modules:
        print(f"\n⚠️  Missing dependencies: {', '.join(missing_modules)}")
        print("Install with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are available")
    return True

def main():
    """Main health check function"""
    print("🏥 AutoSphere AI - Health Check")
    print("=" * 50)
    
    # Test dependencies
    deps_ok = test_dependencies()
    print()
    
    # Test environment
    env_ok = test_environment()
    print()
    
    # Test local server
    server_ok = test_local_server()
    print()
    
    # Summary
    print("📊 Health Check Summary")
    print("=" * 30)
    print(f"Dependencies: {'✅' if deps_ok else '❌'}")
    print(f"Environment:  {'✅' if env_ok else '❌'}")
    print(f"Local Server: {'✅' if server_ok else '❌'}")
    
    if deps_ok and env_ok:
        print("\n🎉 Ready for deployment!")
        print("Next steps:")
        print("1. Push your code to GitHub")
        print("2. Deploy to Render using the deployment guide")
        print("3. Set your environment variables in Render")
    else:
        print("\n⚠️  Please fix the issues above before deploying")
        sys.exit(1)

if __name__ == "__main__":
    main()
