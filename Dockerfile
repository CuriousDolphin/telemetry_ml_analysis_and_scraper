FROM python:3.10-slim-buster
COPY requirements.txt .
RUN pip install -q --no-cache-dir --upgrade -r requirements.txt
WORKDIR /notebooks
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]