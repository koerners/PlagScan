FROM ubuntu:20.04
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# os dependencies
RUN apt-get update && apt install -y default-jre wget python3 curl sudo unzip git

# python dependencies
RUN apt install -y python3-pip 
COPY requirements.txt /
RUN pip3 install -r requirements.txt

# installing joern
RUN wget https://github.com/joernio/joern/releases/latest/download/joern-install.sh && chmod +x ./joern-install.sh && sudo ./joern-install.sh && joern

# Use bash
RUN ln -s bash /bin/sh.bash && mv /bin/sh.bash /bin/sh