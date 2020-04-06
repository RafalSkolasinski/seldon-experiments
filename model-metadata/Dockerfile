FROM seldonio/seldon-core-s2i-python37:0.19-SNAPSHOT

ENV MODEL_NAME Model
ENV API_TYPE REST
ENV SERVICE_TYPE MODEL
ENV PERSISTENCE 0

COPY *.py /microservice/
CMD seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE --log-level DEBUG
