# Thread-Process-Practice For OS Project1
開發平台 : MacBook Pro (Retina, 13-inch, Early 2015)   
&emsp;&emsp;&emsp;&emsp;&emsp;CPU : 2.7 GHz Dual-Core Intel Core i5   
&emsp;&emsp;&emsp;&emsp;&emsp;Memory : 8 GB 1867 MHz DDR3   
&emsp;&emsp;&emsp;&emsp;&emsp;Graphics : Intel Iris Graphics 6100 1536 MB   
&emsp;&emsp;&emsp;&emsp;&emsp;Storage : 256G SSD   

開發環境 : MacOs Catalina 
&emsp;&emsp;&emsp;&emsp;&emsp;IDE : Visual Studio Code

程式語言 : Python

程式設計功能 :  
能夠input並output檔案
做bubble sort並merge成一個檔案
用thread進行bubble sort&merge
用multiprocess進行bubble sort&merge
計時並輸出CPU Process Time

程式設計流程 : 
Main:
設計輸入檔案名稱，已開啟某個檔案
用while迴圈設計使用者介面，說明 ‘請輸入檔案名稱or輸入0離開’
開啟檔案並讀入第一行判斷執行哪個任務
進入該任務function並執行

任務一：
直接進行bubble sort
排完後開檔寫檔
寫入process time
印出process time

任務二：
輸入要切幾份
進入CutArray切input data，切成需要的份數
宣告thread，看data有幾個thread就有幾份
執行每個thread ->進入BubbleSort去做排序
執行每個thread ->進入ListMerge去做合併
等待每個thread結束
merge完結果寫入process time
印出process time

任務三：
使用with mp.Manager as Manager() 的process管理器
設立ProcessList來共享data
輸入要切幾份
進入CutArrayForProcess切input data，切成需要的份數放入ProcessList
宣告Multiprocess，看data有幾個process就有幾份
執行每個process ->進入BubbleSortForProcess去做排序
執行每個process ->進入ListMergeForProcess去做合併
在ListMerge內把merge結果用Multiprocess.Queue()存起來當作share memory的地方才能讓CPU之間進行交流
把queue裡的結果存回ProcessList內
等待每個process結束
merge完結果寫入process time
印出process time

任務四：
輸入要切幾份
進入CutArray切input data，切成需要的份數
每份data進行bubble sort
進入ListMerge去做合併
merge完結果寫入process time
印出process time
	

程式設計Data Structure : 
data = []
intList = []
ProcessList = mp.Manager().list()
threadGroup = []
thread = threading.Thread( target = BubbleSort, args= (intList[i],) )
processGroup = []
tempQueue = mp.Queue()
process = mp.Process( target = BubbleSortForProcess, args= ( ProcessList[i], tempQueue ) )


程式未完成功能：
無
