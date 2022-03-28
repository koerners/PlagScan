FROM alpine:latest

# dependencies
RUN apk update && apk upgrade && apk add --no-cache openjdk11-jre python3 git curl gnupg bash nss ncurses 
RUN ln -sf python3 /usr/bin/python
RUN python -m ensurepip --upgrade

COPY requirements.txt /

RUN pip3 install -r requirements.txt

RUN set -ex && apk --no-cache add sudo

# installing joern
RUN wget https://github.com/joernio/joern/releases/latest/download/joern-install.sh && chmod +x ./joern-install.sh && sudo ./joern-install.sh && joern

