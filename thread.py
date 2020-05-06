import threading
import time
from queue import Queue
import multiprocessing as mp


def BubbleSort( A ):
    n = len( A )
    for i in range( 0, n - 1 ):
        for j in range( i + 1, n ):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                
            
def ListMerge( intList ):
    L = intList.pop(0)
    R = intList.pop(0)
    temp = []
    while len(L) > 0 or len(R) > 0:
        if( len(L) == 0  ):
            temp.append( R.pop(0) )
        elif( len(R) == 0  ):
            temp.append( L.pop(0) )
        elif( L[0] < R[0]  ):
            temp.append( L.pop(0) )
        elif( L[0] > R[0]  ):
            temp.append( R.pop(0) )
        elif( L[0] == R[0]  ):
            temp.append( L.pop(0) )
            temp.append( R.pop(0) )

    
    intList.append( temp )
                           
def CutArray( num, data, intList ):
   
    cutLength = int( len(data) / num )
    
    for i in range(num):
        temp = []
        for _ in range(cutLength):
            temp.append( data.pop(0) )
            
        intList.append( temp )
        
            
def Task2( number, data, intList ):
    threadGroup = []
    CutArray( number, data, intList )
    for i in  range( number ):
        thread = threading.Thread( target = BubbleSort, args= (intList[i],) )
        thread.start()
        threadGroup.append( thread )
    
    for thread in threadGroup :
        thread.join()
    
    
    for i in range( number - 1 ):
        thread = threading.Thread( target = ListMerge, args=  (intList, ) )
        thread.start()
        threadGroup.append( thread )
        
    for thread in threadGroup :
        thread.join()
        

def Task3( number, data, intList ):
    processGroup = []
    CutArray( number, data, intList )
    for i in  range( number ):
        process = mp.Process( target = BubbleSort, args= (intList[i],) )
        process.start()
        processGroup.append( process )
    
    for process in processGroup :
        process.join()
    
    
    for i in range( number - 1 ):
        process = mp.Process( target = ListMerge, args=  (intList, ) )
        process.start()
        processGroup.append( process )
        
    for process in processGroup :
        process.join()
    
    
    
    
def Task4( number, data, intList ):
    CutArray( number, data, intList )
    for i in range( len(intList) ):
        BubbleSort( intList[i] )
    
    for _ in range( number -1 ):
        ListMerge( intList )

def main():
    
    data = []
    intList = []
    
    fileName = input('請輸入檔案名稱or輸入0離開\n')
    while fileName != "0" :
        f = open(fileName + '.txt', 'r')
        task = int( f.readline() )
       
        
        for n in f.read().split():
            data.append( int(n) )
            
        startTime = time.time()
        
        if task == 1:
            BubbleSort( data )
            print( intList )
            
        elif task == 2:
            number = int(input('請輸入份數:\n'))
            Task2( number, data, intList )
            print( intList )
 
        elif task == 3:
            number = int(input('請輸入份數:\n'))
            Task3( number, data, intList )
            print( intList )

            
        elif task == 4:
            number = int(input('請輸入份數:\n'))
            Task4( number, data, intList )
            print( intList )
            
        endTime = time.time()
        print( 'Sort Time = ', endTime - startTime, '\n' )
        
        f.close()
        fileName = input('請輸入檔案名稱or輸入0離開\n')
    print('bye')


if __name__ == '__main__':
    main()
    
    
    
    
    
