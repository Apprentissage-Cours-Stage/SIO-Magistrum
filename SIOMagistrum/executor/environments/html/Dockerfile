FROM alpine:3.19

RUN apk add --no-cache chromium nodejs npm

RUN adduser -D -u 1000 runner

WORKDIR /app
RUN npm init -y && npm install puppeteer-core@21.0.0

COPY run.js /app/run.js

USER runner

ENTRYPOINT ["node", "/app/run.js"]