FROM python:3.12-slim
#建立 Python 環境。不用依賴 Windows Python。


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/analysis.py"]