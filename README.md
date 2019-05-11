# discord-monitors-to-vc
Stream any of your screens to a virtual camera. Designed specifically for Discord and Linux

# Dependencies
Before using make sure that you have **ffmpeg** and **v4l2loopback** installed 

# Installation
Just go to the "release" tab and grab the latest version.
Releases are packed with PyInstaller, so release contains Python interpreter and all necessary libraries.
That's why it has size more than 10 Mb, if you don't like that you can run it directly from the source:
```
pip install -r requirements.txt
python main.py
```

# Usage
Run the program:
```
./discord-monitors-to-vc
# or
python main.py
```

Available arguments:
* --fps FPS_RATE - set the fps_rate of screen sharing. The default value is 60

You'll see the list of all monitors. Select the desired one by using **arrow keys** and hit **Enter**. 

When you've done, just press **Ctrl-C**

![image](https://user-images.githubusercontent.com/12825777/57574299-aaa2f700-7460-11e9-90f5-d14ed7ea1c9e.png)
