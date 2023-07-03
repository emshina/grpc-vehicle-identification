import grpc
import mysql.connector
from concurrent import futures
import registration_pb2 as pb
import registration_pb2_grpc as pb_grpc

class registrationService(pb_grpc.registrationServiceServicer):
    def Insert(self, request, context):
        response = pb.InsertResponse()
        
        # Connect to MySQL database
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            # Execute your database logic here
            insert_query = "INSERT INTO carownerapp_registration(Number_Plate,email,ID_id) VALUES (%s, %s, %s)"
  
            insert_values = (request.Number_plate, request.email, request.id)
            cursor.execute(insert_query, insert_values)
            cnx.commit()
            response.success = True
        except mysql.connector.Error as error:
            response.success = False
            response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
        
        return response
    def Fetch(self , request ,context):
        response = pb.FetchResponse()
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            # Execute your database logic here
            fetch_query = "SELECT Number_plate,email,ID_id FROM carownerapp_registration"
     
            # fetch_values = (request.Number_plate, request.email, request.id)
            cursor.execute(fetch_query)
            rows = cursor.fetchall()
            print('pk')
            for row in rows:
                # print(row[0],row[1],row[2])
                result =response.data_entries.add()
                result.Number_plate = row[0]
                result.email = row[1]
                result.id = row[2]           
            cursor.close()
    
            return response
     
        except mysql.connector.Error as error:
            print('error' ,error)
            # response.success = False
            # response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
        
        
    def Delete(self , request ,context):
        response = pb.DeleteResponse()
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            
            delete_query = "DELETE FROM carownerapp_registration  WHERE Number_plate = %s"
      
            delete_num= (request.Number_plate,)

            cursor.execute(delete_query, delete_num)
            cnx.commit()
            response.success = True
        except mysql.connector.Error as error:
            response.success = False
            response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
        
        return response
    
    
    
    def Update(self, request, context):
        response = pb.UpdateResponse()
        
        # Connect to MySQL database
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
  
            
            update_query = "UPDATE carownerapp_registration SET Number_Plate =%s, email= %s, ID_id=%s WHERE Number_Plate = %s "
        
            
            update_values = (request.Number_plate, request.email, request.id,request.condition)
            cursor.execute(update_query, update_values)
            cnx.commit()
            response.success = True
        except mysql.connector.Error as error:
            response.success = False
            response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
        
        
        
    def FetchNTSA(self , request ,context):
        response = pb.FetchNTSAResponse()
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            # Execute your database logic here
            fetchNTSA_query = "SELECT Number_plate,email, ID_id FROM carownerapp_registration WHERE Number_plate= %s "
            fetchNTSA_values = (request.Number_plate,)
            print(fetchNTSA_values)
            
            
            cursor.execute(fetchNTSA_query,fetchNTSA_values)
            
            rows = cursor.fetchone()
            
            # print(rows)
            result =response.data_entries.add()
            result.Number_plate = rows[0]
            result.email = rows[1]
            result.id = rows[2]   
                # result.date = row[3]         
            cursor.close()
    
            return response
     
        except mysql.connector.Error as error:
            print('error' ,error)
            # response.success = False
            # response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_registrationServiceServicer_to_server(registrationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()