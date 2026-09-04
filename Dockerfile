FROM python:3.11-slim

WORKDIR /valorant-project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY constants/ ./constants/
COPY entities/ ./entities/
COPY logger/ ./logger/
COPY pipeline/ ./pipeline/
COPY src/ ./src/
COPY utils/ ./utils/

CMD ["python", "-m", "pipeline.scraper_pipeline"]