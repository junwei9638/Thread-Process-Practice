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
&emsp;1.能夠input並output檔案  
&emsp;2.做bubble sort並merge成一個檔案  
&emsp;3.用thread進行bubble sort&merge  
&emsp;4.用multiprocess進行bubble sort&merge   
&emsp;5.計時並輸出CPU Process Time    

程式設計流程 :   
Main:  
&emsp;1.設計輸入檔案名稱，已開啟某個檔案  
&emsp;2.用while迴圈設計使用者介面，說明 ‘請輸入檔案名稱or輸入0離開’   
&emsp;3.開啟檔案並讀入第一行判斷執行哪個任務  
&emsp;4.進入該任務function並執行  

任務一：  
&emsp;1.直接進行bubble sort  
&emsp;2.排完後開檔寫檔  
&emsp;3.寫入process time   
&emsp;4.印出process time   

任務二：
&emsp;1.輸入要切幾份    
&emsp;2.進入CutArray切input data，切成需要的份數  
&emsp;3.宣告thread，看data有幾個thread就有幾份  
&emsp;4.執行每個thread ->進入BubbleSort去做排序  
&emsp;5.執行每個thread ->進入ListMerge去做合併  
&emsp;6.等待每個thread結束  
&emsp;7.merge完結果寫入process time      
&emsp;8.印出process time  

任務三：
&emsp;1.使用with mp.Manager as Manager() 的process管理器   
&emsp;2.設立ProcessList來共享data   
&emsp;3.輸入要切幾份  
&emsp;4.進入CutArrayForProcess切input data，切成需要的份數放入ProcessList  
&emsp;5.宣告Multiprocess，看data有幾個process就有幾份  
&emsp;6.執行每個process ->進入BubbleSortForProcess去做排序  
&emsp;7.執行每個process ->進入ListMergeForProcess去做合併  
&emsp;8.在ListMerge內把merge結果用Multiprocess.Queue()存起來當作share memory的地方才能讓CPU之間進行交流  
&emsp;9.把queue裡的結果存回ProcessList內  
&emsp;10.等待每個process結束  
&emsp;11.merge完結果寫入process time  
&emsp;12.印出process time  

任務四：   
&emsp;1.輸入要切幾份  
&emsp;2.進入CutArray切input data，切成需要的份數  
&emsp;3.每份data進行bubble sort  
&emsp;4.進入ListMerge去做合併  
&emsp;5.merge完結果寫入process time  
&emsp;6.印出process time  
	

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
