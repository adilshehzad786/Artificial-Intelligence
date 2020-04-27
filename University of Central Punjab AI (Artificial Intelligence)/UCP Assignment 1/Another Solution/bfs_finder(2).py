
graph = {'A': set(['G', 'A']),
         'B': set(['C', 'D', 'B']),
         'E': set(['F', 'G']),
         'E': set(['K','L']),
       
         
         }
class FileReading():

	 def read(self):

	 	try:
	 		file=open('input.txt')
	 		file.readline()

	 	except(IOError):

	 		print("File not found")


class MYBFS():

 	def bfs_searching(self,start, end_node):

 		visited = []
 		queue = [start]
 		while len(queue)>0:

 			current_node=queue.pop(0)
 			visited.append(current_node)

 			print("Visiting",current_node)

 			if current_node==end_node:

 				print("Found ")

 				return True

 			for items in current_node:

 				if items not in visited and items not in queue:

 					queue.append(items)




   

   

  

if __name__ == '__main__':


	
	reading=FileReading()

	final_reading=reading.read()

	


	

result=MYBFS()

result.bfs_searching(graph,'A')



   


