import video


class System():

    def __init__(self):
        self.__video_controller = video.VideoController()

    def power_on(self):
        self.__video_controller.power_on()
