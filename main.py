import sys
import signal
import argparse
import subprocess
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent


# Function for parsing all available monitors
def parse_monitors():
    all_monitors = subprocess.check_output(['xrandr', '--listactivemonitors'])
    all_monitors = all_monitors.decode('UTF-8')
    all_monitors = all_monitors.splitlines()
    all_monitors = [line.strip() for line in all_monitors]
    return all_monitors[1:]


class Monitor:
    def __init__(self, string):
        self.string = string.strip()
        self.id = None
        self.height = None
        self.width = None
        self.X = None
        self.Y = None

        self.parse_id()
        self.parse_height_and_width()
        self.parse_x_and_y()

    def parse_id(self):
        temp_string = self.string.split()
        self.id = int(temp_string[0][0])
    
    def parse_height_and_width(self):
        temp_string = self.string.split()
        temp_string = temp_string[2].split('/')
        self.width = temp_string[0]
        self.height = temp_string[1].split('x')[1]
    
    def parse_x_and_y(self):
        temp_string = self.string.split()
        temp_string = temp_string[2].split('/')
        temp_string = temp_string[2].split('+')
        self.X = temp_string[1]
        self.Y = temp_string[2]
    
    def __str__(self):
        return self.string
    
    def __repr__(self):
        return self.string


class Main:

    # On which line we should render list of monitors
    MONITORS_BASE_LINE = 5

    # I use green because it looks nice. Change color here if you want so
    DEFAULT_COLOR = Screen.COLOUR_GREEN

    # Setting up base variables for a screen and a config file
    def __init__(self, screen, args):

        # Catch Ctrl-C
        signal.signal(signal.SIGINT, self.exit)

        self.screen = screen
        self.fps_rate = args.fps_rate

        # Parse all available monitors and pass it to the monitor class
        self.monitors = parse_monitors()
        self.monitors = [Monitor(monitor) for monitor in self.monitors]

        # Set active monitor, default is None, although user can run emulation manualy
        self.active_monitor = 0

        # Emulating related stuff
        self.emulating_proccess = None
        self.emulating_monitor = None

        # Display welcoming message
        self.welcoming_message()
        # And list of all available monitors
        self.display_monitors()

        self.screen.refresh()
        self.wait_for_input()
    
    def welcoming_message(self):

        self.screen.print_at(
            '* Select a monitor you want to share', 0, 0, self.DEFAULT_COLOR
        )
        self.screen.print_at(
            '====================================', 0, 1, self.DEFAULT_COLOR
        )

        self.screen.print_at(
            'Monitor currently emulating:', 0, 3, self.DEFAULT_COLOR
        )

        self.screen.print_at(
            'nothing is emulating at the moment', 29, 3, Screen.COLOUR_YELLOW
        )

    def display_monitors(self):
        current_line = self.MONITORS_BASE_LINE

        for monitor in self.monitors:
            pointer = '  '
            if self.active_monitor == monitor.id:
                pointer = '> '
            self.screen.print_at(
                pointer + str(monitor), 0, current_line, self.DEFAULT_COLOR
            )
            current_line += 1
            self.screen.refresh()
    
    def wait_for_input(self):
        while True:
            event = self.screen.get_event()
            if event is not None and isinstance(event, KeyboardEvent):
                if event.key_code == 10:
                    self.emulate()
                if event.key_code == -206:
                    self.change_active()
                if event.key_code == -204:
                    self.change_active(next=False)
                self.screen.refresh()
    
    def change_active(self, next=True):
        if next and self.active_monitor < len(self.monitors)-1:
            self.active_monitor += 1
        if not next and self.active_monitor > 0:
            self.active_monitor -= 1
        self.display_monitors()
    
    def update_status(self):
        self.screen.print_at(
            str(self.emulating_monitor), 29, 3, Screen.COLOUR_YELLOW
        )
        self.screen.refresh()
    
    def emulate(self):
        if self.emulating_proccess is not None:
            self.emulating_proccess.terminate()
            self.emulating_proccess = None
        monitor = self.monitors[self.active_monitor]
        self.emulating_proccess = subprocess.Popen(
            'ffmpeg -hide_banner -loglevel panic -f x11grab -r {} -s "{}"x"{}" -i $DISPLAY+"{}","{}" -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video4'.format(
                self.fps_rate, monitor.width, monitor.height, monitor.X, monitor.Y
            ),
            shell=True,
            stdout=subprocess.DEVNULL
        )
        self.emulating_monitor = monitor
        self.update_status()

    def exit(self, *args):
        print('Finishing...')
        if self.emulating_proccess is not None:
            self.emulating_proccess.terminate()
        subprocess.run(['reset'])
        sys.exit(0)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description='Helps stream desktop in Discord through virtual cams')
    parser.add_argument('--fps', dest='fps_rate', default="60", help="Sets FPS rate (default is 60)")
    args = parser.parse_args()
    # Probing v4l2loopback
    subprocess.run('sudo modprobe v4l2loopback video_nr=4 \'card_label=VirtualScreen\'', shell=True)
    Screen.wrapper(Main, arguments=(args, ))
