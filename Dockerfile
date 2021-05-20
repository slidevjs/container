FROM node:16-buster

LABEL maintainer="https://github.com/stig124"
LABEL upstream="https://github.com/slidevjs/slidev"
LABEL source="https://github.com/slidevjs/container"

WORKDIR /root

# Get the entrypoint script from the current directory
COPY --chown=root:root entrypoint.sh /root

#RUN apt-get update && apt-get install firefox-esr libnspr4  -y && apt-get clean

#Make the entrypoint script executable and install npm
RUN echo 'shamefully-flatten=true' >> .npmrc && chmod 700 entrypoint.sh && npm install -g pnpm

RUN pnpm add --global playwright-chromium

RUN pnpm add --global @slidev/cli @slidev/theme-default @slidev/client vue-template-compiler @antfu/utils

WORKDIR /root/slides

ENTRYPOINT [ "/root/entrypoint.sh" ]
