# PayPal Microfrontend Observability – Group 4

## Team Members
- Keerthana Garimella
- Preethi Jakhar
- Suman Kumari Jakhar

## Project Overview

This project demonstrates how to add observability to a microfrontend application using OpenTelemetry and the OpenTelemetry Collector. It uses a sample PayPal-style frontend to simulate real-world button click interactions and traces them using Python instrumentation.

---

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run OpenTelemetry Collector in Docker
```bash
docker run -p 4318:4318 -v "%cd%/otel-config.yaml:/etc/otel/config.yaml" otel/opentelemetry-collector:latest --config /etc/otel/config.yaml
```

### 3. Start the FastAPI Application
```bash
python -m uvicorn app:app --reload
```

### 4. Open the Web UI
Double click or open `index.html` in your browser. You should see a simple UI with a **"Pay with PayPal"** button.

### 5. Observe Tracing
When you click the **Pay with PayPal** button, telemetry data is generated. Traces will appear in the console and are exported to the OTEL collector via HTTP on port `4318`.

---

## Folder Structure

.
├── app.py
├── index.html
├── index.js
├── otel-config.yaml
├── requirements.txt
└── README.md