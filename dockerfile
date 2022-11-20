FROM python:3.6
WORKDIR /app
ADD . /app
RUN python3 -m pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py" ]

