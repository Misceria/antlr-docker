FROM python3.8 AS builder
COPY requirements.txt .


RUN pip install --user -r requirements.txt

FROM python3.8-slim
WORKDIR /antlr-docker

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local:$PATH

CMD ["python", "-u", "main.py"]