# A container = your code + everything it needs to run, sealed in one box that runs
# the same on your laptop and on the server. Read this top-to-bottom: it's a recipe.

FROM python:3.12-slim
# ^ start from a small, official Python image

WORKDIR /app
# ^ do everything inside the /app folder in the container

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# ^ copy ONLY the dependency list first and install it. Docker caches this step,
#   so it won't re-install everything every time you change your code. (A speed trick.)

COPY . .
# ^ now copy the rest of your code in

# Start the web server. 0.0.0.0 = "listen on all network interfaces" (required inside
# a container). Coolify maps port 8000 to your domain via Traefik + HTTPS.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
