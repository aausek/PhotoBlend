import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='PhotoBlend')
        panel = wx.Panel(self)
        
        self.text_ctrl = wx.TextCtrl(panel, pos=(10, 30))
        my_btn = wx.Button(panel, label='Blend', pos=(10, 55))
        
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
