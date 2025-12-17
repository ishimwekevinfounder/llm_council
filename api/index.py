"""Vercel serverless function entry point for FastAPI backend."""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mangum import Mangum
from backend.main import app

# Wrap FastAPI app with Mangum for serverless
handler = Mangum(app, lifespan="off")

