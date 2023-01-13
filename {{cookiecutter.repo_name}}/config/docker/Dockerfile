FROM python:3.9

ADD . /app
WORKDIR /app

RUN pip install --upgrade pip setuptools
RUN pip install -e ".[development]"
RUN python setup.py develop
RUN python setup.py install

EXPOSE ${BACKEND_PORT:-6543}

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:10001", "/usr/local/bin/gunicorn", "--paster", "development.ini", "-b", "0.0.0.0:${BACKEND_PORT:-6543}", "--reload"]

