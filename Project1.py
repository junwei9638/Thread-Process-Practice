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
    
                
def BubbleSortForProcess( A, queue ):
    n = len( A )
    for i in range( 0, n - 1 ):
        for j in range( i + 1, n ):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    queue.put( A )
    
def ListMergeForProcess( intList, queue ):
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
    
    queue.put( temp )
                
            
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

def CutArrayForProcess( num, data, ProcessList ):
   
    cutLength = int( len(data) / num )
    
    for i in range(num):
        temp = []
        for _ in range(cutLength):
            temp.append( data.pop(0) )
            
        ProcessList.append( temp )
        
            
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
    
    while( len(intList ) != 1 ):
        ListMerge( intList )
    print(len(intList))

def Task3( number, data, ProcessList ):
    with mp.Manager() as Manager:
        processGroup = []
        tempQueue = mp.Queue()
        CutArray( number, data, ProcessList )
        for i in  range( number ):
            process = mp.Process( target = BubbleSortForProcess, args= ( ProcessList[i], tempQueue ) )
            process.start()
            processGroup.append( process )
            ProcessList[i] = tempQueue.get()
    
        for process in processGroup :
            process.join()
    
    
        for i in range( number - 1 ):
            process = mp.Process( target = ListMergeForProcess, args=  ( ProcessList, tempQueue ) )
            process.start()
            processGroup.append( process )
            ProcessList.append( tempQueue.get() )

        
        for process in processGroup :
            process.join()
    
    
    
    
def Task4( number, data, intList ):
    CutArray( number, data, intList )
    for i in range( len(intList) ):
        BubbleSort( intList[i] )
    
    for _ in range( number - 1 ):
        ListMerge( intList )

def main():
    
    data = []
    intList = []
    ProcessList = mp.Manager().list()
    
    fileName = input('請輸入檔案名稱or輸入0離開\n')
    
    while fileName != "0" :
        f = open(fileName + '.txt', 'r')
        task = int( f.readline() )
       
        
        for n in f.read().split():
            data.append( int(n) )
            
        startTime = time.time()
        
        if task == 1:
            BubbleSort( data )
            f = open("output1.txt", "w")
            endTime = time.time()
            print( 'Process Time = ', endTime - startTime, 'sec','\n' )
            
            f.write( str( data ) )
            f.write( '\n\nProcess Time = ' )
            f.write( str( endTime - startTime ) )
            f.write( ' sec' )
            
        elif task == 2:
            number = int(input('請輸入份數:\n'))
            Task2( number, data, intList )
            f = open("output2.txt", "w")
            endTime = time.time()
            print( 'Process Time = ', endTime - startTime, 'sec','\n' )
            
            f.write( str( intList ) )
            f.write( '\n\nProcess Time = ' )
            f.write( str( endTime - startTime ) )
            f.write( ' sec' )
 
        elif task == 3:
            number = int(input('請輸入份數:\n'))
            Task3( number, data, ProcessList )
            f = open("output3.txt", "w")
            endTime = time.time()
            print( 'Process Time = ', endTime - startTime, 'sec','\n' )
            
            f.write( str( ProcessList ) )
            f.write( '\n\nProcess Time = ' )
            f.write( str( endTime - startTime ) )
            f.write( ' sec' )
            

            
        elif task == 4:
            number = int(input('請輸入份數:\n'))
            Task4( number, data, intList )
            f = open("output4.txt", "w")
            endTime = time.time()
            print( 'Process Time = ', endTime - startTime, 'sec','\n' )
            
            f.write( str( intList ) )
            f.write( '\n\nProcess Time = ' )
            f.write( str( endTime - startTime ) )
            f.write( ' sec' )
            
        
        f.close()
        data.clear()
        intList.clear()
        ProcessList = []
        fileName = input('請輸入檔案名稱or輸入0離開\n')
    print('bye')


if __name__ == '__main__':
    main()
    
    
    
    
    
