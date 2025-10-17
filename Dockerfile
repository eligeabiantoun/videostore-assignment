FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Minimal OS deps (tini is optional but nice)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tini \
 && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt

# App code
COPY . /app/

# Make sure entrypoint is executable and has LF endings (avoid CRLF issues)
RUN chmod +x /app/videostore/entrypoint.sh && sed -i 's/\r$//' /app/videostore/entrypoint.sh

# (Optional) use tini as PID 1 for clean signals
ENTRYPOINT ["/usr/bin/tini", "--"]

# Run your app (entrypoint script calls manage.py inside videostore/)
CMD ["./videostore/entrypoint.sh"]

EXPOSE 8000
