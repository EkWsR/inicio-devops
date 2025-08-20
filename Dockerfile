FROM ubuntu:latest
LABEL maintainer="EkWsR"
RUN apt update
RUN apt upgrade -y
RUN apt install -y openssh-server nano bash sudo
RUN mkdir /var/run/sshd
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash student
RUN echo "student:student"| chpasswd
RUN usermod -aG sudo student
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
