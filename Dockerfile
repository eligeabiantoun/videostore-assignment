FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (kept minimal; Pillow uses wheels on slim)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tini \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project last (better layer caching while you iterate on requirements)
COPY . /app/

# Use tini as PID 1 for signal handling
RUN chmod +x /app/videostore/entrypoint.sh

# runs migrations then starts Django
CMD ["./videostore/entrypoint.sh"]

EXPOSE 8000
