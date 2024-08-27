import abc
from src.model.user import User, db
import sqlalchemy

class userDAOInterface(abc.ABC):
    @abc.abstractmethod
    def build_user(self, data):
        pass
    
    @abc.abstractmethod    
    def search_user(self, data):
        pass

    @abc.abstractmethod
    def insert_user(self, data):
        pass

    @abc.abstractmethod    
    def update_user(self, data):
        pass

    @abc.abstractmethod
    def delete_user(self, id):
        pass

class UserDAO(userDAOInterface):
    
    
    
    def build_user(self, data):
        return ( User.setName(data.name), User.setEmail(data.email), User.setDDD(data.ddd), User.setPhone(data.phone), User.setNumber_residence(data.number_residence), User.setStreet(data.street), User.setDistrict(data.district), User.setCity(data.city), User.setState(data.state), User.setCep(data.cep), User.setPassword(data.password) )
    
    def search_user(self, data):
       return
    
    def insert_user(self, data):
       return 

    def update_user(self, data):
       return 

    def delete_user(self, id):
       return 
   