FROM klakegg/hugo:ext-alpine

WORKDIR /workspace/frontend/hugo-site

COPY frontend/hugo-site /workspace/frontend/hugo-site
COPY docs /workspace/docs

EXPOSE 1313

CMD ["server", "--bind", "0.0.0.0", "--baseURL", "http://localhost:1313", "--disableFastRender"]
