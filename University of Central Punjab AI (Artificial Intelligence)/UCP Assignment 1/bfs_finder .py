import sys



class File_Error(Exception):
   
   pass

class ReadFile():

  def read_file(self):
    try:
      f = open('graph.txt')
      s = f.readline()
      i = int(s.strip())


    except (IOError):

      print ("File not Available in System so this is SYSTEM Error")

    except ValueError:

      print ("Graph not enter correctly or may b string Error  occurs so I am Shifting Graph Reading Manually Please change Data in Graph list .")

    except:
      print ("Unexpected error:", sys.exc_info()[0])
      raise


class BFS():

  def bfs_finder(self,graph, start):

    try:

      visited, queue = set(), [start]
      print("Visited Paths")

      while queue:
        vertex = queue.pop(0) # pop shallowest node (first node) from queue

        if vertex not in visited:

          visited.add(vertex)

          print(graph[vertex],visited,graph[vertex] - visited )
          queue.extend(graph[vertex] - visited)

      return visited

    except (ValueError,TypeError,IndexError,KeyError,File_Error):

      print("File or Value not found Error please try another Character Value and make sure file exits")


    
            

if __name__ == '__main__':

  read=ReadFile()

  read.read_file()

  


  graph = {'A': set(['G', 'A']),
         'B': set(['C', 'D', 'B']),
         'E': set(['F', 'G']),
         'E': set(['K','L']),
       
         
         }


  result=BFS()
  final_nodes=result.bfs_finder(graph,'A')

  print("visited nodes:")
  print(final_nodes)

  file1 = open('output.txt', 'a')
    
   
  file1.close()
    
    




    

        
        


  
