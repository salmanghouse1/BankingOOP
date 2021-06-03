class AwesomeRange:


    def __init__(self,start,stop,step=1):
        self.start=start
        self.stop=stop
        self.step=step
        self.current_value=start-step

    def __iter__(self):
        return self

    def __next__(self):
        self.current_value+=self.step


        if self.current_value >=self.stop:
            raise StopIteration

        return self.current_value
