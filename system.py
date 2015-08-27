import video


class System():
    def __init__(self):
        self.__video_controller = video.VideoController()
        self.__video_controller.power_on()
