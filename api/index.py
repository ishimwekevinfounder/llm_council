"""Vercel serverless function entry point for FastAPI backend."""

import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from mangum import Mangum
from backend.main import app

# Wrap FastAPI app with Mangum for serverless
# Vercel will call this handler for all /api/* routes
handler = Mangum(app, lifespan="off")

