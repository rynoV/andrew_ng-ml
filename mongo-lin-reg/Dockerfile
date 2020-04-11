FROM continuumio/miniconda3

# Utilize caching by keeping these together before the other copies
COPY requirements.txt /tmp/
RUN conda install --file /tmp/requirements.txt

WORKDIR "/app"
COPY ./src ./src
COPY ./data ./data

WORKDIR "/app/src"
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
