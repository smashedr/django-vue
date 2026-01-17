FROM node:24 AS builder
WORKDIR /web
COPY web .
RUN npm ci && npm run build


FROM nginx:alpine-slim

LABEL org.opencontainers.image.source="https://github.com/smashedr/django-vue"
LABEL org.opencontainers.image.description="Django Vue"
LABEL org.opencontainers.image.authors="smashedr"

ENV TZ=UTC

RUN apk add --no-cache curl

COPY --from=builder /web/dist /html

COPY nginx/nginx.conf /etc/nginx/nginx.conf
