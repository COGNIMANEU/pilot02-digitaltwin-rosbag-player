FROM ros:humble

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    ros-humble-rosbag2 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install --no-cache-dir rospkg

# Create a working directory and copy files
WORKDIR /usr/src/app
COPY ./ /usr/src/app/src

# Use bash to source the ROS setup and install dependencies
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && \
    rosdep update && \
    rosdep install --from-paths /usr/src/app/src --ignore-src -r -y"

# Set the entrypoint to run the rosbag generator script
CMD ["python3", "/usr/src/app/src/rosbag_generator.py"]
