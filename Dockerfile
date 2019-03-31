FROM osrf/ros2:nightly

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install sudo -y  && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash dev
RUN echo "dev  ALL=(ALL:ALL) ALL" >> /etc/sudoers
RUN echo "dev:dev" | chpasswd 
# for gdbserver
EXPOSE 2000

USER dev
VOLUME "/home/dev/ros2_ws"
WORKDIR "/home/dev/ros2_ws"