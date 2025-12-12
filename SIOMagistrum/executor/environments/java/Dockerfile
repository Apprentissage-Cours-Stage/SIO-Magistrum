FROM openjdk:21-rc-slim

RUN useradd -m -u 1000 runner

WORKDIR /code

COPY run.sh /run.sh
RUN chmod +x /run.sh

USER runner

ENTRYPOINT ["/run.sh"]