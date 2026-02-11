# Deploy to Render - 3S Smart Software Solution

## Prerequisites
- GitHub account
- Render account (free tier available at https://render.com)
- This repository pushed to GitHub

## Deployment Steps

### 1. Push Your Code to GitHub

```bash
# If not already initialized
git init
git add .
git commit -m "Prepare for Render deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 2. Deploy on Render

#### Option A: Using render.yaml (Recommended)

1. Go to https://dashboard.render.com
2. Click "New +" → "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml` and set up:
   - Web Service (Flask app)
   - PostgreSQL Database
5. Click "Apply" to deploy

#### Option B: Manual Setup

1. **Create PostgreSQL Database:**
   - Go to https://dashboard.render.com
   - Click "New +" → "PostgreSQL"
   - Name: `3s-database`
   - Database: `sss_db`
   - User: `sss_admin`
   - Plan: Free
   - Click "Create Database"
   - Copy the "Internal Database URL"

2. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name:** `3s-smart-solution`
     - **Runtime:** Python 3
     - **Build Command:** `./build.sh`
     - **Start Command:** `gunicorn app:app`
     - **Plan:** Free

3. **Add Environment Variables:**
   - Click "Environment" tab
   - Add:
     - `DATABASE_URL` = (paste Internal Database URL from step 1)
     - `SECRET_KEY` = (generate random string, e.g., use `python -c "import secrets; print(secrets.token_hex(32))"`)

4. Click "Create Web Service"

### 3. First Time Setup

After deployment completes (5-10 minutes):

1. Visit your app URL (e.g., `https://3s-smart-solution.onrender.com`)
2. The database will auto-initialize with default admin user
3. Login at: `https://YOUR_APP.onrender.com/login`
   - **Username:** `shalaby`
   - **Password:** `shalaby`
4. **IMPORTANT:** Change the admin password immediately!

### 4. Post-Deployment

- Your app URL will be: `https://YOUR_APP_NAME.onrender.com`
- Database is persistent (won't lose data on restarts)
- Free tier apps sleep after 15 minutes of inactivity
- First request after sleep may take 30-60 seconds

## Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | PostgreSQL connection string (auto-provided by Render) | Yes |
| `SECRET_KEY` | Flask secret key for sessions | Yes |
| `PYTHON_VERSION` | Python version (default: 3.9.6) | No |

## Troubleshooting

### Build Fails
- Check `build.sh` has executable permissions
- Verify `requirements.txt` is correct
- Check build logs in Render dashboard

### Database Connection Issues
- Verify `DATABASE_URL` environment variable is set
- Check database is running in Render dashboard
- Ensure internal database URL is used (not external)

### App Won't Start
- Check start command: `gunicorn app:app`
- Review application logs in Render dashboard
- Verify all environment variables are set

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally (uses SQLite)
python app.py

# Access at http://localhost:5000
```

## Support

For issues, check:
- Render documentation: https://render.com/docs
- Flask documentation: https://flask.palletsprojects.com/
- Application logs in Render dashboard
