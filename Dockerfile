# Use the official ROS 2 Humble image as a base
FROM ros:humble

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    ros-humble-rosbag2 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory and copy files
WORKDIR /usr/src/app
COPY ./config /usr/src/app/config

# Set environment variable for the bag file path 
ENV BAG_FILE_PATH=/usr/src/app/config/sample_bag.db3 

# Set the default command to run the Python script
CMD ["bash", "-c", "source /opt/ros/humble/setup.bash && ros2 bag play \"$BAG_FILE_PATH\""]
