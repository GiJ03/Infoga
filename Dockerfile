FROM python
WORKDIR /opt/
ADD . .
RUN python setup.py install
RUN chmod +x infoga.py
ENTRYPOINT ["python","infoga.py"]
