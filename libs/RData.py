import pandas as pd
import numpy as np
class RTKB(object):
    def __init__(self):
        self.data = pd.DataFrame()
        self.gvs = [""]
        self.mons = [""]
        self.lops = []
    def convert(self, data):
        """
        Chuyển đổi dữ liệu từ dataframe sang numpy array.
        """
        mon,gv=str(data).split('-')
        gv = gv.strip()
        mon = mon.strip()
        if gv not in self.gvs:
                self.gvs.append(gv)
        if mon not in self.mons:
                self.mons.append(mon)
        return self.mons.index(mon), self.gvs.index(gv)
    def read(self, path):
        """
        Đọc dữ liệu từ file excel và lưu vào dataframe.
        :param path: Đường dẫn đến file excel 
        """
        tkbs=np.zeros((19, 60,2), dtype=object)
        pcgd=[]
        self.data = pd.read_excel(path, sheet_name='TKBLop2b', header=0,na_values=['','N/A','missing'], 
                                   usecols='C:U', skiprows=7, nrows=61)
        self.data = self.data.fillna(' - ')
        for lop in self.data.columns:
            if lop not in self.lops:
                self.lops.append(lop)
            ilop = self.lops.index(lop)
            for tiet in self.data.index:
                mon, gv=self.convert(self.data[lop][tiet])
                tkbs[ilop][tiet] = [mon,gv]
            elements=np.unique(self.data[lop])
            print(f"Đã đọc {elements} từ lớp {lop}")
        return tkbs
    def get_gvs(self):
        """
        Trả về dữ liệu đã đọc từ file excel.
        :return: Dữ liệu đã đọc từ file excel
        """
        return self.gvs
    def get_lops(self):
        """
        Trả về danh sách các lớp học.
        """
        return self.lops
    def get_mons(self):
        """ 
        Trả về danh sách các môn học.
        """
        return self.mons
    
            
        
        