import csv

class GetTestData():
    def openDataFile(self,filename):
        self.file= open(filename, 'r')
        return self.file

    def getData(self,openfile):
        self.data=csv.reader(openfile)
        self.mydata=[]
        '''
        if len(self.data)==0:
            print("存储测试的数据文件是空的，请在里面存放一定数量的测试数据！")
            return 0
        else:
            for item in self.data:
                self.mydata.append(item)
            return self.mydata
        '''
        for item in self.data:
            self.mydata.append(item)
        return self.mydata

if __name__=="__main__":
    getdata=GetTestData()
    file=getdata.openDataFile("E:/Python/demo/csv/importData/zhengshuData.csv")
    zhengshuData=getdata.getData(file)
    for item in zhengshuData:
        print(item)