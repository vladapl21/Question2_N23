Queue = [0 for i in range(50)]
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
  global Queue
  global TailPointer
  if TailPointer < 50:
    Queue[TailPointer] = Data
    TailPointer += 1
  else:
    print("Queue is full")
    
def Dequeue():
  global Queue
  global HeadPointer
  if HeadPointer < TailPointer:
    HeadPointer += 1
    return Queue[HeadPointer]
  else:
    return "Empty"

def ReadData():
  f = open("QueueData.txt", "r")
  for i in range(23):
    Data = f.readline()
    Data = Data.strip("\n")
    Enqueue(Data)
  f.close()



class RecordData:
  def __init__(self, ID, Total):
    self.ID = ID # of data type STRING
    self.Total = Total #of data type INTEGER

Records = [] # of data type RecordData and length 50
NumberRecords = 0 # of data type INTEGER

def TotalData():
  global Records
  global NumberRecords
  Flag = False
  Data = Dequeue()
  for i in range(len(Records)):
    if Data == Records[i].ID:
      Records[i].Total += 1
      Flag = True
      break
  if not Flag:
    Records.append(RecordData(Data, 1))
    NumberRecords += 1

def OutputRecords():
  for i in range(NumberRecords):
    print(f'ID {Records[i].ID}   Total {Records[i].Total}')

ReadData()
for i in range(23):
  TotalData()
OutputRecords()
    