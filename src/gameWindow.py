

class Window:
    
    def __init__(self, width:int, height:int) -> None:
        self.width = width
        self.height = height
        self.bg_color = (50, 168, 133)
        self.x_color = (240, 5, 5)
        self.o_color = (5, 5, 240)

    
    def get_height(self) -> int:
        return self.height
    

    def set_height(self, height:int) -> None:
        self.height = height

    
    def get_width(self, width: int) -> int:
        return self.width
    

    def get_bg_color(self) -> tuple:
        return self.bg_color
    
    def get_width(self) -> int:
        return self.width
    
    def get_height(self) -> int:
        return self.height
    


