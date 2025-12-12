FROM php:8.3-cli-alpine

RUN adduser -D -u 1000 runner

WORKDIR /code

USER runner

CMD ["php", "/code/main.php"]