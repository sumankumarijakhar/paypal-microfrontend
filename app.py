from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import logging

app = FastAPI()

# Setup Logging
LoggingInstrumentor().instrument(set_logging_format=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup tracing
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "paypal-fastapi"})
    )
)

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

@app.get("/")
def read_root():
    logger.info("Root endpoint hit")
    return {"message": "PayPal FastAPI Service is running"}