FROM prefecthq/prefect:2.8.3-python3.11
COPY . /workspace
WORKDIR /workspace
COPY requirements-test.txt /
RUN pip install -r /requirements-test.txt
COPY docker-entrypoint.sh /workspace/docker-entrypoint.sh
RUN chmod +x /workspace/docker-entrypoint.sh
ENTRYPOINT ["/workspace/docker-entrypoint.sh"]