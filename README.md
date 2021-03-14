# discord-monitors-to-vc

Stream any of your screens to a virtual camera. Designed specifically for Discord and Linux.

## Maintainance Note

This project is **not maintained** anymore, please use other solutions like [Mon2Cam](https://github.com/ShayBox/Mon2Cam).

## Table of Contents

1. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Install Binary Release](#install-binary-release)
   - [Running from Source](#running-from-source)
2. [Usage](#usage)
3. [License](#license)

## Installation

### Prerequisites

 - [ffmpeg](https://www.ffmpeg.org/)
 - [v4l2loopback](https://github.com/umlaeute/v4l2loopback)

### Install Binary Release

1. Go to [releases](https://github.com/TapO4eg3D/discord-monitors-to-vc/releases) and download the latest executable.
2. Open a terminal and navigate to the directory where you downloaded the file.
3. Change the permissions of the file to make it executable.

```
chmod +x discord-monitors-to-vc
```

4. Run the software.

```
./discord-monitors-to-vc
```

 - Releases are packed with PyInstaller, so release contains Python interpreter and all necessary libraries.

### Running from Source

1. Clone the repository

```
git clone https://github.com/TaPO4eg3D/discord-monitors-to-vc
```

2. Install the requirements and run the software.

```
pip install -r requirements.txt
python main.py
```

 - Optionally, you can run the software with a bash script.

```
./discord-monitors-to-vc
```

## Usage

Run the program:
```
./discord-monitors-to-vc
# or
python main.py
```

### Available Arguments

* --fps FPS_RATE - set the fps_rate of screen sharing. The default value is 60

You'll see the list of all monitors. Select the desired one by using **arrow keys** and hit **Enter**. 

When you've done, just press **Ctrl-C**

![image](https://user-images.githubusercontent.com/12825777/57574299-aaa2f700-7460-11e9-90f5-d14ed7ea1c9e.png)

## License

This product is licensed under the [MIT License](https://github.com/VidMig/VidMig/blob/main/LICENSE). This project is available for commercial use, modification, distribution, and private use.
