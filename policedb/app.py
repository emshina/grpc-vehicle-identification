import grpc
import mysql.connector
from concurrent import futures
import policestation_pb2 as pb
import policestation_pb2_grpc as pb_grpc

class policestationService(pb_grpc.policestationServiceServicer):
    
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
        
 
 
    def FetchCharges(self , request ,context):
        response = pb.FetchchargesResponse()
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            # Execute your database logic here
            fetchNTSA_query = "SELECT * FROM carownerapp_charges WHERE Police_station_code_id = %s"
            fetchNTSA_values = (request.Police_station_code_id,)
            m =request.Police_station_code_id
            # print(m)
            cursor.execute(fetchNTSA_query,fetchNTSA_values)
            rows = cursor.fetchall()
            # print('pk')
            for row in rows:
                # print(row[0],row[1],row[2])
                result =response.Charges_entries.add()
                result.Number_plate = row[3]
                result.charges = row[2]
                result.id = row[0]    
                result.date = row[2]         
            cursor.close()
    
            return response
     
        except mysql.connector.Error as error:
            print('error' ,error)
            # response.success = False
            # response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
           
    
    
    
    def InsertCharges(self, request, context):
        response = pb.InsertChargesResponse()
        
        # Connect to MySQL database
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            # Execute your database logic here
            insertCharges_query = "INSERT INTO carownerapp_charges(Number_Plate_id, Charges,Police_station_code_id) VALUES(%s,%s,%s)"
            insertCharges_values = (request.Number_plate, request.charges, request.Police_station_code_id)
            cursor.execute(insertCharges_query, insertCharges_values)
            cnx.commit()
            response.success = True
        except mysql.connector.Error as error:
            response.success = False
            response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
        
        return response
    
    
    def Police_station(self , request ,context):
        response = pb.PolicestationResponse()
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            # Execute your database logic here
            policeStation_query = "SELECT station_name,Police_station_code FROM carownerapp_police_station WHERE POlice_station_code = %s "
            policestation_values = (request.Police_station_code,)
            cursor.execute(policeStation_query,policestation_values)
            rows = cursor.fetchall()
            print('pk')
            for row in rows:
                # print(row[0],row[1],row[2])
                result =response.station_entries.add()
                x =result.station_name = row[0]
                y = result.Police_station_code = row[1]
                # print( x )
                # print(y)
                       
            cursor.close()
    
            return response
     
        except mysql.connector.Error as error:
            print('error' ,error)
            # response.success = False
            # response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
        
        
        
        
        
    # def DeleteCharges(self , request ,context):
    #     response = pb.DeleteChargesResponse()
        
        
    #     cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
    #     cursor = cnx.cursor()
  
            
    #     deleteCharges_query = "DELETE FROM carownerapp_charges WHERE Police_station_code_id = %s AND id = %s"
    #     deleteCharges_num= (request.police_code ,request.ID)
    #     # deleteCharges_num= (474 ,31)
       
    #     cursor.execute(deleteCharges_query, deleteCharges_num)
    #     cnx.commit()
    #     response.success = True

    #     cursor.close()
    #     cnx.close()
        
    #     return response
    
    def DeleteCharges(self , request ,context):
        response = pb.DeleteChargesResponse()
        cnx = mysql.connector.connect(host="localhost",user="root",password="?00chin@",database="policestationa")
        cursor = cnx.cursor()
        
        try:
            
            deleteCharges_query = "DELETE FROM carownerapp_charges WHERE Police_station_code_id = %s AND id = %s"
      
            deleteCharges_num= (request.police_code ,request.ID ,)

            cursor.execute(deleteCharges_query, deleteCharges_num)
            cnx.commit()
            response.success = True
        except mysql.connector.Error as error:
            response.success = False
            response.error = str(error)
        
        # Close database connection
        cursor.close()
        cnx.close()
        
        return response
    
    
    
    
    
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_policestationServiceServicer_to_server(policestationService(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
    # pk = policestationService()
    # pk.DeleteCharges(' request' ,'context')