FROM seldonio/seldon-core-s2i-python37:1.2.2

ENV MODEL_NAME Model
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

ENV SELDON_LOG_LEVEL INFO

COPY Model.py /microservice/

RUN pip install ray==0.8.6

CMD seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE --log-level $SELDON_LOG_LEVEL --workers 5
