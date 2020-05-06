import threading
import time
from queue import Queue



def BubbleSort( A ):
    n = len( A )
    for i in range( 0, n - 1 ):
        for j in range( i + 1, n ):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                
def MergeSort( A ):
    n = len( A )
    _MergeSort( A, 0, n - 1 )


def _MergeSort( A, p, r ):
    if p < r:
        q = ( p + r ) // 2
        _MergeSort( A, p, q )
        _MergeSort( A, q + 1, r )
        Merge( A, p, q, r )


def Merge( A, p, q, r ):
    n1 = q - p + 1
    n2 = r - q
    
    L = []
    R = []
    for i in range( n1 ):
        L.append( A[p + i] )
        
    for j in range( n2 ):
        R.append( A[q + j + 1] )
        
    i = j = 0
    for k in range( p, r + 1 ):
        if i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        elif i < n1 and j >= n2:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            
def ListMerge( num, intList ):
    print( intList )
    for _ in range( num -1 ):
        pop = intList.pop(0) + intList.pop(0)
        MergeSort( pop )
        intList.append( pop )
        print( intList )
    
            
            
    
                
                
def CutArray( num, data, intList ):
   
    j  = 0
    cutLength = int( len(data) / num )
    
    for i in range(num):
        temp = []
        for _ in range(cutLength):
            
            temp.append( data.pop(0) )
            
        intList.append( temp )
        
            
def Task2( intList ):
    a = 1
    
def Task3( intList ):
    a = 1
    
    
def Task4( number, data, intList ):
    print( data )
    CutArray( number, data, intList )
    for i in range( len(intList) ):
        BubbleSort( intList[i] )
    
    ListMerge( number, intList )


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
            
        elif task == 2:
            number = int(input('請輸入份數:\n'))
            CutArray( number, data, intList )
            Task2( intList )
            
            
        elif task == 3:
            number = int(input('請輸入份數:\n'))
            CutArray( number, data, intList )

            
        else:
            number = int(input('請輸入份數:\n'))
            Task4( number, data, intList )
            
        endTime = time.time()
        print( 'Sort Time = ', endTime - startTime, '\n' )
        
        f.close()
        fileName = input('請輸入檔案名稱or輸入0離開\n')
    print('bye')


if __name__ == '__main__':
    main()
    
    
    
    
    
