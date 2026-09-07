FROM python:3.11-slim

WORKDIR /valorant-project

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY constants/ ./constants/
COPY entities/ ./entities/
COPY logger/ ./logger/
COPY pipeline/ ./pipeline/
COPY src/ ./src/
COPY utils/ ./utils/

COPY valorant/ ./dbt/

CMD ["python", "-m", "pipeline.scraper_pipeline"]