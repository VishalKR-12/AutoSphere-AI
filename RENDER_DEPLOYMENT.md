# AutoSphere AI - Render Deployment Guide

This guide will help you deploy your AutoSphere AI application to Render.

## Prerequisites

1. **Render Account**: Sign up at [render.com](https://render.com)
2. **GitHub Repository**: Your code should be in a GitHub repository
3. **IBM Cloud Credentials**: You'll need your IBM API key and project ID

## Step 1: Prepare Your Repository

Your repository should contain these files (which are already created):
- `autosphere_server.py` - Main Flask application
- `autosphere_ai.py` - AI logic
- `requirements.txt` - Python dependencies
- `render.yaml` - Render configuration
- `Procfile` - Process configuration
- `index.html`, `styles.css`, `script.js` - Frontend files

## Step 2: Deploy to Render

### Option A: Using Render Dashboard (Recommended)

1. **Connect GitHub**:
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" → "Web Service"
   - Connect your GitHub account if not already connected
   - Select your AutoSphere AI repository

2. **Configure Service**:
   - **Name**: `autosphere-ai` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT autosphere_server:app`

3. **Set Environment Variables**:
   - `IBM_API_KEY`: Your IBM Cloud API key
   - `IBM_PROJECT_ID`: Your IBM Cloud project ID
   - `IBM_URL`: `https://us-south.ml.cloud.ibm.com`
   - `HOST`: `0.0.0.0`
   - `DEBUG`: `False`
   - `MODEL_ID`: `ibm/granite-3-3-8b-instruct`
   - `MAX_TOKENS`: `2000`
   - `TEMPERATURE`: `0`
   - `ALLOWED_ORIGINS`: `*`

4. **Deploy**:
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Option B: Using render.yaml (Infrastructure as Code)

1. **Push to GitHub**: Make sure all files are committed and pushed to your repository

2. **Create Service**:
   - Go to Render Dashboard
   - Click "New +" → "Blueprint"
   - Connect your repository
   - Render will automatically detect the `render.yaml` file

3. **Set Secrets**:
   - In the service settings, add your environment variables:
     - `IBM_API_KEY`: Your actual API key
     - `IBM_PROJECT_ID`: Your actual project ID

## Step 3: Verify Deployment

1. **Check Build Logs**: Monitor the build process in Render dashboard
2. **Test Health Endpoint**: Visit `https://your-app-name.onrender.com/api/health`
3. **Test Frontend**: Visit `https://your-app-name.onrender.com`
4. **Test AI Chat**: Try sending a message through the web interface

## Step 4: Custom Domain (Optional)

1. **Add Custom Domain**:
   - Go to your service settings
   - Click "Custom Domains"
   - Add your domain name
   - Follow DNS configuration instructions

## Troubleshooting

### Common Issues

1. **Build Failures**:
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version compatibility
   - Check build logs for specific error messages

2. **Runtime Errors**:
   - Verify environment variables are set correctly
   - Check that IBM credentials are valid
   - Monitor application logs in Render dashboard

3. **CORS Issues**:
   - Ensure `ALLOWED_ORIGINS` is set to `*` for production
   - Check that your frontend is making requests to the correct URL

4. **AI Not Working**:
   - Verify IBM API credentials are correct
   - Check that the model ID is valid
   - Ensure your IBM Cloud account has access to the model

### Logs and Monitoring

- **Build Logs**: Available during deployment
- **Runtime Logs**: Available in the service dashboard
- **Health Check**: Use `/api/health` endpoint to verify service status

## Environment Variables Reference

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `IBM_API_KEY` | IBM Cloud API key | Yes | - |
| `IBM_PROJECT_ID` | IBM Cloud project ID | Yes | - |
| `IBM_URL` | IBM Cloud URL | No | `https://us-south.ml.cloud.ibm.com` |
| `HOST` | Server host | No | `0.0.0.0` |
| `PORT` | Server port | No | `8000` (auto-set by Render) |
| `DEBUG` | Debug mode | No | `False` |
| `MODEL_ID` | AI model to use | No | `ibm/granite-3-3-8b-instruct` |
| `MAX_TOKENS` | Maximum tokens | No | `2000` |
| `TEMPERATURE` | Model temperature | No | `0` |
| `ALLOWED_ORIGINS` | CORS origins | No | `*` |

## Cost Considerations

- **Free Tier**: 750 hours/month, sleeps after 15 minutes of inactivity
- **Starter Plan**: $7/month for always-on service
- **Professional Plan**: $25/month for production workloads

## Security Best Practices

1. **Environment Variables**: Never commit API keys to your repository
2. **HTTPS**: Render provides HTTPS by default
3. **CORS**: Configure appropriate origins for production
4. **API Keys**: Rotate IBM API keys regularly

## Support

- **Render Documentation**: [render.com/docs](https://render.com/docs)
- **IBM Watson Documentation**: [cloud.ibm.com/docs/watson](https://cloud.ibm.com/docs/watson)
- **Flask Documentation**: [flask.palletsprojects.com](https://flask.palletsprojects.com)

## Next Steps

After successful deployment:
1. Test all functionality thoroughly
2. Set up monitoring and alerts
3. Consider upgrading to a paid plan for production use
4. Implement additional security measures as needed
5. Set up automated deployments from your main branch
