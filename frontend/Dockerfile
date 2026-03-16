FROM klakegg/hugo:0.125.7-ext-alpine

WORKDIR /workspace/frontend/hugo-site

COPY frontend/hugo-site /workspace/frontend/hugo-site
COPY docs /workspace/docs

EXPOSE 1313

CMD ["hugo", "server", "--bind", "0.0.0.0", "--baseURL", "http://localhost:1313", "--disableFastRender"]
