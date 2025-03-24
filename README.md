# Pilot02 Digital Twin ROS2 Log Bag Player

This repository contains a docker based version to reproduce bag files.

The ROS 2 Bag Player is a software component designed to play back data stored in ROS 2 bag files. It allows users to replay sensor data, messages, and topics that were previously recorded in a ROS 2 environment. The component reads the bag file, which contains serialized message data, and publishes the messages to the corresponding ROS 2 topics as they were originally recorded.

The main function of the ROS 2 Bag Player is to simulate the real-time behavior of a system by playing back recorded messages at their original timestamps. It is useful for testing, debugging, and developing applications that require replaying real-world data without needing to interact with actual hardware or sensors. The component is integrated with the ROS 2 ecosystem and uses the `ros2 bag` command-line tool to handle the playback process.

## Description

The repository includes the following components:
- Sample bag file under config
- Docker setup for easy containerization
- A Docker Compose-based test environment to verify end-to-end functionality
- A bag generator to create a sample db3 file to perform end to end tests

## Guidelines for build and test the component 

### 1. **Build the Main Docker Image:**

In this step, we build the Docker image using the provided `Dockerfile`. The image is named `pilot02-digitaltwin-rosbag-player`.

```bash
docker build -t pilot02-digitaltwin-rosbag-player .
```
Make sure the path to your configuration file is correctly mapped to the Docker container.

### 2. **Run the ROS 2 Container:**

After building the Docker image, you can run the container using the following command:

```bash
docker run -e BAG_FILE_PATH=/usr/src/app/config/sample_bag.db3 pilot02-digitaltwin-rosbag-player
```

This will start the container and launch the Bag Player with the configuration given. Change the bag log filename if you want to play a different one.

### 3. **Build and Run the test automation:**

Test automation is integrated by docker-compose file:

Run: 
```bash
docker-compose up --build
```
In case the bag player is working, you should see:
```python
rosbag_player        | stdin is not a terminal device. Keyboard handling disabled.[INFO] [1742818971.627322532] [rosbag2_storage]: Opened database '/usr/src/app/config/sample_bag.db3' for READ_ONLY.
rosbag_player        | [INFO] [1742818971.646259230] [rosbag2_player]: Set rate to 1
rosbag_player        | [INFO] [1742818971.654507133] [rosbag2_player]: Adding keyboard callbacks.
rosbag_player        | [INFO] [1742818971.654590518] [rosbag2_player]: Press SPACE for Pause/Resume
rosbag_player        | [INFO] [1742818971.654605692] [rosbag2_player]: Press CURSOR_RIGHT for Play Next Message
rosbag_player        | [INFO] [1742818971.654617059] [rosbag2_player]: Press CURSOR_UP for Increase Rate 10%
rosbag_player        | [INFO] [1742818971.654627191] [rosbag2_player]: Press CURSOR_DOWN for Decrease Rate 10%
rosbag_player        | [INFO] [1742818971.672349532] [rosbag2_storage]: Opened database '/usr/src/app/config/sample_bag.db3' for READ_ONLY.
test_subscriber_2-1  | data: Example data for topic 2, counter 2
test_subscriber_2-1  | ---
test_subscriber_1-1  | data: Example data for topic 1, counter 2
test_subscriber_1-1  | ---
test_subscriber_2-1  | data: Example data for topic 2, counter 3
test_subscriber_2-1  | ---
test_subscriber_1-1  | data: Example data for topic 1, counter 3
test_subscriber_1-1  | ---
test_subscriber_2-1  | data: Example data for topic 2, counter 4
test_subscriber_2-1  | ---
test_subscriber_1-1  | data: Example data for topic 1, counter 4
test_subscriber_1-1  | ---
test_subscriber_2-1  | data: Example data for topic 2, counter 5
test_subscriber_2-1  | ---
test_subscriber_1-1  | data: Example data for topic 1, counter 5
test_subscriber_1-1  | ---
test_subscriber_1-1  | data: Example data for topic 1, counter 6
test_subscriber_1-1  | ---
test_subscriber_2-1  | data: Example data for topic 2, counter 6
test_subscriber_2-1  | ---
test_subscriber_1-1  | data: Example data for topic 1, counter 7
test_subscriber_1-1  | ---
test_subscriber_2-1  | data: Example data for topic 2, counter 7
```

## Player configuration

Add your db3 files into config folder.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

## License

This project is licensed under Apache License v2.0 - see the [LICENSE](LICENSE) file for details.