# Stage 1: Builder
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app
# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local
# Copy application code
COPY . .
# Set PATH to use local pip packag
ENV PATH=/root/.local/bin:$PATH
# set the entry point to run the application
ENTRYPOINT ["python"]