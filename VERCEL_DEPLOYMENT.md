# Vercel Deployment Guide

This guide will help you deploy the LLM Council application to Vercel.

## Prerequisites

1. A GitHub account with this repository
2. A Vercel account (sign up at https://vercel.com)
3. An OpenRouter API key

## Deployment Steps

### 1. Push to GitHub

Make sure all your changes are committed and pushed to GitHub:

```bash
git add .
git commit -m "Configure for Vercel deployment"
git push origin main
```

### 2. Connect to Vercel

1. Go to https://vercel.com and sign in
2. Click "Add New Project"
3. Import your GitHub repository: `ishimwekevinfounder/llm_council`
4. Vercel will auto-detect the configuration

### 3. Configure Environment Variables

In the Vercel project settings, add the following environment variable:

- **OPENROUTER_API_KEY**: Your OpenRouter API key (starts with `sk-or-v1-...`)

You can find this in the "Environment Variables" section of your project settings.

### 4. Deploy

Click "Deploy" and Vercel will:
- Install frontend dependencies
- Build the React app
- Set up the Python serverless functions
- Deploy everything

## Important Notes

### Storage Limitation

⚠️ **Current Limitation**: The application uses file-based storage (`/tmp/data/conversations` in serverless), which is **ephemeral**. This means:
- Conversations are stored in memory/temporary storage
- Data will be lost when serverless functions restart
- For production use, consider migrating to:
  - Vercel KV (Redis)
  - A database (PostgreSQL, MongoDB, etc.)
  - Vercel Blob Storage

### API Routes

The backend API is available at `/api/*` routes:
- `/api/conversations` - List conversations
- `/api/conversations/{id}` - Get conversation
- `/api/conversations/{id}/message` - Send message
- `/api/conversations/{id}/message/stream` - Stream message response

### Custom Domain

After deployment, you can add a custom domain in Vercel project settings.

## Troubleshooting

### Build Fails

- Check that `requirements.txt` includes all dependencies
- Verify `mangum` is included (required for FastAPI on Vercel)
- Check build logs in Vercel dashboard

### API Not Working

- Verify `OPENROUTER_API_KEY` is set in environment variables
- Check that the API routes are accessible at `/api/*`
- Review serverless function logs in Vercel dashboard

### Frontend Can't Connect to API

- Ensure the frontend uses relative URLs (`/api` instead of `http://localhost:8001`)
- Check CORS settings in `backend/main.py`

## Local Development

For local development, continue using:

```bash
# Terminal 1 - Backend
uv run python -m backend.main

# Terminal 2 - Frontend
cd frontend && npm run dev
```

The frontend will automatically use `http://localhost:8001` for API calls in development mode.

